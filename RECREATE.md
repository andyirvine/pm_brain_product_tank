# Prompt: Recreate the Product Brain Application

Use the following prompt to recreate the application code. It assumes you already have the markdown data files (Company/, pm-brain/, User Data/) in place.

---

Build a Flask web application called **Product Brain** that reads a folder of markdown strategy documents and customer research files, visualises them as a strategy dashboard, and lets users query them via the Anthropic Claude API.

## Tech Stack

- **Backend**: Python 3, Flask
- **AI**: Anthropic Claude API (claude-sonnet-4-6), streaming via Server-Sent Events
- **Frontend**: Jinja2, Bootstrap 5 (grid only), Bootstrap Icons, Chart.js, Marked.js, vanilla JS
- **Data**: `hunches.json` and `hypotheses.json` for ideas; everything else is markdown files on disk
- **Dependencies**: flask>=3.0.0, anthropic>=0.25.0, python-dotenv>=1.0.0, markdown>=3.5.0, gunicorn>=21.2.0, python-pptx>=0.6.23

## Files to Create

```
app.py
generate_pptx.py
requirements.txt
.env                  # ANTHROPIC_API_KEY, CLAUDE_MODEL
render.yaml
hunches.json          # empty array []
hypotheses.json       # empty array []
templates/
  base.html
  dashboard.html
  data.html
  query.html
  hunches.html
  reports.html
  report.html
static/css/style.css
Reports/              # empty directory for saved query outputs
```

---

## app.py

### Configuration

```python
from pathlib import Path
BASE_DIR = Path(__file__).parent
REPORTS_DIR = BASE_DIR / "Reports"

PRODUCT_AREAS = [
    "Invoicing & Collections",
    "Tax & Compliance",
    "Cashflow & Forecasting",
    "Accountant Experience",
    "Platform & Core",
]

DOCS = {
    "okrs":        {"file": "Company/company-okrs.md",          "title": "Company OKRs",          "icon": "bullseye"},
    "bets":        {"file": "Company/hypothesis-evidence.md",   "title": "Strategic Bets",         "icon": "lightning"},
    "competitive": {"file": "Company/competitive-landscape.md", "title": "Competitive Landscape",  "icon": "binoculars"},
    "market":      {"file": "Company/market-shifts.md",         "title": "Market Shifts",          "icon": "graph-up"},
    "jobs":        {"file": "Company/job-1-get-paid.md",        "title": "Jobs to Be Done",        "icon": "briefcase"},
}
```

### Routes

| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Dashboard |
| `/data` | GET | Tabbed markdown document viewer |
| `/query` | GET | AI query interface |
| `/api/query` | POST | Streaming Claude endpoint (SSE) |
| `/reports` | GET | List saved reports |
| `/reports/<filename>` | GET | Report detail |
| `/api/save-report` | POST | Save a query answer as a .md file |
| `/export/pptx` | GET | Generate and download PowerPoint |
| `/hunches` | GET | Idea capture interface |
| `/api/hunches` | POST | Create hunch |
| `/api/hunches/<id>` | PATCH | Update / promote hunch |
| `/api/hunches/<id>` | DELETE | Delete hunch |

### Dashboard data — `build_dashboard_data()`

Calls four parser functions that read markdown live (no caching). Returns a dict passed to `dashboard.html`.

**`_parse_bets()`** — reads `Company/hypothesis-evidence.md`, regex-extracts markdown table rows. Maps status emojis: ✅ → "validated", 🧪 → "hypothesis", ❌ → "rejected". Maps confidence strings: VERY HIGH → 5, HIGH → 4, MEDIUM → 3, LOW → 2. Counts `[I-` occurrences per row as evidence count. Returns list of `{name, status, confidence (int), label, evidence (int)}`.

**`_parse_competitors()`** — reads `Company/competitive-landscape.md`. For each `## Heading` block extracts: `**Funding**: $<float>M`, `**Customers**: <int>` (handles K suffix), `**Threat**: HIGH|MEDIUM|LOW`. Returns list of `{name, funding, customers, threat}`.

**`_parse_okr_targets()`** — reads `Company/company-okrs.md`. Extracts markdown table rows with columns `Metric | Current | Target | Unit`. Assigns a hex color per row (cycle through a palette). Returns list of `{label, current, target, unit, color}`.

**`_parse_market_stats()`** — reads `Company/market-shifts.md`. Extracts numbered list items (e.g. `1. **47M** freelancers...`). Assigns a Bootstrap icon name and hex color per stat. Returns list of `{label, value, sub, icon, color}`.

### Context builder — `build_context()`

Walks `Company/`, `pm-brain/`, and `User Data/` recursively, reads every `.md` file, and concatenates them with a `### <relative path>` header between each. Returns a single string used as Claude's system message.

### Streaming query — `POST /api/query`

Accepts JSON `{"question": "..."}`. Builds context, then calls `client.messages.stream()` with the context as system and the question as user message. Uses Flask `stream_with_context()` to yield SSE chunks: `data: <text chunk>\n\n`. Sends `data: [DONE]\n\n` when complete. On error, yields `data: [ERROR] <message>\n\n`.

### Hunch/Hypothesis CRUD

Load/save `hunches.json` and `hypotheses.json` as JSON arrays on every request (no in-memory state). Use `uuid.uuid4()` for IDs and `datetime.now().isoformat()` for timestamps.

