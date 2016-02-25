from random import shuffle

ln = 100 # length of list used in shufflelist function
haystack = []
var1 = 2
var2 = 9
needle = len(haystack)/2
needleFound = False
#def make2dlist():
  #  list1 = np.arange(100).reshape(2,50)
    
def makeStringList(haystack):
    strHaystack = []
    for i in haystack:
        stringList = ""
        stringList+=str(i)
        strHaystack.append(stringList)
    return strHaystack

def shufflelist():
    for i in range(0,ln):
        haystack.append(i)
    shuffle(haystack)
    return haystack


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
    shuffle(haystack)
    return False

def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    shuffle(haystack)
    return return_value

haystack = shufflelist()
needleI = findNeedle(needle)
strHaystack = makeStringList(haystack)
print "needle=",haystack[needleI],",found at index number",needleI



def Search_s():
    return search_slow(haystack, needle)

def Search_f():
    return search_fast(haystack, needle)
   
    
#if __name__ == "__main__":
    #"""
    #timeit test for the search slow function
    #"""
    #import timeit
    #timer = timeit.Timer(Search_s)
    #result = timer.repeat(repeat = 100, number = 10)
    #print ("{:8.6f}".format(min(result)))
    #timer = timeit.Timer(Search_f)
    #result = timer.repeat(repeat = 100, number = 10)
    #print ("{:8.6f}".format(min(result)))
#if __name__ == '__main__':
    #import timeit
    #print(timeit.timeit("findNeedle(needle)", setup="from__main__ import findNeedle, needle"))