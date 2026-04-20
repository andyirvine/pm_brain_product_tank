import os
import json
import re
import uuid
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, jsonify, request, Response, stream_with_context, send_file
import markdown
from dotenv import load_dotenv
import anthropic

load_dotenv()

app = Flask(__name__)

BASE_DIR       = Path(__file__).parent
REPORTS_DIR    = BASE_DIR / "reports"
HUNCHES_FILE   = BASE_DIR / "hunches.json"
HYPOTHESES_FILE = BASE_DIR / "hypotheses.json"
REPORTS_DIR.mkdir(exist_ok=True)

PRODUCT_AREAS = [
    "Invoicing & Collections",
    "Tax & Compliance",
    "Cashflow & Forecasting",
    "Accountant Experience",
    "Platform & Core",
]

# ── Document Registry ────────────────────────────────────────────────────────

def _discover_interviews() -> dict:
    """Dynamically discover all interview files in User Data/."""
    user_data = BASE_DIR / "User Data"
    if not user_data.exists():
        return {}
    docs = {}
    for path in sorted(user_data.glob("interview-*.md")):
        key = path.stem
        title = path.stem.replace("-", " ").title()
        docs[key] = {
            "title": title,
            "file": path,
            "icon": "person-lines-fill",
            "description": f"Customer interview: {title}",
        }
    return docs

DOCS = {
    # ── Company ──────────────────────────────────────────────────────────────
    "okrs": {
        "title": "Company OKRs",
        "file": BASE_DIR / "Company" / "company-okrs.md",
        "icon": "bullseye",
        "description": "Company objectives and key results for 2024",
    },
    "bets": {
        "title": "Strategic Bets",
        "file": BASE_DIR / "Company" / "hypothesis-evidence.md",
        "icon": "lightning-fill",
        "description": "Hypothesis-evidence tracking across all 9 strategic bets",
    },
    "competitive": {
        "title": "Competitive Landscape",
        "file": BASE_DIR / "Company" / "competitive-landscape.md",
        "icon": "diagram-3-fill",
        "description": "Direct and indirect competitor analysis",
    },
    "market": {
        "title": "Market Shifts",
        "file": BASE_DIR / "Company" / "market-shifts.md",
        "icon": "graph-up-arrow",
        "description": "6 macro trends affecting Ledger's strategy",
    },
    "job1": {
        "title": "Job: Get Paid",
        "file": BASE_DIR / "Company" / "job-1-get-paid.md",
        "icon": "person-check-fill",
        "description": "Core job: Get Paid by My Clients",
    },
    "job2": {
        "title": "Job: File Taxes",
        "file": BASE_DIR / "Company" / "job-2-file-taxes.md",
        "icon": "receipt",
        "description": "Core job: File My Taxes Without Stress",
    },
    "job3": {
        "title": "Job: Cashflow Decisions",
        "file": BASE_DIR / "Company" / "job-3-cashflow-decisions.md",
        "icon": "cash-stack",
        "description": "Core job: Make Smart Cashflow Decisions",
    },
    # ── PM Brain: Invoicing & Collections ────────────────────────────────────
    "inv-signals": {
        "title": "Signals Synthesis",
        "file": BASE_DIR / "pm-brain" / "invoicing-collections" / "signals-synthesis.md",
        "icon": "broadcast",
        "description": "Customer signal synthesis — Invoicing & Collections",
    },
    "inv-okrs": {
        "title": "Team OKRs",
        "file": BASE_DIR / "pm-brain" / "invoicing-collections" / "team-okrs.md",
        "icon": "bullseye",
        "description": "Team objectives — Invoicing & Collections",
    },
    "inv-bets": {
        "title": "Hypothesis & Evidence",
        "file": BASE_DIR / "pm-brain" / "invoicing-collections" / "hypothesis-evidence.md",
        "icon": "lightning-fill",
        "description": "Strategic bets — Invoicing & Collections",
    },
    "inv-segments": {
        "title": "Customer Segments",
        "file": BASE_DIR / "pm-brain" / "invoicing-collections" / "customer-segments.md",
        "icon": "people-fill",
        "description": "Customer segments — Invoicing & Collections",
    },
    # ── PM Brain: Tax & Compliance ────────────────────────────────────────────
    "tax-signals": {
        "title": "Signals Synthesis",
        "file": BASE_DIR / "pm-brain" / "tax-compliance" / "signals-synthesis.md",
        "icon": "broadcast",
        "description": "Customer signal synthesis — Tax & Compliance",
    },
    "tax-okrs": {
        "title": "Team OKRs",
        "file": BASE_DIR / "pm-brain" / "tax-compliance" / "team-okrs.md",
        "icon": "bullseye",
        "description": "Team objectives — Tax & Compliance",
    },
    "tax-bets": {
        "title": "Hypothesis & Evidence",
        "file": BASE_DIR / "pm-brain" / "tax-compliance" / "hypothesis-evidence.md",
        "icon": "lightning-fill",
        "description": "Strategic bets — Tax & Compliance",
    },
    "tax-segments": {
        "title": "Customer Segments",
        "file": BASE_DIR / "pm-brain" / "tax-compliance" / "customer-segments.md",
        "icon": "people-fill",
        "description": "Customer segments — Tax & Compliance",
    },
    # ── User Research ─────────────────────────────────────────────────────────
    "interview-index": {
        "title": "Interview Index",
        "file": BASE_DIR / "User Data" / "00_INTERVIEW_INDEX.md",
        "icon": "card-list",
        "description": "Index of all customer interviews",
    },
    "interview-log": {
        "title": "Interview Log",
        "file": BASE_DIR / "User Data" / "interview-log.md",
        "icon": "journal-text",
        "description": "Complete log of all interview sessions",
    },
    "interviews-summary": {
        "title": "Interviews Summary",
        "file": BASE_DIR / "User Data" / "INTERVIEWS_SUMMARY.md",
        "icon": "file-earmark-text-fill",
        "description": "Key findings synthesised across all interviews",
    },
    "signals": {
        "title": "Signals Synthesis",
        "file": BASE_DIR / "User Data" / "signals-synthesis.md",
        "icon": "broadcast",
        "description": "Cross-interview signal synthesis",
    },
    **_discover_interviews(),
}

