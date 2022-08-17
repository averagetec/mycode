#!/usr/bin/python3

import urllib.request
import json

URL = "https://statsapi.web.nhl.com/api/v1/teams"

resp = urllib.request.urlopen(URL)
content = resp.read()
final = json.loads(content.decode("utf-8"))

print(final["teams"][0]["name"])
print(type(final))

