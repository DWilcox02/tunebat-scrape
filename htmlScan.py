#Must copy and paste artist doc info into artist1.html and artist2.html

from nntplib import ArticleInfo
from song import Song
import requests
from bs4 import BeautifulSoup
import pandas as pd



def getSongList():
    soup1 = BeautifulSoup(open("artist1.html"), "html.parser")
    soup2 = BeautifulSoup(open("artist2.html"), "html.parser")
        
    soups = [soup1, soup2]
    list1 = []
    list2 = []
    listIndex = 1
    for soup in soups:
        cards = soup.find_all("div", {"class": "ant-row pDoqI"})
        for card in cards:
            details = card.find("div", {"class": "ant-row NYZ7Y"})
            columns = details.find_all("div", {"class": "ant-col"})
            for column in columns:
                text = column.text
                name = ""
                artist = ""
                key = ""
                tempo = 0
                camelot = ""
                if "..." in text:
                    i = text.find("...")
                    # Get artist name(s)
                    artist = text[:i]
                    length= len(artist)
                    if "lg" in artist:
                        artist = artist[0:length - 2]
                    else:
                        artist = artist[0:length - 1]
                    # Get song name
                    name = text[i + 3:]
                    length = len(name)
                    name = name[:length - 5]
                else:
                    keyIndex = text.find("Key")
                    key = text[:keyIndex + 3]
                    text = text[keyIndex + 3:]
                    BPMIndex = text.find("BPM")
                    bpmStr = text[:BPMIndex]
                    bpm = int(bpmStr)
                    text = text[BPMIndex + 3:]
                    camelot = text
                if (artist == "Lil Peep") | (artist == "Panic! At The Disco"):
                    song = Song(artist=artist, name=name, key=key, tempo=tempo,camelot=camelot)
                    if listIndex == 1:
                        list1.append(song)
                    else:
                        list2.append(song)
        listIndex = listIndex + 1

    return  list1, list2