import requests
from bs4 import BeautifulSoup
from config import url


page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#finds total number of pages
pages = []
for pg in soup.findAll('a', attrs={'class':'page-link'}):
    try:
        int(pg.text)
        pages.append(int(pg.text))
    except ValueError:
        pass

ttl_pages = max(pages)

product_title = []
prices = []

for i in range(1,ttl_pages+1):
    req = requests.get(url + '?page={}'.format(i))
    soup = BeautifulSoup(req.text, 'html.parser')
    [product_title.append(t.text) for t in soup.findAll('div', attrs={'class':'card-title'})]
    [prices.append(p.text) for p in soup.findAll('div', attrs={'class':'card-price'})]
