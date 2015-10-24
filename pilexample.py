from PIL import Image, ImageFilter
import urllib, cStringIO

file = cStringIO.StringIO(urllib.urlopen("http://www.joomlaworks.net/images/demos/galleries/abstract/7.jpg").read())
im = Image.open(file)
imblur = im.filter(ImageFilter.BLUR)
