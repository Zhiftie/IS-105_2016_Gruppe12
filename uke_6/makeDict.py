# -*- code utf-8 -*-
testString = "1234567 891012 345 6 78910"

def makeDict(string):
    """
    Generere en dictionary med alle de unike symbolene fra testString
    """
    stringDict = {}
    stringlen = len(testString)
    byte = ""
    it = 0
    while stringlen>it:
        for letter in string:
            symbol = letter
            if symbol not in stringDict.values():
                it += 1
                stringDict.update({it:symbol})
                byte = symbol
            
            elif symbol in stringDict.values():
                it += 1   
    return stringDict
            
            
        
makeDict(testString)
print makeDict(testString)