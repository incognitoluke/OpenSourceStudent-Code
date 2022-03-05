from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests


# Update the link of the item
link = "https://www.ebay.com/itm/255403814544?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20200708143445%26meid%3D9566f8eb22734c588556a1e16bd5d4ad%26pid%3D101251%26rk%3D1%26rkt%3D1%26itm%3D255403814544%26pmt%3D1%26noa%3D1%26pg%3D2380057%26algv%3DPersonalizedTopicsV2WithSimilarCategoriesPurchaseSuppression%26brand%3DNike&_trksid=p2380057.c101251.m47269&_trkparms=pageci%3A6d8c92c1-9c18-11ec-90a8-b28fdcdb8470%7Cparentrq%3A57684b3717f0a1208ba2fc98fffe7e82%7Ciid%3A1&var=555367547281"

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    price = soup.find('span',attrs={'itemprop':'price'})['content']
    print(price)
