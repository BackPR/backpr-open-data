"""Publish the files in data/ as a new version of the BackPR open data record on Zenodo.

Every version keeps the same concept DOI (10.5281/zenodo.23577823, which always resolves to the newest version)
and gets its own version DOI. The new version copies the previous version's metadata and replaces its files
with data/* and CITATION.cff; only the version label and publication date change.

Needs ZENODO_TOKEN: a Zenodo personal access token with the deposit:write and deposit:actions scopes.
Usage: ZENODO_TOKEN=... python3 scripts/zenodo_new_version.py
"""

import datetime as dt
import glob
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://zenodo.org/api"
CONCEPT_RECORD = "23577823"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def call(method, url, token, body=None, data=None, content_type="application/json"):
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode()
    if data is not None:
        headers["Content-Type"] = content_type
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=120) as res:
            raw = res.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"Zenodo {method} {url} failed: HTTP {e.code} {e.read().decode(errors='replace')[:500]}")


def main():
    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        sys.exit("ZENODO_TOKEN is not set")
    files = sorted(glob.glob(os.path.join(ROOT, "data", "*"))) + [os.path.join(ROOT, "CITATION.cff")]

    # The newest published version of the record.
    latest = call("GET", f"{API}/records/{CONCEPT_RECORD}/versions/latest", token)
    latest_id = latest["id"]

    # Start a new version (Zenodo returns the existing draft if one is already open).
    started = call("POST", f"{API}/deposit/depositions/{latest_id}/actions/newversion", token)
    draft = call("GET", started["links"]["latest_draft"], token)
    draft_id, bucket = draft["id"], draft["links"]["bucket"]

    # Replace the files carried over from the previous version.
    for f in draft.get("files", []):
        call("DELETE", f"{API}/deposit/depositions/{draft_id}/files/{f['id']}", token)
    for path in files:
        name = os.path.basename(path)
        call("PUT", f"{bucket}/{name}", token, data=open(path, "rb").read(), content_type="application/octet-stream")

    today = dt.date.today().isoformat()
    metadata = draft["metadata"]
    metadata.pop("doi", None)  # the draft's reserved DOI is kept by Zenodo
    metadata["version"] = today
    metadata["publication_date"] = today
    call("PUT", f"{API}/deposit/depositions/{draft_id}", token, body={"metadata": metadata})

    published = call("POST", f"{API}/deposit/depositions/{draft_id}/actions/publish", token)
    print(f"Published Zenodo version {today}: https://doi.org/{published.get('doi')} (all versions: https://doi.org/10.5281/zenodo.{CONCEPT_RECORD})")


if __name__ == "__main__":
    main()
