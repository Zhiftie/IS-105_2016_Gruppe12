import scipy as sp
from random import shuffle
import numpy as np
ln = 10000 # lenght of list used in longLnShiffle function
haystack = []
var1 = 2
var2 = 9
needle = 123
needleFound = False
def make2dlist():
    list1 = np.arange(100).reshape(2,50)
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
    for item in haustack:
        if item == needle:
            return True
    return False

def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value

haystack = shufflelist()
needleI = findNeedle(needle)

print "needle=",haystack[needleI],",found at index number",needleI