# Navigation sections — controls grouping in the data page sidebar
DOC_SECTIONS = [
    {
        "label": "Company",
        "icon": "building",
        "docs": ["okrs", "bets", "competitive", "market", "job1", "job2", "job3"],
    },
    {
        "label": "PM Brain: Invoicing",
        "icon": "receipt-cutoff",
        "docs": ["inv-signals", "inv-okrs", "inv-bets", "inv-segments"],
    },
    {
        "label": "PM Brain: Tax",
        "icon": "calculator",
        "docs": ["tax-signals", "tax-okrs", "tax-bets", "tax-segments"],
    },
    {
        "label": "User Research",
        "icon": "people",
        "docs": ["interview-index", "interview-log", "interviews-summary", "signals"],
        "subsections": [
            {
                "label": "Customer Interviews",
                "icon": "person-lines-fill",
                "docs": [k for k in _discover_interviews()],
            }
        ],
    },
]

# ── Dashboard Parsers ─────────────────────────────────────────────────────────
# All dashboard data is derived live from the markdown files.
# Edit any .md file → refresh the browser → charts update automatically.

_CONF_MAP = {
    "VERY HIGH": 5, "HIGH": 4, "MEDIUM-HIGH": 3.5,
    "MEDIUM": 3, "LOW-MEDIUM": 2, "LOW": 1.5,
}
_OKR_COLORS = ["#6366f1", "#22c55e", "#f59e0b", "#06b6d4", "#8b5cf6", "#ec4899", "#f97316"]


