import urllib.request, json
req = urllib.request.urlopen('https://api.github.com/users/hosxam/repos?per_page=50')
data = json.loads(req.read())
for r in data:
    print(r['name'], 'private=' + str(r['private']), 'pushed=' + r['pushed_at'][:10], 'pages=' + str(r['has_pages']), 'clone=' + r['clone_url'])
