#!/usr/bin/env python3
"""HTML dashboard olustur."""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sync.moodle_client import COURSES, get_course_contents, get_messages

ROOT = Path(__file__).resolve().parent.parent / "courses"
OUT = Path(__file__).resolve().parent / "index.html"

PRIORITY = {
    "ie440_nonlinear": {"label": "IE 440 — Nonlinear OR", "level": "zor", "order": 1},
    "ie450_stochastic": {"label": "IE 450 — Stochastic OR", "level": "zor", "order": 2},
    "ie201_programming": {"label": "IE 201 — Programming", "level": "zor", "order": 3},
    "ie423_quality": {"label": "IE 423 — Quality Eng.", "level": "orta", "order": 4},
    "ie341_economics": {"label": "IE 341 — Eng. Economics", "level": "kolay", "order": 5},
    "htr311_tarih": {"label": "HTR 311 — Tarih", "level": "kolay", "order": 6},
}


def gather_data():
    messages = get_messages(unread_only=True, limit=20)
    msg_html = ""
    for m in messages:
        ts = datetime.fromtimestamp(m["timecreated"]).strftime("%d/%m %H:%M")
        subject = m.get("subject", "")[:80]
        text = re.sub(r"<[^>]+>", "", m.get("smallmessage", ""))[:120]
        msg_html += f'<div class="msg"><span class="ts">{ts}</span> <strong>{subject}</strong><br><span class="detail">{text}</span></div>\n'

    courses_html = ""
    sorted_courses = sorted(COURSES.items(), key=lambda x: PRIORITY.get(x[1], {}).get("order", 99))

    for course_id, folder in sorted_courses:
        info = PRIORITY.get(folder, {})
        label = info.get("label", folder)
        level = info.get("level", "")

        materials_dir = ROOT / folder / "materials"
        notes_dir = ROOT / folder / "notes"
        exams_dir = ROOT / folder / "exams"

        local = len([f for f in materials_dir.glob("*") if f.name != ".gitkeep"])
        notes = len([f for f in notes_dir.glob("*") if f.name != ".gitkeep"])
        exams = len([f for f in exams_dir.glob("*") if f.name != ".gitkeep"])

        sections = get_course_contents(course_id)
        remote = sum(1 for s in sections for m in s.get("modules", []) for c in m.get("contents", []) if c.get("type") == "file")

        synced = local >= remote
        level_class = {"zor": "hard", "orta": "medium", "kolay": "easy"}.get(level, "")
        level_badge = {"zor": "ZOR", "orta": "ORTA", "kolay": "KOLAY"}.get(level, "")
        sync_badge = "Guncel" if synced else f"Eksik ({local}/{remote})"
        sync_class = "synced" if synced else "unsynced"

        courses_html += f'''<div class="course {level_class}">
  <div class="course-header">
    <h3>{label}</h3>
    <span class="badge {level_class}">{level_badge}</span>
  </div>
  <div class="stats">
    <div class="stat"><span class="num">{local}</span><span class="lbl">Materyal</span></div>
    <div class="stat"><span class="num">{notes}</span><span class="lbl">Not</span></div>
    <div class="stat"><span class="num">{exams}</span><span class="lbl">Cikmis</span></div>
  </div>
  <div class="sync {sync_class}">{sync_badge}</div>
</div>\n'''

    return msg_html, courses_html


def main():
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    msg_html, courses_html = gather_data()

    html = f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Boun Dashboard</title>
<style>
:root {{
  --bg: #0f1117;
  --card: #1a1d27;
  --border: #2a2d3a;
  --text: #e4e4e7;
  --muted: #71717a;
  --accent: #6366f1;
  --hard: #ef4444;
  --medium: #f59e0b;
  --easy: #22c55e;
  --synced: #22c55e;
  --unsynced: #ef4444;
}}
@media (prefers-color-scheme: light) {{
  :root:not([data-theme="dark"]) {{
    --bg: #f8f9fa;
    --card: #ffffff;
    --border: #e5e7eb;
    --text: #1f2937;
    --muted: #6b7280;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #0f1117;
  --card: #1a1d27;
  --border: #2a2d3a;
  --text: #e4e4e7;
  --muted: #71717a;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; padding: 16px; max-width: 900px; margin: 0 auto; }}
h1 {{ font-size: 1.5rem; margin-bottom: 4px; }}
.updated {{ color: var(--muted); font-size: 0.85rem; margin-bottom: 24px; }}
h2 {{ font-size: 1.1rem; margin-bottom: 12px; color: var(--muted); }}
.messages {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px; margin-bottom: 24px; max-height: 300px; overflow-y: auto; }}
.msg {{ padding: 8px 0; border-bottom: 1px solid var(--border); }}
.msg:last-child {{ border-bottom: none; }}
.msg .ts {{ color: var(--muted); font-size: 0.8rem; }}
.msg .detail {{ color: var(--muted); font-size: 0.85rem; }}
.courses {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }}
.course {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px; }}
.course.hard {{ border-left: 3px solid var(--hard); }}
.course.medium {{ border-left: 3px solid var(--medium); }}
.course.easy {{ border-left: 3px solid var(--easy); }}
.course-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
.course-header h3 {{ font-size: 0.95rem; }}
.badge {{ font-size: 0.7rem; padding: 2px 8px; border-radius: 99px; font-weight: 600; }}
.badge.hard {{ background: var(--hard); color: white; }}
.badge.medium {{ background: var(--medium); color: black; }}
.badge.easy {{ background: var(--easy); color: black; }}
.stats {{ display: flex; gap: 16px; margin-bottom: 8px; }}
.stat {{ text-align: center; }}
.stat .num {{ display: block; font-size: 1.2rem; font-weight: 700; }}
.stat .lbl {{ font-size: 0.75rem; color: var(--muted); }}
.sync {{ font-size: 0.8rem; padding: 4px 8px; border-radius: 6px; text-align: center; }}
.sync.synced {{ background: rgba(34,197,94,0.1); color: var(--synced); }}
.sync.unsynced {{ background: rgba(239,68,68,0.1); color: var(--unsynced); }}
</style>
</head>
<body>
<h1>Boun Dashboard</h1>
<div class="updated">Son guncelleme: {now}</div>

<h2>Okunmamis Mesajlar</h2>
<div class="messages">{msg_html}</div>

<h2>Dersler</h2>
<div class="courses">{courses_html}</div>
</body>
</html>'''

    OUT.write_text(html, encoding="utf-8")
    print(f"Dashboard olusturuldu: {OUT}")


if __name__ == "__main__":
    main()
