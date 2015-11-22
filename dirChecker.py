import re
from os import listdir
from os.path import isfile, join
import time

FILE_LIST = 'fileList.txt'
FILES_PATH = "/home/tutunak/manuals/english/eslpod"

def main():
    fileList = []
    linkList = open(FILE_LIST, 'r')
    for i in linkList:
        fileList.append(re.search("^.+\/(.+mp3$)", i).group(1))
    files = [f for f in listdir(FILES_PATH) if isfile(join(FILES_PATH, f))]
    for i in fileList:
        print(i)
        time.sleep(0.1)
        if i not in files:
            print(i, " not in dir")



if __name__ == '__main__':
    main()
