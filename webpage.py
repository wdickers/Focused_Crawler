from bs4 import BeautifulSoup,Comment
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

class Webpage:
    def __init__(self):
        self.pageUrl = ""
        self.title = ""
        self.text = ""

    def __init__(self,url):
        self.pageUrl = url
        myopener = MyOpener()
        page = myopener.open(url)
        soup = BeautifulSoup(page)
        
        self.title = ""
        if soup.title:
            self.title = soup.title.string
        text_nodes = soup.findAll(text=True)
        visible_text = filter(visible, text_nodes)
        self.text = ''.join(visible_text)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head']:
        return False
    return True