def _parse_bets() -> list:
    path = BASE_DIR / "Company" / "hypothesis-evidence.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")

    # Pass 1 — collect evidence counts from body sections
    evidence_map: dict[str, int] = {}
    for section in re.split(r'\n## Bet \d+', text)[1:]:
        first_line = section.split('\n')[0]
        bet_name = re.sub(r'^[:\s—–\-]+', '', first_line).strip()
        gp = re.search(r'General pattern[^\n]*?(\d+)[/+]', section)
        if gp:
            evidence_map[bet_name] = int(gp.group(1))

    # Pass 2 — parse the structured summary table
    table = re.search(
        r'\| Bet \| Status \| Confidence \| Action \|(.+?)(?=\n\n---|\Z)',
        text, re.DOTALL
    )
    if not table:
        return []

    bets = []
    for row in re.findall(r'^\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|', table.group(), re.MULTILINE):
        name_raw, status_raw, conf_raw, _ = [c.strip() for c in row]
        if not name_raw or name_raw.lower().startswith('bet') or set(name_raw) <= {'-', ' '}:
            continue

        name     = re.sub(r'^\d+\.\s*', '', name_raw)
        conf_key = re.sub(r'[^A-Z\- ]', '', conf_raw.upper()).strip()
        conf_num = _CONF_MAP.get(conf_key, 2)

        if '⚠️' in status_raw or 'Reject' in status_raw or 'Challenged' in status_raw:
            status, conf_num = 'rejected', 0
        elif '🔄' in status_raw or 'Hypothesis' in status_raw:
            status = 'hypothesis'
        elif conf_key == 'VERY HIGH':
            status = 'very-high'
        elif '✅' in status_raw or 'Validated' in status_raw:
            status = 'validated'
        else:
            status = 'medium'

        # Match evidence count by partial name overlap
        evidence = next(
            (v for k, v in evidence_map.items() if any(w in k for w in name.split()[:2])),
            0
        )

        bets.append({
            "name": name, "confidence": conf_num, "prev": conf_num,
            "status": status, "label": conf_raw, "evidence": evidence,
        })

    return bets


def _parse_competitors() -> list:
    path = BASE_DIR / "Company" / "competitive-landscape.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")

    tier1 = re.split(r'## Tier 2', text, maxsplit=1)[0]
    competitors = []

    for section in re.split(r'\n### ', tier1)[1:]:
        name = section.split('\n')[0].strip()
        if not name or name.lower().startswith(('competitive', 'tier')):
            continue

        funding = 0.0
        fm = re.search(r'\$([\d.]+)M\s*raised', section)
        if fm:
            funding = float(fm.group(1))

        customers = 0
        cm = re.search(r'~?([\d,]+)\s*paying', section)
        if cm:
            customers = int(cm.group(1).replace(',', ''))

        threat = "MEDIUM"
        tm = re.search(r'\*\*Threat Level\*\*:\s*\*\*([A-Z\-]+)', section)
        if tm:
            threat = tm.group(1)

        competitors.append({"name": name, "funding": funding, "customers": customers, "threat": threat})

    return competitors or [
        {"name": "Cleo Finance", "funding": 8.2, "customers": 2400, "threat": "HIGH"},
        {"name": "TaxWise Pro",  "funding": 0,   "customers": 8000, "threat": "MEDIUM"},
        {"name": "Pulseflow",    "funding": 2.1, "customers": 320,  "threat": "LOW"},
        {"name": "Meridian",     "funding": 24,  "customers": 9000, "threat": "LOW"},
    ]


