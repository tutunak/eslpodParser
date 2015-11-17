import urllib.request
import sys
from bs4 import BeautifulSoup
import re


def main(url):
    html = urllib.request.urlopen(url).read()
    soupPage = BeautifulSoup(html, "lxml")
    tags = soupPage('a')
    reSite = re.search("(^http.+)show_all.php", url)
    site = reSite.group(1)
    for tag in tags:
        link = tag.get('href', None)
        if (re.match("^http.+mp3$", link)) != None:
            print(link)
        elif (tag.contents[0] == "next"):
            url = site + link
    print(url)


if __name__ == '__main__':
    url = "https://www.eslpod.com/website/show_all.php"
    main(url)
