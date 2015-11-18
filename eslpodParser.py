import urllib.request
import sys
from bs4 import BeautifulSoup
import re
import time
import logging


def main(url):
    logging.basicConfig(filename='eslpod.log',level=logging.INFO)
    while True:
        html = urllib.request.urlopen(url).read()
        soupPage = BeautifulSoup(html, "lxml")
        tags = soupPage('a')
        reSite = re.search("(^http.+)show_all.php", url)
        site = reSite.group(1)
        prevUrl = url
        for tag in tags:
            link = tag.get('href', None)
            if (re.match("^http.+mp3$", link)) != None:
                logging.info(link)
                print(link)
            elif (tag.contents[0] == "next"):
                url = site + link
        logging.info(url)
        print(url)
        if prevUrl == url:
            break
        logging.info('Pause 10 second')
        print("Pause 10 second")
        time.sleep(10)

if __name__ == '__main__':
    url = "https://www.eslpod.com/website/show_all.php"
    main(url)
