
var date = ['January 20, 1990', 'February 10, 1990', 'March 3, 1990', 'March 24, 1990', 'April 7, 1990', 'April 14, 1990', 'April 21, 1990', 'May 19, 1990', 'June 9, 1990', 'June 16, 1990', 'June 30, 1990', 'July 21, 1990', 'August 4, 1990', 'September 1, 1990', 'September 8, 1990', 'September 15, 1990', 'September 29, 1990', 'October 6, 1990', 'October 13, 1990', 'October 20, 1990', 'October 27, 1990', 'November 3, 1990', 'November 10, 1990', 'December 1, 1990', 'December 8, 1990', 'January 5, 1991', 'January 19, 1991', 'January 26, 1991', 'February 9, 1991', 'February 23, 1991', 'March 9, 1991', 'March 23, 1991', 'March 30, 1991', 'April 13, 1991', 'April 20, 1991', 'April 27, 1991', 'May 11, 1991', 'May 18, 1991', 'May 25, 1991', 'June 8, 1991', 'June 15, 1991', 'July 20, 1991', 'July 27, 1991', 'September 14, 1991', 'September 21, 1991', 'October 5, 1991', 'October 12, 1991', 'November 2, 1991', 'November 9, 1991', 'November 23, 1991', 'November 30, 1991', 'December 7, 1991', 'January 25, 1992', 'February 1, 1992', 'February 8, 1992', 'February 29, 1992', 'March 21, 1992', 'April 25, 1992', 'June 20, 1992', 'July 4, 1992', 'August 8, 1992', 'August 15, 1992', 'November 14, 1992', 'November 28, 1992', 'March 6, 1993', 'March 13, 1993', 'May 1, 1993', 'May 15, 1993', 'July 10, 1993', 'July 24, 1993', 'September 11, 1993', 'November 6, 1993', 'December 11, 1993', 'December 25, 1993', 'January 22, 1994', 'February 12, 1994', 'March 12, 1994', 'April 9, 1994', 'May 21, 1994', 'August 6, 1994', 'August 27, 1994', 'December 3, 1994', 'December 17, 1994', 'January 28, 1995', 'February 25, 1995', 'April 15, 1995', 'June 3, 1995', 'July 8, 1995', 'August 26, 1995', 'September 2, 1995', 'September 9, 1995', 'September 30, 1995', 'November 25, 1995', 'December 2, 1995', 'March 23, 1996', 'May 4, 1996', 'May 18, 1996', 'July 13, 1996', 'July 27, 1996', 'August 3, 1996', 'November 9, 1996', 'December 7, 1996', 'February 22, 1997', 'March 22, 1997', 'May 3, 1997', 'May 24, 1997', 'June 14, 1997', 'August 30, 1997', 'September 13, 1997', 'October 4, 1997', 'October 11, 1997', 'January 17, 1998', 'January 31, 1998', 'February 14, 1998', 'February 28, 1998', 'March 14, 1998', 'April 4, 1998', 'April 25, 1998', 'May 23, 1998', 'June 6, 1998', 'September 5, 1998', 'October 3, 1998', 'October 17, 1998', 'November 14, 1998', 'November 28, 1998', 'December 5, 1998', 'January 16, 1999', 'January 30, 1999', 'February 13, 1999', 'March 13, 1999', 'April 10, 1999', 'May 8, 1999', 'June 12, 1999', 'July 17, 1999', 'July 24, 1999', 'July 31, 1999', 'September 4, 1999', 'September 18, 1999', 'October 9, 1999', 'October 23, 1999'];

