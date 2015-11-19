import urllib.request
from bs4 import BeautifulSoup
import re


def main(url, lastCount):
    linkList = []
    html = urllib.request.urlopen(url).read()
    soupPage = BeatifulSoup(html, "xml")
    tags = soupPage('a')
    for tag in tags:
        link = tag.get('href', None)
        if (re.match("^http.+mp3$", link)) ! = None:
            linkList.append(link)
        if len(linkList >= lastCount): break

if __name__ == '__main__':
    url = "https://www.eslpod.com/website/show_all.php"
    lastCount = 10
