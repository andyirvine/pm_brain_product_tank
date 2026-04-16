# Gemini Project Mandates

This document defines the foundational standards and workflows for Gemini CLI within the "Product Brain Example" project. These instructions take precedence over general defaults.

## Project Overview
This is a Product Management (PM) tool designed to synthesize user interviews, market shifts, and competitive landscapes into actionable hypotheses and strategic reports. It uses a Flask-based web interface (`app.py`) and generates PowerPoint presentations (`generate_pptx.py`).

## Engineering Standards

### Python Environment
- Use `requirements.txt` for dependency management.
- Prefer `python3` for execution.
- Adhere to PEP 8 standards for all Python code.

### Data Structure & Integrity
- **JSON Files:** `hunches.json` and `hypotheses.json` are core data stores. Always validate schema before writing.
- **Markdown Docs:** Strategic insights are stored in `Company/`, `pm-brain/`, and `User Data/`. Maintain the existing directory hierarchy.
- **Reports:** New reports should be saved in the `Reports/` directory using the naming convention `YYYY-MM-DD_HH-MM-SS_slug.md`.

### UI & Templates
- The project uses Flask with Jinja2 templates located in `Templates/`.
- Styling is managed via `static/css/style.css`. Prefer modifying this file over inline styles.

## Workflows

### Report Generation
When asked to synthesize information:
1. Research relevant files in `User Data/`, `Company/`, and `pm-brain/`.
2. Generate the report in Markdown.
3. Save it to `Reports/` with the timestamped filename.

### Hypothesis Management
When updating hypotheses:
1. Read `hypotheses.json`.
2. Update the entries based on new evidence found in `User Data/` or `Company/`.
3. Ensure `hypothesis-evidence.md` files are updated to reflect the changes.
