import requests

response = requests.get('https://raider.io/')

contentresponse = response.content
content = response.text
status_code = response.status_code
headers = response.headers