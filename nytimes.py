# Python program to fetch the contents of an nytimes article

from bs4 import BeautifulSoup, Tag
from urllib.request import Request, urlopen
import re

url = input('enter the url for the nytimes articles - ')

# formatting the text in the format we want
def parse_text(soup):
    article_title = soup.h1.string
    article_summary = soup.find(id='article-summary').string
    article_blocks_parent = soup.find('section', class_='meteredContent')
    blocks = article_blocks_parent.find_all('div', class_='StoryBodyCompanionColumn')
    article_text = ''

    for block in blocks:
        paragraphs = block.find_all('p')
        block_text = ''

        for p in paragraphs:
            p_text = ''
            for child in p.children:
                if(isinstance(child, Tag)):
                    p_text = p_text + child.string
                else:
                    p_text = p_text + child

            block_text = block_text + p_text
        
        article_text = article_text + block_text

    print('{0}\n{1}\n\n{2}'.format(article_title, article_summary, article_text))

# validating if the user entered a valid link to nytimes.com
if re.match('https://nytimes.com/.+', url) is None:
    print('please enter a valid nytimes article')
else:
    try:
        req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
        html = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        parse_text(soup)
    except:
        print('There was a problem scraping the data')