def _parse_okr_targets() -> list:
    path = BASE_DIR / "Company" / "company-okrs.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")

    table = re.search(
        r'\| Metric \| Baseline \| Target \|.+?(?=\n\n---|\Z)',
        text, re.DOTALL
    )
    if not table:
        return []

    targets = []
    for i, row in enumerate(re.findall(
        r'^\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|',
        table.group(), re.MULTILINE
    )):
        label, _, target_raw, *_ = [c.strip() for c in row]
        if not label or label.lower() in ('metric', '---') or set(label) <= {'-', ' '}:
            continue
        nm = re.search(r'[\d.]+', target_raw)
        target_val = float(nm.group()) if nm else 0
        unit = 'K$' if ('$' in target_raw and 'K' in target_raw) else \
               '%'  if ('%' in target_raw or 'MAU' in target_raw) else \
               'pts' if 'NPS' in label else ''
        targets.append({
            "label": label, "target": target_val, "current": 0,
            "unit": unit, "color": _OKR_COLORS[i % len(_OKR_COLORS)],
        })

    return targets or [
        {"label": "MRR",                "target": 50, "current": 0, "unit": "K$",  "color": "#6366f1"},
        {"label": "NPS Score",          "target": 40, "current": 0, "unit": "pts", "color": "#22c55e"},
        {"label": "Tax Clarity NPS",    "target": 70, "current": 0, "unit": "%",   "color": "#f59e0b"},
        {"label": "Time Reduction",     "target": 50, "current": 0, "unit": "%",   "color": "#06b6d4"},
        {"label": "Feature Adoption",   "target": 80, "current": 0, "unit": "%",   "color": "#8b5cf6"},
        {"label": "Accountant Partners","target": 50, "current": 0, "unit": "",    "color": "#ec4899"},
        {"label": "Referral %",         "target": 25, "current": 0, "unit": "%",   "color": "#f97316"},
    ]


def _parse_market_stats() -> list:
    path = BASE_DIR / "Company" / "market-shifts.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")

    stats = []
    patterns = [
        (r'(\d+) million Americans did freelance', lambda m: f"{m.group(1)}M",
         "US Freelancers", "+34% since 2019", "people-fill", "#6366f1"),
        (r'\$(\d+)M\+ in 2023', lambda m: f"${m.group(1)}M+",
         "AI Bookkeeping Raised", "in 2023 alone", "cpu-fill", "#f59e0b"),
        (r'(\d+) days \(2023\)', lambda m: m.group(1),
         "Avg Days-to-Payment", "days (up from 32)", "clock-fill", "#ef4444"),
        (r'(\d+)% of solopreneurs report reducing software', lambda m: f"{m.group(1)}%",
         "Freelancers Cutting SaaS", "in past 6 months", "scissors", "#8b5cf6"),
    ]
    for pattern, fmt, label, sub, icon, color in patterns:
        m = re.search(pattern, text)
        if m:
            stats.append({"label": label, "value": fmt(m), "sub": sub, "icon": icon, "color": color})

    return stats or [
        {"label": "US Freelancers",          "value": "64M",    "sub": "+34% since 2019",   "icon": "people-fill", "color": "#6366f1"},
        {"label": "AI Bookkeeping Raised",   "value": "$180M+", "sub": "in 2023 alone",      "icon": "cpu-fill",    "color": "#f59e0b"},
        {"label": "Avg Days-to-Payment",     "value": "41",     "sub": "days (up from 32)",  "icon": "clock-fill",  "color": "#ef4444"},
        {"label": "Freelancers Cutting SaaS","value": "38%",    "sub": "in past 6 months",   "icon": "scissors",    "color": "#8b5cf6"},
    ]


def build_dashboard_data() -> dict:
    return {
        "bets":        _parse_bets(),
        "competitors": _parse_competitors(),
        "okr_targets": _parse_okr_targets(),
        "market_stats": _parse_market_stats(),
    }

# ── Hunches helpers ───────────────────────────────────────────────────────────

def _load_hunches() -> list:
    if not HUNCHES_FILE.exists():
        return []
    return json.loads(HUNCHES_FILE.read_text(encoding="utf-8"))


def _save_hunches(hunches: list) -> None:
    HUNCHES_FILE.write_text(json.dumps(hunches, indent=2, ensure_ascii=False), encoding="utf-8")


def _load_hypotheses() -> list:
    if not HYPOTHESES_FILE.exists():
        return []
    return json.loads(HYPOTHESES_FILE.read_text(encoding="utf-8"))


def _save_hypotheses(hypotheses: list) -> None:
    HYPOTHESES_FILE.write_text(json.dumps(hypotheses, indent=2, ensure_ascii=False), encoding="utf-8")


