# Python program to fetch all the top developer job listings on hotnigerianjobs.com

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# fetching the page and creating the beautiful soup object with it
url = 'https://www.hotnigerianjobs.com/index.php?qid=Developer'
req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

jobs = soup.find_all(class_='mycase')

for job in jobs:
    link = job.find('a')
    print(type(link))
