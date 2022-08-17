#!/usr/bin/env python3

import requests

URL = "https://statsapi.web.nhl.com/api/v1/teams"

resp = requests.get(URL).json()

print(resp["teams"][0]["name"])
