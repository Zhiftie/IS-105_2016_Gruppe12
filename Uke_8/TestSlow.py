import numpy as np
import matplotlib.pyplot as plt
import timeit

def makeHaystack(size): #max size: 536 870 912
    for i in xrange(0,size):
        haystack.append(i)
    return haystack

def setNeedleStart():
    start = haystack[1]
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

def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value

def Search_s():
    return search_slow(haystack, needle)
   
def testS(needleMethod):
    global needle
    needle = needleMethod()
    sSlow = []
    while len(haystack) <= 10000000:
        timer = timeit.Timer(Search_s)
        result = timer.repeat(repeat = 1, number = 1)        
        sSlow.append((len(haystack), min(result)))
        for i in xrange(len(haystack),(len(haystack)*2)): #dobbler størrelsen på liste
            haystack.append(i) 
        needle = needleMethod() #setter needle på samme plass som tidligere i den nå utvidede listen.
    return sSlow

haystack = []
makeHaystack(100000)
needle = None

sList = testS(setNeedleMiddle)
x , y = splitL(sList)

plt.scatter(x,y)
plt.plot(x,y)
plt.xscale("log")
plt.autoscale()
plt.grid()
plt.show()