var artist = ['Michael Bolton', 'Paula Abdul', 'Janet Jackson', 'Alannah Myles', 'Taylor Dayne', 'Tommy Page', "Sinéad O'Connor", 'Madonna', 'Wilson Phillips', 'Roxette', 'New Kids on the Block', 'Glenn Medeiros', 'Mariah Carey', 'Sweet Sensation', 'Jon Bon Jovi', 'Wilson Phillips', 'Nelson', 'Maxi Priest', 'George Michael', 'James Ingram', 'Janet Jackson', 'Vanilla Ice', 'Mariah Carey', 'Whitney Houston', 'Stevie B', 'Madonna', 'Janet Jackson', 'Surface', 'C+C Music Factory', 'Whitney Houston', 'Mariah Carey', 'Timmy T', 'Gloria Estefan', 'Londonbeat', 'Wilson Phillips', 'Amy Grant', 'Roxette', 'Hi-Five', 'Mariah Carey', 'Extreme', 'Paula Abdul', 'EMF', 'Bryan Adams', 'Paula Abdul', 'Color Me Badd', 'Marky Mark & the Funky Bunch', 'Mariah Carey', 'Karyn White', 'Prince', 'Michael Bolton', 'P.M. Dawn', 'Michael Jackson', 'Color Me Badd', 'George Michael', 'Right Said Fred', 'Mr. Big', 'Vanessa Williams', 'Kris Kross', 'Mariah Carey', 'Sir Mix-A-Lot', 'Madonna', 'Boyz II Men', 'The Heights', 'Whitney Houston', 'Peabo Bryson', 'Snow', 'Silk', 'Janet Jackson', 'SWV', 'UB40', 'Mariah Carey', 'Meat Loaf', 'Janet Jackson', 'Mariah Carey', 'Bryan Adams', 'Céline Dion', 'Ace Of Base', 'R. Kelly', 'All-4-One', 'Lisa Loeb & Nine Stories', 'Boyz II Men', 'Boyz II Men', 'Ini Kamoze', 'TLC', 'Madonna', 'Montell Jordan', 'Bryan Adams', 'TLC', 'Seal', 'Michael Jackson', 'Coolio', 'Mariah Carey', 'Whitney Houston', 'Mariah Carey & Boyz II Men', 'Céline Dion', 'Mariah Carey', 'Bone Thugs-N-Harmony', '2Pac', 'Toni Braxton', 'Los Del Rio', 'Blackstreet', 'Toni Braxton', 'Spice Girls', 'Puff Daddy', 'The Notorious B.I.G.', 'Hanson', 'Faith Evans', 'The Notorious B.I.G. featuring Puff Daddy & Mase', 'Mariah Carey', 'Boyz II Men', 'Elton John', 'Savage Garden', 'Janet Jackson', 'Usher', 'Céline Dion', 'Will Smith', 'K-Ci & JoJo', 'Next', 'Mariah Carey', 'Brandy', 'Aerosmith', 'Monica', 'Barenaked Ladies', 'Lauryn Hill', 'Divine', 'R. Kelly', 'Brandy', 'Britney Spears', 'Monica', 'Cher', 'TLC', 'Ricky Martin', 'Jennifer Lopez', "Destiny's Child", 'Will Smith', 'Christina Aguilera', 'Enrique Iglesias', 'TLC', 'Mariah Carey', 'Santana'];

