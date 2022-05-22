from song import Song
import requests
from bs4 import BeautifulSoup
import pandas as pd
from cloudscraper import cloudscraper

# Get artists
# artist1 = input("Artist 1: ")
artist1 = "lil peep"
artist1 = artist1.lower().strip().replace(" ", "-")
# artist2 = input("Artist 2: ")
# artist2 = artist2.lower().strip().replace(" ", "-")

r1 = requests.get("https://tunebat.com/Search?q=%s" % (artist1))
c1 = r1.content
soup1 = BeautifulSoup(c1, "html.parser")
print(type(c1))

scraper = cloudscraper.create_scraper()
r1 = scraper.get("https://tunebat.com/Search?q=%s" % (artist1))
with open("html.txt", "w") as file:
    file.write(r1.text())

#Does not work due to tunebat having too sophisticated cloudflare
