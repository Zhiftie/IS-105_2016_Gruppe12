import numpy as np
import matplotlib.pyplot as plt
import timeit

def makeHaystack(listname,size): #max size: 536 870 912
    listname = []
    for i in xrange(0,size):
        listname.append(i)
    return listname

def setNeedleStart():
    start = haystack[100]
    return start

def setNeedleMiddle():
    middle = (len(haystack)/2)
    return haystack[middle]

def setNeedleEnd():
    end = (len(haystack)-1)
    return haystack[end]

def splitL(lS):
    x_val, y_val = zip(*lS)
    return x_val, y_val

def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False

def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value

def Search_s():
    return search_slow(haystack, needle)

def Search_f():
    return search_fast(haystack, needle)
   
def testS(needleMethod):
    global needle
    needle = needleMethod()
    sSlow = []
    while len(haystack) <= 10000000: 
        timer = timeit.Timer(Search_s)
        result = timer.repeat(repeat = 1, number = 100)        
        sSlow.append((len(haystack), min(result)))
        makeHaystack(1000000)
        needle = needleMethod()
    return sSlow

def testF(needleMethod):
    global needle
    sFast = []
    needle = needleMethod()
    while len(haystack) <= 10000000:
        timer = timeit.Timer(Search_f)
        result = timer.repeat(repeat = 1, number = 100)
        sFast.append((len(haystack),min(result)))
        makeHaystack(1000000)
        needle = needleMethod() #
    return sFast
haystack = []
makeHaystack(1000000)
needle = None

fList = testF(setNeedleStart)
needle = None
x , y = splitL(fList)




        
        
    