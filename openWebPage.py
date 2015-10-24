#open a web page
import webbrowser
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    imgList = []
    titletext = []
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for attr in attrs:
                if attr == "src":
                    imgList.append(attr)
        #print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

home = "http://bookscouter.com"
ext1 = "/prices.php?isbn="
isbn = "0135114047"
ext2 = "&searchbutton=Sell"

url2 = "http://www.amazon.com/Calculus-Early-Transcendentals-James-Stewart/dp/0538497904/ref=sr_1_1?s=books&ie=UTF8&qid=1445657141&sr=1-1&keywords=calculus+early+transcendentals"

url3 = "http://www.amazon.com/Management-Turfgrass-Diseases-Vargas-Jr/dp/0471474118/ref=sr_1_1?ie=UTF8&qid=1445652814&sr=8-1&keywords=management+of+turfgrass+disease"

urlResults = "http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords=calculus+textbook"

url = home + ext1 + isbn + ext2
file = urllib2.urlopen(urlResults)
file_str_first = file.read() #whole html

#print file_str

start_str = file_str_first
linksToVisit = []

for i in range(0,16):
    print start_str[:100]
    int_from_result = start_str.find("<li id=\"result_" + str(i))
    string_from_result = start_str[int_from_result:]
    print string_from_result[:100]
#if string_from_result.find("Categories related") < string_from_result.find("href"):
        #continue
    int_href = string_from_result.find("href")
    string_from_href = string_from_result[int_href+6:]
    print string_from_href[:100]
    int_endquote = string_from_href.find("\"")
    string_link = string_from_href[:int_endquote]
    print string_link
    linksToVisit.append(string_link)
    start_str = string_from_href[int_endquote:]


#print linksToVisit



def getPageFeatures(file_str):
#find <div id="mainImageContainer"
    int_imgContainer = file_str.find("<div id=\"mainImageContainer\"")
    file_from_Container = file_str[int_imgContainer:]
    http_int = file_from_Container.find("http")
    file_from_http = file_from_Container[http_int:]
    jpg_int = file_from_http.find("\"")
    imgurl_substring = file_from_http[: jpg_int]
    print imgurl_substring
#find title
    int_titleSpan = file_str.find("<span id=\"productTitle\"")
    file_from_TitleTag = file_str[int_titleSpan:]
    closTag_int = file_from_TitleTag.find(">")
    closTag_int = closTag_int + 1
    file_from_title = file_from_TitleTag[closTag_int:]
    nextOpenTag_int = file_from_title.find("<")
    titleText_substring = file_from_title[:nextOpenTag_int]
    titleText_Split = titleText_substring.split()
    print titleText_Split
#find isbn
    int_ISBN = file_str.find("<div id=\"isbn_feature_div")
    file_from_ISBN = file_str[int_ISBN:]
    isbn10_int = file_from_ISBN.find("ISBN-10")
    file_from_ISBN10 = file_from_ISBN[isbn10_int:]
    endOfSpan_int = file_from_ISBN10.find("\">")
    file_from_endOfSpan = file_from_ISBN10[endOfSpan_int+2:]
    endOfISBN = file_from_endOfSpan.find("<")
    ISBN_substring = file_from_endOfSpan[:endOfISBN]
    print ISBN_substring




for link in linksToVisit:
    file_to_open = urllib2.urlopen(link)
    full_html_get_features = file_to_open.read() 
    getPageFeatures(full_html_get_features)




#parser = MyHTMLParser()
#parser.feed(file_str)

#webbrowser.open_new(imgurl_substring)


        


