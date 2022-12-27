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

def searchQuery(username):
    html = urllib.request.urlopen(baseURL + username).read()
    #print(html)

    object = json.loads(html)
    #print(object)
    #keys = object.keys()
    #print(keys)

    print('List of Users')
    #print(object['users'][1]['user']['username'])
    i=0
    while True:
        try:
            print(object['users'][i]['user']['username'])
        except:
            break
        i+=1

searchQuery('ucsc')
searchQuery('ucscacm')
searchQuery('dscucsc')
searchQuery('baskinengineering')

def ID(username):
    html = urllib.request.urlopen(baseURL + username).read()
    #print(html)

    object = json.loads(html)
    print(object['users'][0]['user']['pk'])

ID('ucsc')