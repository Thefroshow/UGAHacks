from clarifai.client import ClarifaiApi
import json

def get_the_fucking_tags(image):
    """Uses clarifai api to get image tags."""
    clarifai_api = ClarifaiApi() # assumes environment variables are set.
    result = clarifai_api.tag_images(open(image))
    data = json.dumps(result)
    jdata = json.loads(data)
    jresults = jdata['results'][0]['result']['tag']['classes'][0]
    return jresults

