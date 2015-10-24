from clarifai.client import ClarifaiApi
import json
image = raw_input("pls gib image ")
clarifai_api = ClarifaiApi() # assumes environment variables are set.
result = clarifai_api.tag_images(open(image))
data = json.dumps(result)
jdata = json.loads(data)
jresults = jdata['results'][0]['result']['tag']['classes'][0]

for item in jresults:
    print item
