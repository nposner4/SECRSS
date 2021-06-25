import feedparser
import urllib.request
from bs4 import BeautifulSoup
import time
from time import sleep
import winsound

oldres = ''
while True:
    sleep(0.12)
    newsfeed = feedparser.parse('https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=4&company=&dateb=&owner=include&start=0&count=40&output=atom')
    entry = newsfeed.entries[0]
    links = entry.links[0]
    link = links.get('href')
    content = urllib.request.urlopen(''+link)
    read_content = content.read()
    soup = BeautifulSoup(read_content, 'html.parser')
    for a in soup.find_all('a', href= True):
        str = a['href']
        if str.startswith("/Archives"):
            res = "https://www.sec.gov" + str
            if res != oldres:
                print(res)
                print(time.ctime())
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                oldres = res
                break
            break
