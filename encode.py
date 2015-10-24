#SUPER CUSTOM UGAHACKS ISBN ENCODER

def NumericToAlpha(num):
    s1 = num.replace("0","A")
    s2 = s1.replace("1","B")
    s3 = s2.replace("2","C")
    s4 = s3.replace("3","D")
    s5 = s4.replace("4","E")
    s6 = s5.replace("5","F")
    s7 = s6.replace("6","G")
    s8 = s7.replace("7","H")
    s9 = s8.replace("8","I")
    s10 = s9.replace("9","J")
    return s10

str = "013110362X"
str_encoded = NumericToAlpha(str)
print str_encoded
