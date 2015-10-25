from clarifai_basic import ClarifaiCustomModel
from clarifai.client import ClarifaiApi
import urllib2
import sys
import json
import openWebPage
import webbrowser
from openWebPage import Textbook
import encode
import decode
import pilexample
from PIL import Image
import isbnList
import webbrowser
import time

#i have no idea what im doing lol

clarifai = ClarifaiCustomModel()

try:
    if sys.argv[1] == None:
        print "BAD"
    else:
        print "how did i get here?"
except IndexError:
    print "gib url pls"
    print "goodbye.."
    time.sleep(3)
    sys.exit()

probMax = 0
maxScoreISBN = ""
IMGURL = sys.argv[1]


for isbn in isbnList.getISBNList():
<<<<<<< HEAD
    print "OH NO, MY DATA IS SHOWING"
    result = clarifai.predict(IMGURL, encode.NumericToAlpha(isbn))
=======
    print encode.NumericToAlpha(isbn)
    result = clarifai.predict("http://ecx.images-amazon.com/images/I/51opYcR6kVL._SX415_BO1,204,203,200_.jpg", encode.NumericToAlpha(isbn))
>>>>>>> d20a1387e5af3562e6f2dd40e36b120610a7c710
    data = json.dumps(result)
    jdata = json.loads(data)
    jresults = jdata['urls'][0]['score']
    print str(jresults) + ":" + encode.NumericToAlpha(isbn)


    if result['urls'][0]['score'] > probMax:
        probMax = result['urls'][0]['score']
        maxScoreISBN = isbn

isbn = maxScoreISBN



home = "http://bookscouter.com"
ext1 = "/prices.php?isbn="
ext2 = "&searchbutton=Sell"

url = home + ext1 + isbn + ext2

webbrowser.open_new(url)
