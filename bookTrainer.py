# BOOK TRAINER #

#import all the stuffs
from clarifai_basic import ClarifaiCustomModel
concept = ClarifaiCustomModel()

#assign the stuffs
image_url = ""
tag = ""


ISBN_DICT = {tag:image_url}

#Provide some positive example images for concept
concept.positive(image_url, tag );
