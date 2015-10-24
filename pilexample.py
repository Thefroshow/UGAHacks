from PIL import Image, ImageFilter, ImageShow
import urllib, cStringIO

file = cStringIO.StringIO(urllib.urlopen("https://upload.wikimedia.org/wikipedia/en/4/4f/Sharpe's_Siege_front_book_cover.jpg").read())
im = Image.open(file)
im.save("file_clean.jpg")
imblur = im.filter(ImageFilter.BLUR)
imblur.save("file_blurred.jpg")
