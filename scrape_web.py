# Justin Foxhoven
# djustinf

import urllib3
import certifi
from bs4 import BeautifulSoup
from bs4.element import Comment

def scrape(url):
    # SSL enabled because urllib3 is unhappy otherwise...
    # Plus it's good practice so why not right?
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                               ca_certs=certifi.where(),
                               timeout=10,
                               retries=urllib3.Retry(5))

    # Grab the desired page and make it something usable.
    pageHtml = http.request('GET', url).data
    soup = BeautifulSoup(pageHtml, "html.parser")
    text = soup.findAll(text=True)
    visibleText = filter(visible, text)

    return str(' '.join(word.strip() for word in visibleText))

# Only grab visible text on the page
def visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
