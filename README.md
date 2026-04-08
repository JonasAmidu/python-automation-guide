# Python Automation Guide

A collection of automation resources — prompts, templates, and a comprehensive Python e-book — designed to help developers streamline DevOps workflows and eliminate repetitive tasks.

## What's Included

### 1. `notion-automation-template/`
A Notion workspace template for planning and tracking automation projects. Includes sales page assets.

### 2. `chatgpt-prompts/`
Curated ChatGPT prompts for generating automation scripts, DevOps runbooks, and infrastructure code. Includes sales page assets.

### 3. `python-automation-guide/`
The core content — a Python automation e-book covering:

- **Scheduled tasks** — `cron` jobs, `schedule`, `APScheduler`
- **API interactions** — `requests`, authentication, rate limiting
- **File operations** — batch processing, CSV/PDF handling with `pandas`
- **Email automation** — sending reports, monitoring alerts
- **Operational efficiency** — scripting away repetitive DevOps tasks

Also includes an `upload.py` script for automated file uploads and an HTML sales page.

## How to Use

```bash
# Explore the e-book content
cat python-automation-guide/ebook.md

# Run the upload automation script
python python-automation-guide/upload.py

# Open the sales page
open python-automation-guide/sales-page.html
```

## Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3 |
| Scheduling | cron, schedule, APScheduler |
| HTTP | requests |
| Data | pandas, CSV |
| Automation | subprocess, os, shutil |
| Web | HTML, JavaScript (sales pages) |

## License

MIT License — [github.com/JonasAmidu](https://github.com/JonasAmidu)
