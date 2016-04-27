import numpy as np
import matplotlib.pyplot as plt
import timeit

def makeHaystack(size): #max size: 536 870 912
    for i in xrange(0,size):
        haystack.append(i)
    return haystack

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

def Search_f():
    return search_fast(haystack, needle)

def testF(needleMethod):
    global needle
    sFast = []
    needle = needleMethod()
    while len(haystack) <= 1000000:
        timer = timeit.Timer(Search_f)
        result = timer.repeat(number = 100)
        sFast.append((len(haystack),min(result)))
        print sFast[(len(sFast)-1)]
        makeHaystack(100000)
        needle = needleMethod() 
    return sFast

haystack = []
makeHaystack(100000)
needle = None

fList = testF(setNeedleMiddle)
x , y = splitL(fList)

plt.scatter(x,y)
plt.plot(x,y)
plt.xscale("log")
plt.autoscale()
plt.grid()
plt.show()