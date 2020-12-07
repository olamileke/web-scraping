# python program to scrape the contentes of a the economist url

from bs4 import BeautifulSoup, Tag
from urllib.request import Request, urlopen
import re

url = input('enter the url of the economist article - ')

# function to parse the html and put it in the format that we want
def parse_text(soup):
    article_title = soup.find(class_='article__headline').string
    article_summary = soup.find(class_='article__description').string
    article_picture = soup.img['src']
    article_blocks = soup.find_all(class_='article__body-text')
    article_text = ''

    for block in article_blocks:
        text = ''

        for child in block.children:
            if isinstance(child, Tag):
                if child.string:
                    text = text + child.string
            else:
                text = text + child

        article_text = article_text + text

    print('{0}\n{1}\n{2}\n\n{3}'.format(article_title, article_summary, article_picture, article_text))

# a bit of validation to make sure that a correct economist url was entered
if re.match('https://(www.)*economist.com/.+', url) is None:
    print('please enter a valid economist article url')

elif re.match('https://(www.)*economist.com/weeklyedition(.*)', url) is not None:
    print('I am sorry. I cannot scrape this.')

else: 
    try:
        req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
        html = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        parse_text(soup)
    except:
        print('There was a problem scraping the data')
