from bs4 import BeautifulSoup

html_content = '<html><head><title>Example</title</head><body><p>This is a sample HTML document.</p</body></html>'
soup = BeautifulSoup(html_content, 'html.parser')

p_tag = soup.find('p')
p_text = p_tag.text
print(p_text)

a_tag = soup.find('a')
href_value = a_tag['href']
print(href_value)
