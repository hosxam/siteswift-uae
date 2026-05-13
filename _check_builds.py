"""
Check GitHub Pages build status for the repo.
Usage: python _check_builds.py
Requires GITHUB_TOKEN env var or no arg for public info.
"""
import os, json, urllib.request

token = os.getenv("GITHUB_TOKEN", "")
headers = {
    "Accept": "application/vnd.github.v3+json",
}
if token:
    headers["Authorization"] = f"Bearer {token}"

repo = "hosxam/siteswift-uae"

req = urllib.request.Request(
    f"https://api.github.com/repos/{repo}/pages/builds?per_page=5",
    headers=headers,
)
resp = urllib.request.urlopen(req)
builds = json.loads(resp.read())
for i, b in enumerate(builds):
    err = b.get("error", {}).get("message", "none")
    print(f"Build #{i}: status={b['status']} commit={str(b['commit'])[:8]} created={b['created_at']} error={err}")
