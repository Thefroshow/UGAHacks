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

textbooks = openWebPage.amazonSearchPage("http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords=calculus+textbook")
for tb in textbooks:
    #tb.printSelf()
    tb.printImgURL()
