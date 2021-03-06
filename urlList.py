###############
#Richard Saney#
###############

import openWebPage

def getURLLIST():
   websites = [
        "http://www.amazon.com/Code-Language-Computer-Hardware-Software/dp/0735611319/ref=sr_1_1?s=books&ie=UTF8&qid=1445728549&sr=1-1&keywords=programming",
        "http://www.amazon.com/Beginning-Programming-All--Reference-Dummies/dp/0470108541/ref=sr_1_2?s=books&ie=UTF8&qid=1445728549&sr=1-2&keywords=programming",
        "http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_3?s=books&ie=UTF8&qid=1445728549&sr=1-3&keywords=programming",
        "http://www.amazon.com/Programming-Language-Beginners-LEARN-DAY/dp/1514311259/ref=sr_1_4?s=books&ie=UTF8&qid=1445728549&sr=1-4&keywords=programming",
        "http://www.amazon.com/HTML-CSS-Design-Build-Websites/dp/1118008189/ref=sr_1_5?s=books&ie=UTF8&qid=1445728549&sr=1-5&keywords=programming",
        "http://www.amazon.com/Game-Programming-Patterns-Robert-Nystrom/dp/0990582906/ref=sr_1_7?s=books&ie=UTF8&qid=1445728549&sr=1-7&keywords=programming",
        "http://www.amazon.com/Smarter-Way-Learn-JavaScript-technology/dp/1497408180/ref=sr_1_8?s=books&ie=UTF8&qid=1445728549&sr=1-8&keywords=programming",
        "http://www.amazon.com/Programming-Language-Brian-W-Kernighan/dp/0131103628/ref=sr_1_9?s=books&ie=UTF8&qid=1445728549&sr=1-9&keywords=programming",
        "http://www.amazon.com/Programming-Absolute-Beginner-Jerry-Ford/dp/1598633740/ref=sr_1_10?s=books&ie=UTF8&qid=1445728549&sr=1-10&keywords=programming",
        "http://www.amazon.com/Python-Programming-Introduction-Computer-Science/dp/1590282418/ref=sr_1_11?s=books&ie=UTF8&qid=1445728549&sr=1-11&keywords=programming",
        #"http://www.amazon.com/Programming-Windows-JavaScript-Developer-Reference-ebook/dp/B00LX6D0PM/ref=sr_1_12?s=books&ie=UTF8&qid=1445728549&sr=1-12&keywords=programming",
        "http://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X/ref=sr_1_13?s=books&ie=UTF8&qid=1445729409&sr=1-13&keywords=programming",
        #"http://www.amazon.com/Programming-Sucks-Aspiring-Developers-Guide-ebook/dp/B00MNFRKPS/ref=sr_1_14?s=books&ie=UTF8&qid=1445729423&sr=1-14&keywords=programming",
        #"http://www.amazon.com/Programming-Guide-Computer-LEARN-Design-ebook/dp/B00XS06I8C/ref=sr_1_15?s=books&ie=UTF8&qid=1445729423&sr=1-15&keywords=programming",
        "http://www.amazon.com/Coding-Dummies-Computers-Nikhil-Abraham/dp/1118951301/ref=sr_1_16?s=books&ie=UTF8&qid=1445729423&sr=1-16&keywords=programming",
        "http://www.amazon.com/Programming-Absolute-Beginners-Guide-3rd/dp/0789751984/ref=sr_1_17?s=books&ie=UTF8&qid=1445729423&sr=1-17&keywords=programming",
        "http://www.amazon.com/Programming-JAVA-JavaScript-Coding-Guide/dp/1514844915/ref=sr_1_18?s=books&ie=UTF8&qid=1445729423&sr=1-18&keywords=programming",
        "http://www.amazon.com/Exercises-Programmers-Challenges-Develop-Coding/dp/1680501224/ref=sr_1_19?s=books&ie=UTF8&qid=1445729423&sr=1-19&keywords=programming",
        "http://www.amazon.com/Programming-Swift-Create-Fully-Function/dp/151701171X/ref=sr_1_22?s=books&ie=UTF8&qid=1445729423&sr=1-22&keywords=programming",
        "http://www.amazon.com/C-Programming-Language-4th/dp/0321563840/ref=sr_1_23?s=books&ie=UTF8&qid=1445729423&sr=1-23&keywords=programming",
        "http://www.amazon.com/Learn-Program-Scratch-Introduction-Programming/dp/1593275439/ref=sr_1_24?s=books&ie=UTF8&qid=1445729423&sr=1-24&keywords=programming",
        "http://www.amazon.com/Python-Informatics-Dr-Charles-Severance/dp/1492339245/ref=sr_1_25?s=books&ie=UTF8&qid=1445729655&sr=1-25&keywords=programming",
        "http://www.amazon.com/Practical-Programming-Strength-Training-Rippetoe/dp/0982522754/ref=sr_1_26?s=books&ie=UTF8&qid=1445729671&sr=1-26&keywords=programming",
        "http://www.amazon.com/Programming-Raspberry-Pi-Second-Getting/dp/1259587401/ref=sr_1_28?s=books&ie=UTF8&qid=1445729671&sr=1-28&keywords=programming",
        #"http://www.amazon.com/HTML5-Programming-Language-Computers-Technology-ebook/dp/B00W0GWX7K/ref=sr_1_29?s=books&ie=UTF8&qid=1445729671&sr=1-29&keywords=programming",
        "http://www.amazon.com/Elements-Programming-Interviews-Insiders-Guide/dp/1479274836/ref=sr_1_31?s=books&ie=UTF8&qid=1445729671&sr=1-31&keywords=programming",
        "http://www.amazon.com/Mathematics-Generic-Programming-Alexander-Stepanov/dp/0321942043/ref=sr_1_32?s=books&ie=UTF8&qid=1445729671&sr=1-32&keywords=programming",
        "http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/ref=sr_1_33?s=books&ie=UTF8&qid=1445729671&sr=1-33&keywords=programming",
        "http://www.amazon.com/Python-Kids-Playful-Introduction-Programming/dp/1593274076/ref=sr_1_34?s=books&ie=UTF8&qid=1445729671&sr=1-34&keywords=programming",
        "http://www.amazon.com/Programming-Absolute-Beginner-Jerry-Ford/dp/1305504437/ref=sr_1_35?s=books&ie=UTF8&qid=1445729671&sr=1-35&keywords=programming",
        "http://www.amazon.com/Programming-Arduino-Getting-Started-Sketches/dp/0071784225/ref=sr_1_36?s=books&ie=UTF8&qid=1445729671&sr=1-36&keywords=programming",
        "http://www.amazon.com/Python-Programming-Beginners-Introduction-Computer/dp/1501000861/ref=sr_1_37?s=books&ie=UTF8&qid=1445730655&sr=1-37&keywords=programming",
        "http://www.amazon.com/Beginning-Programming-Hours-Teach-Yourself/dp/0672337002/ref=sr_1_40?s=books&ie=UTF8&qid=1445730670&sr=1-40&keywords=programming",
        "http://www.amazon.com/Beginning-C-Through-Game-Programming/dp/1435457420/ref=sr_1_41?s=books&ie=UTF8&qid=1445730670&sr=1-41&keywords=programming",
        "http://www.amazon.com/Programming-Principles-Practice-Using-2nd/dp/0321992784/ref=sr_1_42?s=books&ie=UTF8&qid=1445730670&sr=1-42&keywords=programming",
        "http://www.amazon.com/Hello-World-Computer-Programming-Beginners/dp/1617290920/ref=sr_1_44?s=books&ie=UTF8&qid=1445730670&sr=1-44&keywords=programming",
        "http://www.amazon.com/Hacking-Art-Exploitation-Jon-Erickson/dp/1593271441/ref=sr_1_45?s=books&ie=UTF8&qid=1445730670&sr=1-45&keywords=programming",
        "http://www.amazon.com/Think-Like-Programmer-Introduction-Creative/dp/1593274246/ref=sr_1_46?s=books&ie=UTF8&qid=1445730670&sr=1-46&keywords=programming",
        "http://www.amazon.com/Android-Development-Programming-Guide-Learn/dp/1517640091/ref=sr_1_47?s=books&ie=UTF8&qid=1445730670&sr=1-47&keywords=programming",
        "http://www.amazon.com/Beginning-Programming-Java-Dummies-Barry/dp/1118407814/ref=sr_1_48?s=books&ie=UTF8&qid=1445730670&sr=1-48&keywords=programming",
        "http://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X/ref=sr_1_51?s=books&ie=UTF8&qid=1445730989&sr=1-51&keywords=programming",
        "http://www.amazon.com/Java-Beginners-Guide-Herbert-Schildt/dp/0071809252/ref=sr_1_52?s=books&ie=UTF8&qid=1445731007&sr=1-52&keywords=programming",
        "http://www.amazon.com/Learning-Python-5th-Mark-Lutz/dp/1449355730/ref=sr_1_53?s=books&ie=UTF8&qid=1445731007&sr=1-53&keywords=programming",
        "http://www.amazon.com/Programming-Language-Addison-Wesley-Professional-Computing/dp/0134190440/ref=sr_1_55?s=books&ie=UTF8&qid=1445731007&sr=1-55&keywords=programming",
        "http://www.amazon.com/Seven-Languages-Weeks-Programming-Programmers/dp/193435659X/ref=sr_1_57?s=books&ie=UTF8&qid=1445731007&sr=1-57&keywords=programming",
        "http://www.amazon.com/Python-Programming-Absolute-Beginner-3rd/dp/1435455002/ref=sr_1_59?s=books&ie=UTF8&qid=1445731007&sr=1-59&keywords=programming",
        "http://www.amazon.com/Beginning-C-Through-Game-Programming/dp/1305109910/ref=sr_1_61?s=books&ie=UTF8&qid=1445731183&sr=1-61&keywords=programming",
        "http://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670/ref=sr_1_63?s=books&ie=UTF8&qid=1445731696&sr=1-63&keywords=programming",
        "http://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612/ref=sr_1_64?s=books&ie=UTF8&qid=1445732025&sr=1-64&keywords=programming",
        "http://www.amazon.com/Programming-Success-Day-Beginners-Efficient/dp/1508429030/ref=sr_1_66?s=books&ie=UTF8&qid=1445732067&sr=1-66&keywords=programming",
        "http://www.amazon.com/Head-First-Java-Kathy-Sierra/dp/0596009208/ref=sr_1_68?s=books&ie=UTF8&qid=1445732067&sr=1-68&keywords=programming",
        "http://www.amazon.com/Programming-C-4th-Developers-Library/dp/0321776410/ref=sr_1_71?s=books&ie=UTF8&qid=1445732067&sr=1-71&keywords=programming",
        "http://www.amazon.com/Programming-Arduino-Next-Steps-Sketches/dp/0071830251/ref=sr_1_74?s=books&ie=UTF8&qid=1445732253&sr=1-74&keywords=programming",
        "http://www.amazon.com/Android-Programming-Day-Power-Beginners/dp/1507893744/ref=sr_1_76?s=books&ie=UTF8&qid=1445732274&sr=1-76&keywords=programming",
        "http://www.amazon.com/Introduction-Algorithms-3rd-Thomas-Cormen/dp/0262033844/ref=sr_1_77?s=books&ie=UTF8&qid=1445732274&sr=1-77&keywords=programming",
        "http://www.amazon.com/iOS-Programming-Fundamentals-Swift-Basics/dp/1491936770/ref=sr_1_80?s=books&ie=UTF8&qid=1445732274&sr=1-80&keywords=programming",
        "http://www.amazon.com/Coders-Work-Reflections-Craft-Programming/dp/1430219483/ref=sr_1_82?s=books&ie=UTF8&qid=1445732274&sr=1-82&keywords=programming",
        "http://www.amazon.com/Linux-Programming-Interface-System-Handbook/dp/1593272200/ref=sr_1_83?s=books&ie=UTF8&qid=1445732274&sr=1-83&keywords=programming"  
        ]
   return websites