
def alphaToNumeric(alpha):
    s1 = alpha.replace("A","0")
    s2 = s1.replace("B","1")
    s3 = s2.replace("C","2")
    s4 = s3.replace("D","3")
    s5 = s4.replace("E","4")
    s6 = s5.replace("F","5")
    s7 = s6.replace("G","6")
    s8 = s7.replace("H","7")
    s9 = s8.replace("I","8")
    s10 = s9.replace("J","9")
    return s10
    
str = "ABCDCAFFGX"
str_decoded = alphaToNumeric(str)
print str_decoded