import urllib.request
import sys
from bs4 import BeautifulSoup


def main(url):
    html = urllib.request.urlopen(url).read()
    soupPage = BeautifulSoup(html)
    tags = soupPage('a')
    for i in tags:
        print (i.get('href', None))


if __name__ == '__main__':
    main(sys.argv[1])
