"""Mirror BackPR's open data from backpr.com into this repository.

Downloads https://backpr.com/data/datapackage.json and every file it lists into data/, then rewrites the
"Datasets" section of README.md from the package, so the README always matches the files.

Prints what changed and, when run in GitHub Actions, writes two outputs:
  changed=true|false         any file in data/ changed
  release=true|false         a dataset's CSV changed (other than the live directory statistics), so the
                             copies on Hugging Face, Kaggle and Zenodo should get a new version

Usage: python3 scripts/sync.py
"""

import hashlib
import json
import os
import urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA = os.path.join(ROOT, "data")
README = os.path.join(ROOT, "README.md")
PACKAGE_URL = "https://backpr.com/data/datapackage.json"
LIVE = "finder-directory-stats"  # refreshed daily on backpr.com; a change here alone isn't a new release
START, END = "<!-- datasets:start -->", "<!-- datasets:end -->"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "backpr-open-data-sync/1.0 (+https://github.com/BackPR/backpr-open-data)"})
    with urllib.request.urlopen(req, timeout=60) as res:
        return res.read()


def digest(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest() if os.path.exists(path) else None


def save(name, body):
    """Write a file; return True if its content changed."""
    path = os.path.join(DATA, name)
    if name.endswith(".json"):
        # Stable formatting keeps diffs readable.
        body = (json.dumps(json.loads(body), indent=1, ensure_ascii=False) + "\n").encode("utf-8")
    before = digest(path)
    open(path, "wb").write(body)
    return digest(path) != before


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]


def readable(date):
    """2026-10 -> October 2026; 2026-09-08 -> September 8, 2026."""
    parts = date.split("-")
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        return f"{MONTHS[int(parts[1]) - 1]} {parts[0]}"
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        return f"{MONTHS[int(parts[1]) - 1]} {int(parts[2])}, {parts[0]}"
    return date


def datasets_markdown(pkg):
    lines, seen = [], set()
    for r in pkg["resources"]:
        base = r["name"].rsplit("-", 1)[0]
        if base in seen:
            continue
        seen.add(base)
        if base == LIVE:
            status = "Version: live · Updated daily on backpr.com and weekly here"
            with open(os.path.join(DATA, f"{base}.csv"), encoding="utf-8") as fh:
                states = sum(1 for _ in fh) - 1
            records = f"one record per state with listings: {states} states"
        else:
            status = f"Version {r['version']} · Last checked {readable(r['last_checked'])}"
            records = f"{r.get('records')} records"
        lines += [f"### {r['title']}", "", r["description"], ""]
        lines.append(f"- Files: [`data/{base}.csv`](data/{base}.csv), [`data/{base}.json`](data/{base}.json) ({records})")
        lines.append(f"- {status}")
        if r.get("sources"):
            lines.append("- Sources: " + "; ".join(src["title"] for src in r["sources"]))
        if r.get("notes"):
            lines.append(f"- Notes: {r['notes']}")
        lines.append(f"- Live copy: {r['path']} · Page on backpr.com: {r['page']}")
        lines.append(f"- Cite as: {r['cite_as']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    os.makedirs(DATA, exist_ok=True)
    raw = fetch(PACKAGE_URL)
    pkg = json.loads(raw)
    changed = []
    if save("datapackage.json", raw):
        changed.append("datapackage.json")
    for r in pkg["resources"]:
        name = r["path"].rsplit("/", 1)[1]
        if save(name, fetch(r["path"])):
            changed.append(name)

    readme = open(README, encoding="utf-8").read()
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    new_readme = f"{head}{START}\n{datasets_markdown(pkg)}{END}{tail}"
    if new_readme != readme:
        open(README, "w", encoding="utf-8").write(new_readme)
        changed.append("README.md")

    # A new release only when a dataset's CSV changes (the data itself). The JSON files also carry the
    # descriptions, so a wording change alone isn't a release; the live statistics change daily.
    release = any(c.endswith(".csv") and not c.startswith(LIVE) for c in changed)
    print("Changed:", ", ".join(changed) if changed else "nothing")
    print("New release:", "yes" if release else "no")
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as fh:
            fh.write(f"changed={'true' if changed else 'false'}\nrelease={'true' if release else 'false'}\n")


if __name__ == "__main__":
    main()
