from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi() # assumes environment variables are set.
result = clarifai_api.tag_images(open('/Users/Jaris/Desktop/Lighthouse.jpg'))

print result

