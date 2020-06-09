#!/usr/bin/env/ python

import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://en.wikipedia.org/wiki/List_of_Billboard_Modern_Rock_Tracks_number_ones_of_the_1990s')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

date = []
artist = []
songdata = []
artistdata = []

cheese = soup.find_all('td')
burger = soup.find_all('th')

def artistFunc():
    for a in cheese:
        artistdata.append(a.get_text())

    artistList = []
    for div in artistdata:
        artistList.append(div)

    print(len(artistdata))

    artist = artistList[1:513]
    
    x = 0
    stringList = ""
    while x < len(artist):
        stringList += str(artist[x]).replace('\n',';')
        x = x + 1
    main2List = stringList.split(';')
    
    #  Run this to get the list printed to the console, to then copy/paste to bigList.
    #  There are 11 song titles in bigList, that you have to manually cut out and add to the song
    #  list in order.  This is due to special formatting at Wikipedia that throws off the scrap,
    #  and it just became easier to manually correct them than try to parse it out.
    #print(main2List)


    bigList = ['The Jesus and Mary Chain', 'December 30, 1989', '3', 'The Psychedelic Furs', 'January 20, 1990', '3', 'Peter Murphy', 'February 10, 1990', '7', "Sinéad O'Connor", 'March 31, 1990', '1', 'Midnight Oil', 'April 7, 1990', '1', 'The Church', 'April 14, 1990', '1', 'Depeche Mode', 'April 21, 1990', '3', "Sinéad O'Connor", 'May 12, 1990', '1', 'Midnight Oil', 'May 19, 1990', '1', 'The Sundays', 'May 26, 1990', '1', 'Depeche Mode', 'June 2, 1990', '1', 'World Party', 'June 9, 1990', '5', 'Concrete Blonde', 'July 14, 1990', '4', 'Gene Loves Jezebel', 'August 11, 1990', '1', 'David J', 'August 18, 1990', '1', 'Gene Loves Jezebel', 'August 25, 1990', '1', "Jane's Addiction", 'September 1, 1990', '1', 'The Railway Children', 'September 8, 1990', '1', "Jane's Addiction", 'September 15, 1990', '1', 'INXS', 'September 22, 1990', '1', 'The Cure', 'September 29, 1990', '2', 'The Replacements', 'October 13, 1990', '1', 'The Cure', 'October 20, 1990', '1', "Jane's Addiction", 'October 27, 1990', '1', 'The Replacements', 'November 3, 1990', '3', "Jane's Addiction", 'November 24, 1990', '3', 'The Sisters of Mercy', 'December 15, 1990', '5', 'Happy Mondays', 'January 19, 1991', '1', 'Sting', 'January 26, 1991', '2', 'Jesus Jones', 'February 9, 1991', '5', 'R.E.M.', 'March 16, 1991', '8', 'Simple Minds', 'May 11, 1991', '2', 'Elvis Costello', 'May 25, 1991', '4', 'Electronic', 'June 22, 1991', '2', 'Siouxsie and the Banshees', 'July 6, 1991', '5', 'Big Audio Dynamite II', 'August 10, 1991', '4', 'The Psychedelic Furs', 'September 7, 1991', '2', 'Robyn Hitchcock and the Egyptians', 'September 21, 1991', '5', 'Red Hot Chili Peppers', 'October 26, 1991', '2', 'U2', 'November 9, 1991', '2', 'Nirvana', 'November 23, 1991', '1', 'U2', 'November 30, 1991', '9', 'Talking Heads', 'February 1, 1992', '1', 'Lou Reed', 'February 8, 1992', '3', 'The Sugarcubes', 'February 29, 1992', '5', 'U2', 'April 4, 1992', '1', 'The Cure', 'April 11, 1992', '4', 'Cracker', 'May 9, 1992', '2', 'The Charlatans', 'May 23, 1992', '1', 'XTC', 'May 30, 1992', '2', 'The Cure', 'June 13, 1992', '4', "The B-52's", 'July 11, 1992', '4', 'Faith No More', 'August 8, 1992', '1', 'Morrissey', 'August 15, 1992', '6', 'Peter Gabriel', 'September 26, 1992', '2', 'Suzanne Vega', 'October 10, 1992', '1', 'R.E.M.', 'October 17, 1992', '5', '10,000 Maniacs', 'November 21, 1992', '2', 'Soul Asylum', 'December 5, 1992', '1', 'Peter Gabriel', 'December 12, 1992', '5', "Ned's Atomic Dustbin", 'January 16, 1993', '1', 'Jesus Jones', 'January 23, 1993', '6', 'Belly', 'March 6, 1993', '3', 'Depeche Mode', 'March 27, 1993', '5', 'New Order', 'May 1, 1993', '2', 'Depeche Mode', 'May 15, 1993', '1', 'New Order', 'May 22, 1993', '4', 'Porno for Pyros', 'June 19, 1993', '5', 'Tears for Fears', 'July 24, 1993', '3', 'Red Hot Chili Peppers', 'August 14, 1993', '4', 'The Juliana Hatfield Three', 'September 11, 1993', '1', 'Blind Melon', 'September 18, 1993', '1', 'Red Hot Chili Peppers', 'September 25, 1993', '1', 'Blind Melon', 'October 2, 1993', '2', 'Nirvana', 'October 16, 1993', '3', 'The Lemonheads', 'November 6, 1993', '9', 'Pearl Jam', 'January 8, 1994', '1', 'Gin Blossoms', 'January 15, 1994', '1', 'Nirvana', 'January 22, 1994', '2', 'Beck', 'February 5, 1994', '5', 'Crash Test Dummies', 'March 12, 1994', '1', 'Tori Amos', 'March 19, 1994', '2', 'Morrissey', 'April 2, 1994', '7', 'Live', 'May 21, 1994', '3', 'Green Day', 'June 11, 1994', '1', 'Toad the Wet Sprocket', 'June 18, 1994', '6', 'The Offspring', 'July 30, 1994', '2', 'Counting Crows', 'August 13, 1994', '1', 'Green Day', 'August 20, 1994', '5', 'R.E.M.', 'September 24, 1994', '5', 'The Cranberries', 'October 29, 1994', '6', 'Nirvana', 'December 10, 1994', '1', 'R.E.M.', 'December 17, 1994', '3', 'Green Day', 'January 7, 1995', '7', 'Live', 'February 25, 1995', '9', 'Better Than Ezra', 'April 29, 1995', '5', 'Soul Asylum', 'June 3, 1995', '3', 'U2', 'June 24, 1995', '4', 'Alanis Morissette', 'July 22, 1995', '5', 'Green Day', 'August 26, 1995', '1', 'Silverchair', 'September 2, 1995', '3', 'Bush', 'September 23, 1995', '2', 'Goo Goo Dolls', 'October 7, 1995', '1', 'Alanis Morissette', 'October 14, 1995', '1', 'The Presidents of the United States of America', 'October 21, 1995', '1', 'Goo Goo Dolls', 'October 28, 1995', '3', 'Red Hot Chili Peppers', 'November 18, 1995', '4', 'Bush', 'December 16, 1995', '2', 'Oasis', 'December 30, 1995', '9', 'The Smashing Pumpkins', 'March 2, 1996', '1', 'Oasis', 'March 9, 1996', '1', 'Alanis Morissette', 'March 16, 1996', '3', 'Oasis', 'April 6, 1996', '5', 'The Cranberries', 'May 11, 1996', '4', 'Tracy Bonham', 'June 8, 1996', '3', 'Dishwalla', 'June 29, 1996', '1', 'Butthole Surfers', 'July 6, 1996', '3', 'Primitive Radio Gods', 'July 27, 1996', '6', 'Pearl Jam', 'September 7, 1996', '1', '311', 'September 14, 1996', '4', 'Eels', 'October 12, 1996', '2', 'Sublime', 'October 26, 1996', '3', 'Bush', 'November 16, 1996', '7', 'Garbage', 'January 4, 1997', '4', 'U2', 'February 1, 1997', '4', 'Live', 'March 1, 1997', '1', 'The Wallflowers', 'March 8, 1997', '5', 'U2', 'April 12, 1997', '3', 'The Verve Pipe', 'May 3, 1997', '3', 'Third Eye Blind', 'May 24, 1997', '5', 'The Mighty Mighty Bosstones', 'June 28, 1997', '1', 'Third Eye Blind', 'July 5, 1997', '3', 'Matchbox Twenty', 'July 26, 1997', '1', 'Sugar Ray', 'August 2, 1997', '8', 'Smash Mouth', 'September 27, 1997', '5', 'Chumbawamba', 'November 1, 1997', '7', 'Everclear', 'December 20, 1997', '1', 'Marcy Playground', 'December 27, 1997', '15', 'Fastball', 'April 11, 1998', '7', 'Semisonic', 'May 30, 1998', '5', 'Goo Goo Dolls', 'July 4, 1998', '5', 'Eve 6', 'August 8, 1998', '2', 'Barenaked Ladies', 'August 22, 1998', '1', 'Eve 6', 'August 29, 1998', '1', 'Barenaked Ladies', 'September 5, 1998', '4', 'Eve 6', 'October 3, 1998', '1', 'Hole', 'October 10, 1998', '3', 'Goo Goo Dolls', 'October 31, 1998', '1', 'Hole', 'November 7, 1998', '1', 'Goo Goo Dolls', 'November 14, 1998', '1', 'Lenny Kravitz', 'November 21, 1998', '2', 'Cake', 'December 5, 1998', '3', 'Everlast', 'December 26, 1998', '8', 'Sugar Ray', 'February 20, 1999', '1', 'Everlast', 'February 27, 1999', '1', 'Sugar Ray', 'March 6, 1999', '5', 'Lit', 'April 10, 1999', '11', 'Red Hot Chili Peppers', 'June 26, 1999', '16', 'Creed', 'October 16, 1999', '1', 'Bush', 'October 23, 1999', '2', 'Foo Fighters', 'November 6, 1999', '1', 'Bush', 'November 13, 1999', '2', 'Creed', 'November 27, 1999', '1', 'Bush', 'December 4, 1999', '1', 'Creed', 'December 11, 1999', '1', 'Limp Bizkit', 'December 18, 1999', '1', 'Blink-182', 'December 25, 1999', '8']

    #  Splits bigList into 3
    h = 0
    i = 1
    j = 2
    artistString = []
    while h < len(bigList):
        artistString.append(bigList[h])
        h = h + 3
    print(artistString)
    print(len(artistString))
    dateString = []
    while i < len(bigList):
        dateString.append(bigList[i])
        i = i + 3
    print(dateString)
    print(len(dateString))

    weeksString = []
    while j < len(bigList):
        weeksString.append(bigList[j])
        j = j + 3
    print(weeksString)
    print(len(weeksString))


#artistFunc()

def songFunc():
    for a in burger:
        songdata.append(a.get_text())
    '''
    songList = []
    for div in songdata:
        songList.append(div)
    '''
    song = songdata[5:161]
    print(len(song))

    h = 0
    songString = []
    while h < len(song):
        songString.append(song[h].replace('\n',''))
        h = h + 1
    
    print(songString)
    print(len(songString))

    # Will have to fix 11 song title errors mentioned above.
    # Make sure lengths of all 4 lists match.
        
songFunc()