# ── Helpers ───────────────────────────────────────────────────────────────────

def render_md(path: Path) -> str:
    """Read a markdown file and return rendered HTML."""
    if not path.exists():
        return "<p><em>File not found.</em></p>"
    raw = path.read_text(encoding="utf-8")
    return markdown.markdown(raw, extensions=["tables", "fenced_code", "attr_list"])


def build_context() -> str:
    """Concatenate all documents into a single context string for the LLM."""
    parts = []
    for key, doc in DOCS.items():
        if doc["file"].exists():
            parts.append(f"## {doc['title']}\n\n{doc['file'].read_text(encoding='utf-8')}")
    return "\n\n---\n\n".join(parts)


def _build_sections_for_template() -> list:
    """Return DOC_SECTIONS with only keys that exist on disk."""
    result = []
    for section in DOC_SECTIONS:
        valid_keys = [k for k in section["docs"] if k in DOCS and DOCS[k]["file"].exists()]
        if not valid_keys:
            continue
        entry = {**section, "docs": valid_keys}
        if "subsections" in section:
            subs = []
            for sub in section["subsections"]:
                sub_keys = [k for k in sub["docs"] if k in DOCS and DOCS[k]["file"].exists()]
                if sub_keys:
                    subs.append({**sub, "docs": sub_keys})
            entry["subsections"] = subs
        result.append(entry)
    return result


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def dashboard():
    return render_template("dashboard.html", data=json.dumps(build_dashboard_data()))


@app.route("/data")
def data():
    active = request.args.get("tab", "okrs")
    if active not in DOCS:
        active = "okrs"
    doc = DOCS[active]
    content_html = render_md(doc["file"])
    return render_template(
        "data.html",
        docs=DOCS,
        sections=_build_sections_for_template(),
        active_tab=active,
        content=content_html,
        doc_meta=doc,
    )


@app.route("/query")
def query_page():
    return render_template("query.html")


@app.route("/api/query", methods=["POST"])
def api_query():
    payload = request.get_json(silent=True) or {}
    question = payload.get("question", "").strip()
    if not question:
        return jsonify({"error": "No question provided"}), 400

    context = build_context()
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    model  = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")

    system_prompt = f"""You are an expert product strategy analyst embedded inside Ledger's Product Brain — \
a structured intelligence layer for a seed-stage fintech startup that helps small business owners \
manage invoicing, taxes, and cashflow.

Answer questions with precision, always citing specific evidence (interview numbers, data points, \
OKR metrics) from the documents below. Be concise but thorough. Use markdown formatting where helpful.

COMPANY DOCUMENTS:
{context}"""

    def generate():
        try:
            with client.messages.stream(
                model=model,
                max_tokens=2048,
                system=system_prompt,
                messages=[{"role": "user", "content": question}],
            ) as stream:
                for text in stream.text_stream:
                    yield f"data: {json.dumps(text)}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as exc:
            yield f"data: {json.dumps(f'Error: {exc}')}\n\n"
            yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.route("/reports")
