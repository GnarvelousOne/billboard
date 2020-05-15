#!/usr/bin/env/ python

import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import pandas as pd

webpage_response = requests.get('https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1990s')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

date = []
artist = []
song = []

pizza = soup.find_all('td')

x = 5
for i in range(140):
    if (pizza[x].string):
        date.append((pizza[x].string))
    else:
        date.append((pizza[x].a.string))
    if (pizza[x+1].string):
        artist.append((pizza[x+1].string))
    else:
        artist.append((pizza[x+1].a.string))
    if (pizza[x+2].string):
        song.append((pizza[x+2].string))
    else:
        song.append((pizza[x+2].a.string))
    x += 7

data = {'Date': date, 'Artist': artist, 'Song': song}

top1990 = pd.DataFrame(data)
print(top1990)
