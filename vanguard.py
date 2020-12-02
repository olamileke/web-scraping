# Python program to scrape the latest news from the vanguard nigeria site

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_alerts(soup):
    links_container = soup.find(id='vanguard_latest_news-2')
    links_parents = links_container.find_all('div')

    for parent in links_parents:
        time = parent.find(class_='post-date').string
        link = parent.find('a')
        title = link.string
        url = link['href']

        print('{0}\n{1}\n{2}\n'.format(title, url, time))

try:
    url = 'https://vanguardngr.com'
    req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
    html = urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    get_alerts(soup)
except:
    print('there was a problem accessing the url')


