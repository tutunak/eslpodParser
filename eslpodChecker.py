import urllib.request
from bs4 import BeautifulSoup
import re


FILES_PATH = "~/"



def main(url, lastCount):
    linkList = []
    html = urllib.request.urlopen(url).read()
    soupPage = BeautifulSoup(html, "lxml")
    tags = soupPage('a')
    for tag in tags:
        link = tag.get('href', None)
        if (re.match("^http.+mp3$", link)) != None:
            linkList.append(link)
            print(link)
        if len(linkList) >= lastCount: break
    check_files(linkList)


def check_files(linkList):
    files = []
    for link in linkList:
        print(re.search("^.+\/(.+mp3$)", link).group(1))


if __name__ == '__main__':
    url = "https://www.eslpod.com/website/show_all.php"
    lastCount = 10
    main(url, lastCount)
