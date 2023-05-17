import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://raider.io/')
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find_all(class_='product_pod')
content = str(content)

number = r'\d{3}-\d{3}-\d{4}'
