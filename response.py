import requests
import json

response = requests.get('https://raider.io/mythic-plus-rankings/season-df-2/all/world/leaderboards')


contentresponse = response.content
content = response.text
status_code = response.status_code
headers = response.headers
f = open("mplus.txt","a")
open("mplus.txt", 'w')
f.write(content)
f.close()

print(headers)
