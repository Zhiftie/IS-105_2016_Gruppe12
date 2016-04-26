import numpy as np
import matplotlib.pyplot as plt
import timeit

def make2dlist():
    list1 = np.arange(100).reshape(2,50)
def makeHaystack(size): #max size: 536 870 912
    haystack =  []
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
    end = (len(haystack)-140)
    return haystack[end]
    
    
"""
Iterates over a list looking for an item with the x value, once its found it returns the index number
"""
def findNeedle(needle):
    for i in[i for i, v in enumerate(haystack) if v == needle ]:
        return i
    
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

#haystack = shufflelist()
#needleI = findNeedle(needle)



def Search_s():
    return search_slow(haystack, needle)

def Search_f():
    return search_fast(haystack, needle)
   
  
haystack = makeHaystack(10000)
needle = setNeedleStart()

#if __name__ == "__main__":
    #"""
    #timeit test for the search slow function
    #"""
def testS():
    sSlow = []
    haystack = makeHaystack(10000)
    needle = setNeedleStart()
    while len(haystack) <= 1000000: #haystack resettes ikke. Fix
        timer = timeit.Timer(Search_s)
        result = timer.repeat(repeat = 1, number = 10)        
        sSlow.append((len(haystack),min(result)))
        makeHaystack(int(len(haystack)+10000))
    return sSlow

def testF():
    sFast = []
    haystack = makeHaystack(10000)
    needle = setNeedleStart()
    while len(haystack) <= 1000000:
        timer = timeit.Timer(Search_f)
        result = timer.repeat(repeat = 1, number = 10)
        sFast.append((len(haystack),min(result)))
        makeHaystack(int(len(haystack)+10000))
    return sFast
        
    
fList = testF()
sList = testS()

def graph(l1):
    plt.plot(l1)
    plt.show()
    
graph(fList)
graph(sList)
        
        
    