import request

response = request.get('https://raider.io/mythic-plus-rankings/season-df-2/all/world/leaderboards')

contentresponse = response.content
content = response.text
status_code = response.status_code
headers = response.headers

print(response)