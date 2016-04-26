from random import shuffle


var1 = 2
var2 = 9  
needleFound = False
haystack = []
def make2dlist():
    list1 = np.arange(100).reshape(2,50)
def makeHaystack(size): #max size: 536 870 912
    for i in range(0,size):
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
   

sSlow = []
sFast = []
haystack = makeHaystack(10000000)  #max size: 536 870 912  
needle = setNeedleStart()
print len(haystack)
if __name__ == "__main__":
    """
    timeit test for the search slow function
    """
    import timeit
    global sSlow
    global sFast
    timer = timeit.Timer(Search_s)
    result = timer.repeat(repeat = 10, number = 1)
    sSlow = result
    print ("{:8.6f}".format(min(result)))
    timer = timeit.Timer(Search_f)
    result = timer.repeat(repeat = 10, number = 1)
    sFast = result
    print ("{:8.6f}".format(min(result)))
    
print sSlow
#if __name__ == '__main__':
    #import timeit
    #print(timeit.timeit("findNeedle(needle)", setup="from__main__ import findNeedle, needle"))