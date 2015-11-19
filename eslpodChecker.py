import urllib.request
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import re



FILES_PATH = "/tmp/eslpodtest"



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
    files = [f for f in listdir(FILES_PATH) if isfile(join(FILES_PATH, f))]
    #print(files)
    fne = []
    for link in linkList:
        filename = re.search("^.+\/(.+mp3$)", link).group(1)
        if filename  not in files:
            print("file not exist ", filename)
            fne.append()
    files_download(fne)

def files_download(download_list)

if __name__ == '__main__':
    url = "https://www.eslpod.com/website/show_all.php"
    lastCount = 10
    main(url, lastCount)
