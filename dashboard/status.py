#!/usr/bin/env python3
"""Ders durumu ozeti — materyaller, mesajlar, odevler."""

import re
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sync.moodle_client import COURSES, get_course_contents, get_messages

ROOT = Path(__file__).resolve().parent.parent / "courses"

COURSE_ID_TO_FOLDER = {v: k for k, v in COURSES.items()}


def course_status(course_id, folder_name):
    materials_dir = ROOT / folder_name / "materials"
    notes_dir = ROOT / folder_name / "notes"
    exams_dir = ROOT / folder_name / "exams"

    local_files = len([f for f in materials_dir.glob("*") if f.name != ".gitkeep"])
    note_files = len([f for f in notes_dir.glob("*") if f.name != ".gitkeep"])
    exam_files = len([f for f in exams_dir.glob("*") if f.name != ".gitkeep"])

    sections = get_course_contents(course_id)

    remote_files = 0
    assignments = []
    for section in sections:
        for module in section.get("modules", []):
            for content in module.get("contents", []):
                if content.get("type") == "file":
                    remote_files += 1

            if module.get("modname") in ("assign", "quiz"):
                due = module.get("dates", [])
                due_str = ""
                for d in due:
                    if d.get("label") == "Due:":
                        due_str = datetime.fromtimestamp(d["timestamp"]).strftime("%d/%m/%Y %H:%M")
                assignments.append({
                    "name": module["name"],
                    "type": module["modname"],
                    "due": due_str,
                })

    return {
        "local_materials": local_files,
        "remote_materials": remote_files,
        "notes": note_files,
        "exams": exam_files,
        "assignments": assignments,
    }


def show_messages():
    print("--- Son Mesajlar (okunmamis) ---")
    messages = get_messages(unread_only=True, limit=15)
    if not messages:
        print("  Okunmamis mesaj yok.\n")
        return

    for m in messages:
        ts = datetime.fromtimestamp(m["timecreated"]).strftime("%d/%m %H:%M")
        subject = m.get("subject", "")[:70]
        text = re.sub(r"<[^>]+>", "", m.get("smallmessage", m.get("text", "")))[:100]
        print(f"  {ts} | {subject}")
        if text and text != subject:
            print(f"         {text}")
    print()


def main():
    print(f"=== BOUN Dashboard — {datetime.now().strftime('%d/%m/%Y %H:%M')} ===\n")

    show_messages()

    print("--- Dersler ---")
    for course_id, folder in COURSES.items():
        info = course_status(course_id, folder)

        sync_icon = "v" if info["local_materials"] >= info["remote_materials"] else "!"
        print(f"[{sync_icon}] {folder}")
        print(f"    Materyaller: {info['local_materials']}/{info['remote_materials']} indirildi")
        if info["notes"]:
            print(f"    Notlar: {info['notes']} dosya")
        if info["exams"]:
            print(f"    Cikmislar: {info['exams']} dosya")

        if info["assignments"]:
            print("    Odevler:")
            for a in info["assignments"]:
                due = f" (son: {a['due']})" if a["due"] else ""
                print(f"      - {a['name']}{due}")
        print()


if __name__ == "__main__":
    main()