`PATCH /api/hunches/<id>` with `{"action": "promote"}`:
1. Finds hunch by id, sets `promotedToHypothesis = True`
2. Creates new hypothesis object in `hypotheses.json` with `hunchId` reference and `status = "hypothesis"`
3. Saves both files, returns the new hypothesis

### Report saving — `POST /api/save-report`

Accepts `{"question": "...", "answer": "..."}`. Filename: `YYYY-MM-DD_HH-MM-SS_<slug>.md` where slug is the question lowercased, non-alphanumeric replaced with hyphens, truncated to 50 chars. File content: `# <question>\n\n---\n\n<answer>`. Saves to `Reports/`.

---

## generate_pptx.py

Exports the same dashboard data to a PowerPoint file using python-pptx. Entry point: `generate_pptx(data) -> str` (returns the output file path).

Slides:
1. Title slide — app name, date
2. Strategic Bet Confidence — bar chart, x-axis 0–5
3. Bet Status Breakdown — pie/doughnut chart (validated / hypothesis / rejected counts)
4. Customer Evidence per Bet — bar chart
5. Competitor Landscape — scatter chart (x = funding $M, y = customers)
6. OKR Targets — table with current vs target and unit
7. Competitor Threat Matrix — table with name and threat level

Use a color palette matching the web app theme (indigo primary #6366f1, green #22c55e, amber #f59e0b, red #ef4444). Return the file path; Flask streams it as a download attachment with a timestamped filename.

---

## Templates

### base.html

- Dark sidebar: background #0f172a, fixed position, 240px wide
- Nav links: Dashboard (`/`), Strategy Docs (`/data`), AI Query (`/query`), Hunches (`/hunches`), Reports (`/reports`)
- CDN includes: Chart.js, Marked.js, Bootstrap 5 grid CSS, Bootstrap Icons
- Link to `/static/css/style.css`
- `{% block content %}{% endblock %}` in main area

### dashboard.html

Bootstrap grid layout. Sections in order:

1. Page header — title, subtitle, last-updated timestamp
2. Four market stat cards — value, label, Bootstrap icon, colored top border
3. **Strategic Bet Confidence** — `Chart.js` horizontal bar chart, data from `bets[].confidence` (0–5 scale)
4. **Bet Status Breakdown** — doughnut chart, counts of validated / hypothesis / rejected
5. **Customer Evidence per Bet** — vertical bar chart, data from `bets[].evidence`
6. **Competitor Landscape** — scatter chart, x = `competitors[].funding`, y = `competitors[].customers`, point labels are competitor names
7. **OKR Targets** — progress bars, each showing current vs target with unit label
8. **Competitor Threat Levels** — card list with HIGH / MEDIUM / LOW badges
9. Export button → `GET /export/pptx`

### data.html

Tab buttons for each key in `DOCS`. Clicking a tab renders the markdown document as HTML in a content pane. Render server-side using Python's `markdown` library; pass rendered HTML to the template.

### query.html

- Scrollable message display area; renders streamed chunks using `marked.parse()`
- Suggested query chips (3–5 hardcoded questions) that populate the textarea on click
- Auto-resizing `<textarea>` for the question
- Submit button — POSTs to `/api/query`, reads SSE stream, appends chunks to display
- "Save as Report" button — appears after an answer is received, POSTs to `/api/save-report`

### hunches.html

- New hunch form: `<textarea>` for body, `<select>` for productArea (from PRODUCT_AREAS passed by Flask), `<input>` for okrLink, radio buttons for confidence (low / medium / high)
- Filter chips: All / High / Medium / Low / Promoted — filter the list client-side
- Hunch cards: body text, product area, confidence badge, created date
- Promote button (disabled + greyed if `promotedToHypothesis` is true)
- Delete button

### reports.html

List of report files in `Reports/`, sorted newest first. Each row: date parsed from filename, report title (first line of file), link to detail view.

### report.html

Display report title and full content rendered as markdown HTML. Download button.

---

## static/css/style.css

```css
:root {
  --sidebar-width: 240px;
  --primary: #6366f1;
  --success: #22c55e;
  --warning: #f59e0b;
  --danger: #ef4444;
  --surface: #ffffff;
  --bg: #f8fafc;
  --border: #e2e8f0;
  --text: #1e293b;
  --text-muted: #64748b;
}
```

- `body { display: flex; min-height: 100vh; background: var(--bg); }`
- Sidebar: fixed, left 0, full height, `width: var(--sidebar-width)`, dark background
- Main content: `margin-left: var(--sidebar-width)`, padding, flex-grow
- Cards: white, `border-radius: 12px`, subtle box-shadow, `border: 1px solid var(--border)`
- Chart containers: `.chart-wrap { height: 300px; position: relative; }`
- Filter chips: pill buttons with hover and `.active` states
- Responsive via Bootstrap grid classes (`col-lg-6`, `col-xl-4`)

---

## Deployment

**.env:**
```
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-sonnet-4-6
```

**render.yaml:**
```yaml
services:
  - type: web
    name: product-brain
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
    envVars:
      - key: ANTHROPIC_API_KEY
        sync: false
      - key: CLAUDE_MODEL
        value: claude-sonnet-4-6
```

**Local:**
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# add ANTHROPIC_API_KEY to .env
python app.py  # http://localhost:8080
```
