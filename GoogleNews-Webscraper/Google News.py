from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

root = "https://www.google.com/"
link = "https://www.google.com/search?q=biden&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwjAvsKDyOXtAhXBhOAKHXWdDgcQpwUIKQ&biw=1604&bih=760&dpr=1.2"

def news(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html5lib')
    for item in soup.find_all('div', attrs={'class': 'ZINbbc xpd O9g5cc uUPGi'}):
        raw_link = (item.find('a', href=True)['href'])
        link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
                
        title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
        description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())

        title = title.replace(",", "")
        description = description.replace(",", "")

        time = description.split(" · ")[0]
        descript = description.split(" · ")[1]
        
        print(title)
        print(time)
        print(descript)
        print(link)
        document = open("Data.csv", "a")
        document.write("{}, {}, {}, {} \n".format(title, time, descript, link))
        document.close()
        
    next = soup.find('a', attrs={'aria-label':'Next page'})
    next = (next['href'])
    link = root + next
    news(link)
news(link)
