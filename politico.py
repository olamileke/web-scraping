# Python script to fetch the contents of a politico article

from bs4 import BeautifulSoup, Tag
from urllib.request import Request, urlopen
import re

url = input('enter the politico url that you want to scrape - ')

def parse_text(soup):
    article_title_tag = soup.find(class_='headline')

    if article_title_tag is None:
        parse_text_states(soup)
        return
    
    article_title = article_title_tag.string
    article_summary = soup.find(class_='dek')
    article_picture_tag = soup.picture
    article_picture = ''
    article_paragraphs = soup.find_all(class_='story-text__paragraph') 
    article_text = ''

    if article_picture_tag is not None:
        article_picture = article_picture_tag.img['src']

    if article_summary is None:
        article_summary = ''
    else:
        article_summary = article_summary.string

    for p in article_paragraphs:
        p_text = ''
        for child in p.children:
            if(isinstance(child, Tag)):
                if child.string:
                    p_text = p_text + child.string
            else:
                p_text = p_text + child

        article_text = article_text + p_text

    print('{0}\n{1}\n{2}\n\n{3}'.format(article_title, article_summary, article_picture, article_text))

# parsing the unique urls for politico state artices
def parse_text_states(soup):
    article_picture_tag = soup.picture
    article_picture = ''

    if article_picture_tag is not None:
        article_picture = article_picture_tag.img['src']

    story_text = soup.find(class_='story-text')
    article_title = story_text.h1.span.string
    article_paragraphs = story_text.find_all('p', class_=validate_state_paragraphs)[1:]
    article_text = ''

    for p in article_paragraphs:
        p_text = ''
        for child in p.children:
            if(isinstance(child, Tag)):
                if child.string:
                    p_text = p_text + child.string
            else:
                p_text = p_text + child

        article_text = article_text + p_text

    print('{0}\n{1}\n\n{2}'.format(article_title, article_picture, article_text))

# filter to remove the byline, timestamp and updated paragraphs from the block text
# when accessing a politico states article
def validate_state_paragraphs(class_name):
    excluded_classes = ['byline', 'timestamp', 'updated']
    if class_name in excluded_classes:
        return False
    return True


# validation performed to ensure the user entered the correct url
if re.match('https://(www.)*politico.com/.+', url) is None:
    print('please enter a valid link to a politico article')

elif re.match('https://(www.)*politico.com/video(.*)', url) is not None:
    print('sorry. I do not scrape politico video links')

elif re.match('https://(www.)*politico.com/newsletters(.*)', url) is not None:
    print('sorry. I do not scrape politico newsletter links')

else:
    try:
        req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
        html = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        parse_text(soup)
    except:
        print('there was a problem scraping the data')
