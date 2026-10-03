#!/usr/bin/env python3
"""Moodle'dan tum ders materyallerini indir."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sync.moodle_client import COURSES, get_course_contents, download_file

ROOT = Path(__file__).resolve().parent.parent / "courses"


def _safe_filename(section_idx, filename, used_names):
    """Ayni isimli dosyalari section indexi ile ayir."""
    if filename not in used_names:
        used_names.add(filename)
        return filename
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    new_name = f"{stem}_s{section_idx}{suffix}"
    used_names.add(new_name)
    return new_name


def sync_course(course_id, folder_name):
    dest = ROOT / folder_name / "materials"
    dest.mkdir(parents=True, exist_ok=True)

    sections = get_course_contents(course_id)
    new_files = 0
    skipped = 0
    used_names = set()

    for section_idx, section in enumerate(sections):
        section_name = section.get("name", "").strip()
        if not section_name:
            continue

        for module in section.get("modules", []):
            for content in module.get("contents", []):
                if content.get("type") != "file":
                    continue

                filename = _safe_filename(section_idx, content["filename"], used_names)
                file_path = dest / filename

                if file_path.exists():
                    skipped += 1
                    continue

                print(f"  [{folder_name}] {filename}")
                try:
                    download_file(content["fileurl"], file_path)
                    new_files += 1
                except Exception as e:
                    print(f"    HATA: {e}")

    return new_files, skipped


def main():
    print("Moodle sync basliyor...\n")
    total_new = 0
    total_skipped = 0

    for course_id, folder in COURSES.items():
        print(f"--- {folder} (ID: {course_id}) ---")
        new, skipped = sync_course(course_id, folder)
        total_new += new
        total_skipped += skipped
        print(f"  Yeni: {new}, Mevcut: {skipped}\n")

    print(f"Tamamlandi. {total_new} yeni dosya indirildi, {total_skipped} dosya zaten mevcuttu.")


if __name__ == "__main__":
    main()
