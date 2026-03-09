# AGENTS.md — jenr8ed.github.io

## About This Repository
Personal portfolio and project showcase for Jennifer McKinley (@JenR8ed).
QA Engineer & Python Developer. Hosted on GitHub Pages.

**Live site:** https://jenr8ed.github.io

## Stack
- Python (scripts and automation)
- HTML/CSS (static pages)
- GitHub Pages (hosting)

## Environment Setup
```bash
# Python scripts
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt  # if requirements.txt exists

# Run Python files
python3 <filename>.py
```

## Key Files
- `README.md` — project overview
- `validate_report.py` — report validation script
- `test_validate_report.py` — unit tests for validate_report

## Jules Task Guidelines
- Always check for a `requirements.txt` before installing packages
- Run tests with `python3 -m pytest` before committing
- Keep Python code PEP 8 compliant
- Do not add frontend frameworks — this repo stays simple HTML/Python
- Target branch for Jules PRs: `main`

## Coding Conventions
- Python 3.x only
- Use docstrings for all functions
- Commit messages: imperative mood, e.g. "Add unit tests for validate_report"
- Keep scripts modular and testable

## Common Tasks for Jules
- Write or improve unit tests
- Fix Python linting issues
- Add docstrings to undocumented functions
- Resolve TODO comments in code
- Update README.md
