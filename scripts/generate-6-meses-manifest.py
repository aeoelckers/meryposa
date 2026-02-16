#!/usr/bin/env python3
"""Genera media/6-meses/manifest.json a partir de los archivos de media/6-meses/."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEDIA_DIR = ROOT / "media" / "6-meses"
MANIFEST_PATH = MEDIA_DIR / "manifest.json"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
VIDEO_EXTS = {".mp4", ".webm", ".mov"}


def is_hidden(path: Path) -> bool:
    return any(part.startswith('.') for part in path.parts)


def main() -> None:
    if not MEDIA_DIR.exists():
        raise SystemExit(f"No existe carpeta: {MEDIA_DIR}")

    files = sorted(
        p for p in MEDIA_DIR.iterdir()
        if p.is_file() and not is_hidden(p) and p.name.lower() not in {"readme.md", "manifest.json"}
    )

    image_files = [p for p in files if p.suffix.lower() in IMAGE_EXTS]
    video_files = [p for p in files if p.suffix.lower() in VIDEO_EXTS]

    manifest = {
        "images": [f"../media/6-meses/{p.name}" for p in image_files],
        "video": f"../media/6-meses/{video_files[0].name}" if video_files else "../media/6-meses/video01.mp4",
    }

    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Manifest generado: {MANIFEST_PATH}")
    print(f"- Imágenes: {len(image_files)}")
    print(f"- Video: {manifest['video']}")


if __name__ == "__main__":
    main()
