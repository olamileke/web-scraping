# python program to scrape the contents of a washington post article

from bs4 import BeautifulSoup, Tag
from urllib.request import Request, urlopen
import re

url = input('enter the url of the w.post article - ')

def parse_text(soup):
    article_title = soup.h1.string
    article_picture = soup.img.attrs.get('src')
    article_body = soup.find(class_='article-body')

    if article_body is None:
        article_body = soup.find(class_='story relative')

    article_blocks = article_body.find_all(class_='font--body')
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

    # removing the Read More extra tabs at the end
    read_start_index = article_text.find('Read more')
    if read_start_index != -1:
        article_text = article_text[:read_start_index]

    print('{0}\n{1}\n\n{2}'.format(article_title, article_picture, article_text))

# a bit of validation to ensure the user entered a valid w. post article url
if re.match('https://(www.)*washingtonpost.com/.+', url) is None:
    print('enter a valid w.post article')

elif re.match('https://(www.)*washingtonpost.com/video(.*)', url) is not None:
    print('sorry. I do not scrape washington post video links')

elif re.match('https://(www.)*washingtonpost.com/travel(.*)', url) is not None:
    print('sorry. I do not scrape washington post travel links')

else:
    req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
    html = urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    parse_text(soup)