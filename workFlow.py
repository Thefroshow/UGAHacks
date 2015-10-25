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
from upload import upload_pic
from imgurpython import ImgurClient

def goToBookScouterURL(url_in):
    clarifai = ClarifaiCustomModel()
    probMax = 0
    maxScoreISBN = ""
    print "Searching textbooks...."
    for isbn in isbnList.getISBNList():
        result = clarifai.predict(url_in, encode.NumericToAlpha(isbn))
        data = json.dumps(result)
        jdata = json.loads(data)
        jresults = jdata['urls'][0]['score']
        #print str(jresults) + ":" + encode.NumericToAlpha(isbn)
        if result['urls'][0]['score'] > probMax:
            probMax = result['urls'][0]['score']
            maxScoreISBN = isbn
    isbn = maxScoreISBN
    home = "http://bookscouter.com"
    ext1 = "/prices.php?isbn="
    ext2 = "&searchbutton=Sell"
    url = home + ext1 + isbn + ext2
    
    print "Found Textbook"
    print "ISBN-10 "+isbn+" with probablity: "+"%0.3f" % probMax
    
    webbrowser.open_new(url) #go to bookscouter.com

#i have no idea what im doing lol

IMGURL = ""
try:
    IMGURL = sys.argv[1]
except IndexError:
    print "Usage: python workflow.py <imageURL>"
    sys.exit()

#check command-line arg
# 1 url : do it
# 2 local : upload to imgur, get url go to 1
# 3 bad ? not handled


if IMGURL.startswith("http"):
    print "Detected Image Type: URL"
    goToBookScouterURL(IMGURL)
else:
    print "Detected Image Type: Local File"
    # some imgur shit
    # get that url
  
    client = ImgurClient("9b49c76280e81b6", "0e7bdd8b67230bdc28b419f611e098f07b6ee848")
    image = upload_pic(client, IMGURL)
    image_str = str(image['link'])
    goToBookScouterURL(image_str)
    
    