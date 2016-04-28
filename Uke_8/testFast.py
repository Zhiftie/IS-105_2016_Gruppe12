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
    return haystack[(len(haystack)//2)] # Lager problemer når needle > 100k

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
    while len(haystack) <= 10000000: 
        timer = timeit.Timer(Search_f)
        result = timer.repeat(repeat = 1, number = 1)        
        sFast.append((len(haystack), min(result)))
        for i in xrange(len(haystack),(len(haystack)+100000)):#
            haystack.append(i)
        needle = needleMethod() #setter needle på samme plass som tidligere i den nå utvidede listen.
    return sFast
"""
skriv resultatet til fil. må utbedres
"""
def writetofile(name):
    fname = name +".csv"
    with open(fname, 'w') as f: #Sett "text.csv" til et beskrivende navn" 
        writer = csv.writer(f, delimiter='\t')  
        writer.writerows(zip(x,y))

haystack = []
makeHaystack(100000)
needle = None

fList = testF(setNeedleStart)
x , y = splitL(fList)
writetofile(raw_input("Name file> "))

plt.scatter(x,y)
plt.plot(x,y)
plt.xscale("log")
plt.autoscale()
plt.grid()
plt.show()

