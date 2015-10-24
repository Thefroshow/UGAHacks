##################
# Pillow Example #
# -Josh Harper   #
##################

#import statements
from PIL import Image, ImageFilter, ImageShow
import urllib, cStringIO

#declare global variables
testimgURL = "http://www.man7.org/tlpi/cover/TLPI-front-cover.png"
testFile = cStringIO.StringIO(urllib.urlopen(testimgURL).read())

#function for running an image file through filters and saving the results
def filterFun(imgFile):
    """FUN WITH PIL.ImageFilter!
    A quick note about Emboss and Detail filters:
    we do not want to use them..
    emboss makes the image all grey and shit
    and detail removes the color..
    """

    #open and save original image file
    im = Image.open(imgFile)
    im.save("ImageTesting/file_clean.png")

    #BLUR
    imBlur = im.filter(ImageFilter.BLUR)
    imBlur.save("ImageTesting/file_blurred.png")

    #SMOOTH
    imSmooth = im.filter(ImageFilter.SMOOTH)
    imSmooth.save("ImageTesting/file_smooth.png")

    #SHARPEN
    imSharpen = im.filter(ImageFilter.SHARPEN)
    imSharpen.save("ImageTesting/file_sharpen.png")

    #DETAIL
    imDetail = im.filter(ImageFilter.DETAIL)
    imDetail.save("ImageTesting/file_detail.png")

filterFun(testFile)
