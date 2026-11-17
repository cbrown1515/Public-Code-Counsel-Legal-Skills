#!/usr/bin/env python3
"""Package a skill as a .zip you can upload to Claude or import into AppletHub.

The zip holds one folder named after the skill, with SKILL.md, references/ and assets/.
README.md and evals/ stay out: they are for people and testers, not for the model.

Usage: python3 tools/package_skill.py <skill-dir> [--out dist]
"""
import argparse
import sys
import zipfile
from pathlib import Path

INCLUDE = ('SKILL.md', 'references', 'assets')


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('skill')
    ap.add_argument('--out', default='dist')
    args = ap.parse_args()
    skill = Path(args.skill).resolve()
    if not (skill / 'SKILL.md').exists():
        sys.exit(f'{skill} has no SKILL.md')
    files = [skill / 'SKILL.md']
    for sub in INCLUDE[1:]:
        if (skill / sub).exists():
            files += sorted(f for f in (skill / sub).rglob('*') if f.is_file() and not f.name.startswith('.'))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    target = out / f'{skill.name}.zip'
    words = 0
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, f'{skill.name}/{f.relative_to(skill).as_posix()}')
            words += len(f.read_text(encoding='utf-8', errors='ignore').split())
    print(f'{target}: {len(files)} files, about {words / 500:.0f} pages')
    for f in files:
        print('  ' + f.relative_to(skill).as_posix())


if __name__ == '__main__':
    main()
