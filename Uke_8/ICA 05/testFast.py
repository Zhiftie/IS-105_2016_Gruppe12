import numpy as np
import matplotlib.pyplot as plt
import timeit
import csv

def makeHaystack(size): #max size: 536 870 912
    for i in xrange(0,size):
        haystack.append(i)
    return haystack

def setNeedleStart():
    start = haystack[100]
    return start

def setNeedleMiddle():
    return haystack[(len(haystack)//2)] 

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
    needle = needleMethod()
    sFast = []
    while len(haystack) <= 10000000: #max size of haystack
        timer = timeit.Timer(Search_f)
        result = timer.repeat(repeat = 10, number = 1)        
        sFast.append((len(haystack), min(result)))
        for i in xrange(len(haystack),(len(haystack)*2)): 
            haystack.append(i)
        needle = needleMethod() #moves needle to the same relative position in the extended haystack
    return sFast

def createFile(filename): 
    with open(filename,'w') as f:
        writer = csv.writer(f, delimiter = ",")  
        writer.writerows(zip(x,y))

haystack = []
makeHaystack(100000) # initial size of haystack
needle = None

fList = testF(setNeedleStart)# where to put the needle. 
x , y = splitL(fList)
createFile('test1.csv') # descriptive name of the created file