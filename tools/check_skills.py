#!/usr/bin/env python3
"""Check every skill in this repo before it ships.

Runs the Agent Skills spec checks (with the `skills-ref` validator when it is installed:
`pip install skills-ref`) and this repo's own rules:

- frontmatter carries a license and metadata.version and metadata.updated;
- every references/ or assets/ file SKILL.md names exists, and every such file is named;
- README.md and evals/evals.json exist, and every eval file is marked fictional;
- quotes in an answer key's table rows appear word for word in the eval's source file;
- files shared between skills are identical;
- the files a hosted runner loads fit in about 40 pages (a page is about 500 words).

Usage: python3 tools/check_skills.py [skill-dir ...]   (default: every skill in the repo)
Exit code 1 if any check fails. Size overruns are warnings.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'docs', 'tools', 'dist', '.git'}
SHARED = [
    ('nda-playbook-builder/references/nda-clause-types.md', 'nda-review/references/nda-clause-types.md'),
    ('nda-playbook-builder/assets/example-playbook.md', 'nda-review/references/nda-playbook.md'),
]
WORDS_PER_PAGE = 500
PAGE_BUDGET = 40
NAME_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
ALLOWED_FIELDS = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}


def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None
    try:
        import yaml
        return yaml.safe_load(m.group(1)) or {}
    except ImportError:
        data = {}
        for line in m.group(1).splitlines():
            if re.match(r'^[a-z-]+:', line):
                key, _, val = line.partition(':')
                data[key.strip()] = val.strip() or {}
        return data


def spec_errors(skill):
    try:
        from skills_ref.validator import validate
        return list(validate(skill))
    except ImportError:
        pass
    text = (skill / 'SKILL.md').read_text(encoding='utf-8')
    fm = frontmatter(text)
    if fm is None:
        return ['SKILL.md has no YAML frontmatter']
    errs = []
    extra = set(fm) - ALLOWED_FIELDS
    if extra:
        errs.append(f'unexpected frontmatter fields: {sorted(extra)}')
    name = str(fm.get('name', ''))
    if not NAME_RE.match(name) or len(name) > 64:
        errs.append(f'bad name: {name!r}')
    if name != skill.name:
        errs.append(f'name {name!r} does not match folder {skill.name!r}')
    desc = fm.get('description') or ''
    if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
        errs.append('description must be 1 to 1024 characters')
    return errs


def house_errors(skill, warnings):
    errs = []
    text = (skill / 'SKILL.md').read_text(encoding='utf-8')
    fm = frontmatter(text) or {}
    meta = fm.get('metadata') if isinstance(fm.get('metadata'), dict) else {}
    if not fm.get('license'):
        errs.append('frontmatter has no license')
    for key in ('version', 'updated'):
        if not meta.get(key):
            errs.append(f'frontmatter metadata has no {key}')
    if len(text.splitlines()) > 500:
        errs.append('SKILL.md is over 500 lines')

    named = set(re.findall(r'`((?:references|assets)/[^`\s]+)`', text))
    for path in sorted(named):
        if not (skill / path).exists():
            errs.append(f'SKILL.md names {path}, which does not exist')
    words = len(re.sub(r'^---\n.*?\n---\n', '', text, flags=re.S).split())
    for sub in ('references', 'assets'):
        for f in sorted((skill / sub).rglob('*')) if (skill / sub).exists() else []:
            if f.is_file() and not f.name.startswith('.'):
                rel = f.relative_to(skill).as_posix()
                if rel not in named:
                    errs.append(f'{rel} is never named in SKILL.md')
                words += len(f.read_text(encoding='utf-8', errors='ignore').split())
    pages = words / WORDS_PER_PAGE
    if pages > PAGE_BUDGET:
        warnings.append(f'{skill.name}: about {pages:.0f} pages loaded per run (budget {PAGE_BUDGET}); '
                        'hosted runners with page limits may need fewer reference files')

    if not (skill / 'README.md').exists():
        errs.append('no README.md')
    evals_file = skill / 'evals' / 'evals.json'
    if not evals_file.exists():
        return errs + ['no evals/evals.json']
    try:
        evals = json.loads(evals_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        return errs + [f'evals.json does not parse: {e}']
    if evals.get('skill_name') != skill.name:
        errs.append('evals.json skill_name does not match the folder')
    if evals.get('data_origin') != 'synthetic':
        errs.append('evals.json must declare data_origin: synthetic')
    if not evals.get('evals'):
        errs.append('evals.json has no cases')
    for f in sorted((skill / 'evals').glob('*')):
        if f.is_file() and f.suffix != '.json':
            head = '\n'.join(f.read_text(encoding='utf-8').splitlines()[:6])
            if 'Fictional' not in head:
                errs.append(f'evals/{f.name} is not marked Fictional in its first lines')
    for case in evals.get('evals', []):
        paths = list(case.get('files', [])) + ([case['answer_key']] if case.get('answer_key') else [])
        for p in paths:
            if not (skill / p).exists():
                errs.append(f'eval {case.get("id")} names {p}, which does not exist')
        if case.get('answer_key') and len(case.get('files', [])) == 1:
            source = (skill / case['files'][0]).read_text(encoding='utf-8')
            key = (skill / case['answer_key']).read_text(encoding='utf-8')
            for line in key.splitlines():
                if line.startswith('|'):
                    for q in re.findall(r'"([^"]{12,})"', line):
                        if q not in source:
                            errs.append(f'answer key quote not in source: {q[:60]!r}')
    return errs


def main(argv):
    skills = [ROOT / a for a in argv] if argv else sorted(
        d for d in ROOT.iterdir() if d.is_dir() and d.name not in SKIP_DIRS and (d / 'SKILL.md').exists())
    failed = False
    warnings = []
    for skill in skills:
        errs = spec_errors(skill) + house_errors(skill, warnings)
        print(f'{"FAIL" if errs else "ok  "} {skill.name}')
        for e in errs:
            print(f'     - {e}')
        failed |= bool(errs)
    for a, b in SHARED:
        pa, pb = ROOT / a, ROOT / b
        if pa.exists() and pb.exists() and pa.read_bytes() != pb.read_bytes():
            print(f'FAIL shared file differs: {a} and {b}')
            failed = True
    for w in warnings:
        print(f'warn {w}')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
