from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

#include json library
import json

baseURL = "https://www.instagram.com/web/search/topsearch/?query="

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen(baseURL + 'ucsc').read()
#print(html)

object = json.loads(html)
print(object)
keys = object.keys()
print(keys)

print('a user')
print(object['users'][1]['user']['username'])