var song = ['How Am I Supposed to Live Without You', 'Opposites Attract', 'Escapade', 'Black Velvet', 'Love Will Lead You Back', "I'll Be Your Everything", 'Nothing Compares 2 U', 'Vogue', 'Hold On', 'It Must Have Been Love', 'Step By Step', "She Ain't Worth It", 'Vision of Love', 'If Wishes Came True', 'Blaze Of Glory', 'Release Me', "(Can't Live Without Your) Love And Affection", 'Close To You', 'Praying for Time', "I Don't Have the Heart", 'Black Cat', 'Ice Ice Baby', 'Love Takes Time', "I'm Your Baby Tonight", 'Because I Love You (The Postman Song)', 'Justify My Love', 'Love Will Never Do (Without You)', 'The First Time', 'Gonna Make You Sweat (Everybody Dance Now)', 'All the Man That I Need', 'Someday', 'One More Try', 'Coming Out of the Dark', "I've Been Thinking About You", "You're in Love", 'Baby Baby', 'Joyride', 'I Like the Way (The Kissing Game)', "I Don't Wanna Cry", 'More Than Words', 'Rush Rush', 'Unbelievable', '(Everything I Do) I Do It for You', 'The Promise of a New Day', 'I Adore Mi Amor', 'Good Vibrations', 'Emotions', 'Romantic', 'Cream', 'When A Man Loves A Woman', 'Set Adrift on Memory Bliss', 'Black or White', 'All 4 Love', "Don't Let The Sun Go Down On Me", "I'm Too Sexy", 'To Be With You', 'Save the Best for Last', 'Jump', "I'll Be There", 'Baby Got Back', 'This Used To Be My Playground', 'End of the Road', 'How Do You Talk To An Angel', 'I Will Always Love You', 'A Whole New World', 'Informer', 'Freak Me', "That's The Way Love Goes", 'Weak', "(I Can't Help) Falling in Love with You", 'Dreamlover', "I'd Do Anything for Love (But I Won't Do That)", 'Again', 'Hero', 'All For Love', 'The Power Of Love', 'The Sign', "Bump n' Grind", 'I Swear', 'Stay (I Missed You)', "I'll Make Love to You", 'On Bended Knee', 'Here Comes the Hotstepper', 'Creep', 'Take A Bow', 'This Is How We Do It', 'Have You Ever Really Loved A Woman', 'Waterfalls', 'Kiss from a Rose', 'You Are Not Alone', "Gangsta's Paradise", 'Fantasy', 'Exhale (Shoop Shoop)', 'One Sweet Day', 'Because You Loved Me', 'Always Be My Baby', 'Tha Crossroads', 'How Do U Want It', "You're Makin' Me High", 'Macarena (Bayside Boys Mix)', 'No Diggity', 'Un-Break My Heart', 'Wannabe', "Can't Nobody Hold Me Down", 'Hypnotize', 'MMMBop', "I'll Be Missing You", 'Mo Money Mo Problems', 'Honey', '4 Seasons of Loneliness', "Candle in the Wind '97", 'Truly Madly Deeply', 'Together Again', 'Nice & Slow', 'My Heart Will Go On', "Gettin' Jiggy Wit It", 'All My Life', 'Too Close', 'My All', 'The Boy Is Mine', "I Don't Want to Miss a Thing", 'The First Night', 'One Week', 'Doo Wop (That Thing)', 'Lately', "I'm Your Angel", 'Have You Ever', 'Baby One More Time', 'Angel of Mine', 'Believe', 'No Scrubs', "Livin' la Vida Loca", 'If You Had My Love', 'Bills, Bills, Bills', 'Wild Wild West', 'Genie in a Bottle', 'Bailamos', 'Unpretty', 'Heartbreaker', 'Smooth'];

let datetext = document.getElementById("datetext");
let artisttext = document.getElementById("artisttext");
let songtext = document.getElementById("songtext");

datetext.innerHTML = date[0];
artisttext.innerHTML = artist[0];
songtext.innerHTML = song[0];

window.onload=()=>{
  var artisturl = document.querySelector("#artistlink");
  artisturl.href = 'https://www.youtube.com/results?search_query='+artisttext.innerHTML;
  var songurl = document.querySelector("#songlink");
  songurl.href = 'https://www.youtube.com/results?search_query='+artisttext.innerHTML+' '+songtext.innerHTML;
};

var i = 0;

$(document).ready(function(){
  $("#next").click(function(){
    datetext.innerHTML = date[i+1];
    console.log(date[i+1]);
    artisttext.innerHTML = artist[i+1];
    songtext.innerHTML = "'"+song[i+1]+"'";
    var artisturl = document.querySelector("#artistlink");
    artisturl.href = 'https://www.youtube.com/results?search_query='+artisttext.innerHTML;
    var songurl = document.querySelector("#songlink");
    songurl.href = 'https://www.youtube.com/results?search_query='+artisttext.innerHTML+' '+songtext.innerHTML;

    i ++;
  });
});

$(document).ready(function(){
  $("#previous").click(function(){
    datetext.innerHTML = date[i-1];
    console.log(date[i-1]);
    artisttext.innerHTML = artist[i-1];
    songtext.innerHTML = "'"+song[i-1]+"'";
    var artisturl = document.querySelector("#artistlink");
    artisturl.href = 'https://www.youtube.com/results?search_query='+artisttext.innerHTML;
    var songurl = document.querySelector("#songlink");
    songurl.href = 'https://www.youtube.com/results?search_query='+artisttext.innerHTML+' '+songtext.innerHTML;
    i --;
  });
});
