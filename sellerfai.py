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

#clarifai = ClarifaiCustomModel()

def trainTextbook(textbook):
    clarifai = ClarifaiCustomModel()
    
    con_name = textbook.isbn.replace(" ","B_")
    concept_name = con_name.replace("\"","")    

    concept_name = con_name.replace("\"","")

    concept_name1 = "Calculus"
    concept_name2 = "ISBN7hi"
    concept_name3 = con_name
    
    #import pdb
    #pdb.set_trace()

    PHISH_POSITIVES = [
        textbook.imgURL
        ]
    
    for positive_example in PHISH_POSITIVES:
        clarifai.positive(positive_example, concept_name2)
        
        PHISH_NEGATIVES = [
            ]
        
        for negative_example in PHISH_NEGATIVES:
            clarifai.negative(negative_example, concept_name2)
            
            
    clarifai.train(concept_name2)
           

    result = clarifai.predict(textbook.imgURL, concept_name2)
    print result['status']['message'], "%0.3f" % result['urls'][0]['score'], result['urls'][0]['url']
    print result


textb = Textbook("http://i.imgur.com/Lr6Ncvdb.jpg","title","123")
trainTextbook(textb)


#exit(3)
textbooks = openWebPage.amazonSearchPage("http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords=calculus+textbook")
for tb in textbooks:
    trainTextbook(tb)
    tb.printImgURL()

