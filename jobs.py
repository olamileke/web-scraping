# Python program to fetch all the top developer job listings on hotnigerianjobs.com

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

# fetching the page and creating the beautiful soup object with it
url = 'https://www.hotnigerianjobs.com/index.php?qid=Developer'
req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

# fetching all the job tag objects
jobs = soup.find_all(class_='mycase')


# formatting the job information to get it in the correct format
for job in jobs:
    link = job.find('a')
    if link is not None:
        role = link.string
        url = link['href']
        description = job.find(class_='mycase4').contents[0]
        description = description.strip()

        print('{0}\n{1}\n{2}\n'.format(role, description, url))