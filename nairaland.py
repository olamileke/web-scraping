# Python script to get all the links on the nairaland front page

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, Tag
import re

url = 'https://nairaland.com'
req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})

# downloading the page's content
response = urlopen(req)
data = response.read()
html = data.decode('utf-8')

# creating the beautiful soup object
soup = BeautifulSoup(html, 'html.parser')

# fetching the table containing all the links
table = soup.find_all('table', class_='boards')[1]

# custom function to filter the links
def not_navigation_link(href):
    if re.match('/news/', href) is None:
        return True
    
    return False

# obtaining the particular table data column containing the links
links = table.find_all('td', limit=2)[1].find_all('a', href=not_navigation_link)

# a bit of parsing to get the links in the exact format we want
for link in links:
    text = ''

    for child in link.children:
        if(isinstance(child, Tag)):
            text = text + child.string
        else:
            text = text + child

    print('{0} - {1}'.format(text, link['href']))