def reports_page():
    files = sorted(REPORTS_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    reports = []
    for f in files:
        raw = f.read_text(encoding="utf-8")
        # First line is "# question"
        first_line = raw.splitlines()[0].lstrip("# ").strip() if raw.splitlines() else f.stem
        # Extract date from filename prefix YYYY-MM-DD_HH-MM-SS
        try:
            date_str = "_".join(f.stem.split("_")[:2])
            date = datetime.strptime(date_str, "%Y-%m-%d_%H-%M-%S").strftime("%b %d, %Y %H:%M")
        except Exception:
            date = ""
        reports.append({"filename": f.name, "title": first_line, "date": date})
    return render_template("reports.html", reports=reports)


@app.route("/reports/<filename>")
def report_view(filename):
    # Sanitise — only allow safe filenames
    if not re.match(r'^[\w\-. ]+\.md$', filename):
        return "Not found", 404
    path = REPORTS_DIR / filename
    if not path.exists():
        return "Not found", 404
    if request.args.get("dl"):
        return send_file(path, as_attachment=True, download_name=filename, mimetype="text/markdown")
    content_html = render_md(path)
    raw = path.read_text(encoding="utf-8")
    title = raw.splitlines()[0].lstrip("# ").strip() if raw.splitlines() else filename
    return render_template("report.html", title=title, content=content_html, filename=filename)


@app.route("/api/save-report", methods=["POST"])
def api_save_report():
    payload  = request.get_json(silent=True) or {}
    question = payload.get("question", "").strip()
    answer   = payload.get("answer", "").strip()
    if not question or not answer:
        return jsonify({"error": "Missing question or answer"}), 400

    slug = re.sub(r'[^a-z0-9]+', '-', question.lower())[:60].strip('-')
    ts   = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{ts}_{slug}.md"
    path = REPORTS_DIR / filename

    content = f"# {question}\n\n*Generated {datetime.now().strftime('%B %d, %Y at %H:%M')}*\n\n---\n\n{answer}\n"
    path.write_text(content, encoding="utf-8")
    return jsonify({"filename": filename})


@app.route("/export/pptx")
def export_pptx():
    from generate_pptx import build_pptx
    try:
        data = build_dashboard_data()
        path = build_pptx(data)
        filename = f"ledger-strategy-{datetime.now().strftime('%Y-%m-%d')}.pptx"
        return send_file(
            path,
            as_attachment=True,
            download_name=filename,
            mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )
    except Exception as exc:
        return f"Error generating deck: {exc}", 500


@app.route("/hunches")
def hunches_page():
    hunches = _load_hunches()
    okr_labels = [t["label"] for t in _parse_okr_targets()]
    return render_template(
        "hunches.html",
        hunches=hunches,
        product_areas=PRODUCT_AREAS,
        okr_labels=okr_labels,
    )


@app.route("/api/hunches", methods=["POST"])
def api_create_hunch():
    payload = request.get_json(silent=True) or {}
    body = payload.get("body", "").strip()
    if not body:
        return jsonify({"error": "Body is required"}), 400
    confidence = payload.get("confidence", "medium")
    if confidence not in ("low", "medium", "high"):
        confidence = "medium"
    hunch = {
        "id": str(uuid.uuid4()),
        "body": body,
        "productArea": payload.get("productArea", ""),
        "okrLink": payload.get("okrLink", ""),
        "confidence": confidence,
        "createdAt": datetime.now().isoformat(),
        "promotedToHypothesis": False,
    }
    hunches = _load_hunches()
    hunches.insert(0, hunch)
    _save_hunches(hunches)
    return jsonify(hunch), 201


@app.route("/api/hunches/<hunch_id>", methods=["PATCH"])
def api_update_hunch(hunch_id):
    payload = request.get_json(silent=True) or {}
    hunches = _load_hunches()
    for h in hunches:
        if h["id"] == hunch_id:
            if payload.get("promotedToHypothesis") is True and not h["promotedToHypothesis"]:
                h["promotedToHypothesis"] = True
                hypotheses = _load_hypotheses()
                hypotheses.append({
                    "id": str(uuid.uuid4()),
                    "hunchId": h["id"],
                    "body": h["body"],
                    "productArea": h["productArea"],
                    "okrLink": h["okrLink"],
                    "confidence": h["confidence"],
                    "promotedAt": datetime.now().isoformat(),
                    "status": "hypothesis",
                })
                _save_hypotheses(hypotheses)
            _save_hunches(hunches)
            return jsonify(h)
    return jsonify({"error": "Not found"}), 404


@app.route("/api/hunches/<hunch_id>", methods=["DELETE"])
def api_delete_hunch(hunch_id):
    hunches = _load_hunches()
    hunches = [h for h in hunches if h["id"] != hunch_id]
    _save_hunches(hunches)
    return jsonify({"ok": True})


if __name__ == "__main__":
    print("\n  Product Brain running → http://localhost:8080\n")
    app.run(debug=True, port=8080)
