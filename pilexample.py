from PIL import Image, ImageFilter, ImageShow
import urllib, cStringIO
testimgURL = "http://www.man7.org/tlpi/cover/TLPI-front-cover.png"
testFile = cStringIO.StringIO(urllib.urlopen(testimgURL).read())


def filterFun(file):
    """FUN WITH PIL.ImageFilter!"""

    im = Image.open(file)
    im.save("ImageTesting/file_clean.png")

    #blur dat shit
    imBlur = im.filter(ImageFilter.BLUR)
    imBlur.save("ImageTesting/file_blurred.png")

    #smooth dat shit
    imSmooth = im.filter(ImageFilter.SMOOTH)
    imSmooth.save("ImageTesting/file_smooth.png")

    #SHARPEN
    imSharpen = im.filter(ImageFilter.SHARPEN)
    imSharpen.save("ImageTesting/file_sharpen.png")

    #DETAIL
    imDetail = im.filter(ImageFilter.DETAIL)
    imDetail.save("ImageTesting/file_detail.png")

filterFun(testFile)
