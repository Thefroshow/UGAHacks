#Richard Saney
#Josh Harper
#Alex Hunt

#[endpoint] => http://research.api.sellerlabs.com/
#[key] => 1445656217|slapi|c546db3b045236ccad072dea3d86317b

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
import urlList
import time

#image to tags
#tags dictionary
#endpoint = "http://research.api.sellerlabs.com/"
#key = "1445656217|slapi|c546db3b045236ccad072dea3d86317b"
#response = urllib2.urlopen('http://')
#html = response.read()

'''
def get_the_tags(image):
    """Uses clarifai api to get image tags."""
    clarifai_api = ClarifaiApi() # assumes environment variables are set.
    result = clarifai_api.tag_images(open(image))
    data = json.dumps(result)
    jdata = json.loads(data)
    jresults = jdata['results'][0]['result']['tag']['classes'][0]
    return jresults
'''
'''
imgFile = sys.argv[1]  #the jpeg passed in
if(!(imgFile.endsWith(".jpeg") || imgFile.endsWith(".png") || imgFile.endsWith(".gif") || imgFile.endsWith(".jpg"))):
    print "Bad end file extension"
    sys.exit(0)
'''



def trainTextbook(textbook, textbooks):
    clarifai = ClarifaiCustomModel()


    concept_name = encode.NumericToAlpha(textbook.isbn[1:])

    PHISH_POSITIVES = [
        textbook.imgURL
        #pilexample.filterBlur(textbook.imgURL)
        ]

    for positive_example in PHISH_POSITIVES:
        clarifai.positive(positive_example, concept_name)

        PHISH_NEGATIVES = []

        for t in textbooks:
            if t != textbook:
                PHISH_NEGATIVES.append(t.imgURL)



        for negative_example in PHISH_NEGATIVES:
            clarifai.negative(negative_example, concept_name)


    clarifai.train(concept_name)


    result = clarifai.predict(textbook.imgURL, concept_name)
    print result['status']['message'], "%0.3f" % result['urls'][0]['score'], result['urls'][0]['url']
    print concept_name
    print decode.alphaToNumeric(concept_name)





'''
urls = ["http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords=calculus+textbook","http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=data+mining+textbook&rh=i%3Aaps%2Ck%3Adata+mining+textbook"]
#for url in urls:

textbooks = []

for i in range(0,len(urlList.getURLLIST())):
    try:
        file_to_open = urllib2.urlopen(urlList.getURLLIST()[i])
        full_html_get_features = file_to_open.read()
    #print openWebPage.getPageFeatures(url)
        textbooks.append(openWebPage.getPageFeatures(full_html_get_features))
    except urllib2.HTTPError:
        print "THE DARK LORD SUMMONS EVIL TCP/IP PACKETS"
        time.sleep(2)
        i = i-1
'''
'''
i = 0
textbooks = makeTextbookList(0)
for tb in textbooks:
    print i
    tb.printSelf()
    trainTextbook(tb, textbooks)
    i = i +1
'''

#print len(textbooks)

#call first time with 0 as param and empty textbooks
def makeTextbookList(index, textbooks):
    url_list = urlList.getURLLIST()
    for i in range(index, len(url_list)):
        try:
            ith_url = urllib2.urlopen(url_list[i])
            htmlPage = ith_url.read()
            textbooks.append(openWebPage.getPageFeatures(htmlPage))
        except urllib2.HTTPError:
            print "Error sleep for 1 second"
            time.sleep(2)
            return makeTextbookList(i, textbooks)
    return textbooks


i = 0
textbooks = []
textbooks = makeTextbookList(0, textbooks)
for tb in textbooks:
    print tb.isbn
    #trainTextbook(tb, textbooks)

