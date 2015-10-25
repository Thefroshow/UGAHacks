from clarifai_basic import ClarifaiCustomModel
from clarifai.client import ClarifaiApi
import urllib2
import sys
import json
import openWebPage
from openWebPage import Textbook
import encode
import decode
import pilexample
from PIL import Image
import isbnList


#get the picture from file on computer
bookPic = "/Users/Jaris/Desktop/GameProgrammingPatterns.jpg"

clarifai = ClarifaiCustomModel()

probMax = 0
maxScoreISBN = ""



for isbn in isbnList.getISBNList():
    print encode.NumericToAlpha(isbn)
    result = clarifai.predict("http://ecx.images-amazon.com/images/I/51TMVvrxCbL._SX404_BO1,204,203,200_.jpg", encode.NumericToAlpha(isbn))
    data = json.dumps(result)
    jdata = json.loads(data)
    jresults = jdata['urls'][0]['score']
    print jresults


    if result['urls'][0]['score'] > probMax:
        probMax = result['urls'][0]['score']
        maxScoreISBN = isbn

isbn = maxScoreISBN



home = "http://bookscouter.com"
ext1 = "/prices.php?isbn="
ext2 = "&searchbutton=Sell"

url = home + ext1 + isbn + ext2

webbrowser.open_new(url)
