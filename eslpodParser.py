import urllib.request
import sys
from bs4 import BeautifulSoup
import re


def main(url):
    html = urllib.request.urlopen(url).read()
    soupPage = BeautifulSoup(html, "lxml")
    tags = soupPage('a')
    for i in tags:
        link = i.get('href', None)
        if (re.match("^http.+mp3$", link)) != None:
            print(link)


if __name__ == '__main__':
    main(sys.argv[1])
