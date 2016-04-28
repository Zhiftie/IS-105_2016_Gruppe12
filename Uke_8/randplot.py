import csv
import matplotlib.pyplot as plt

def readFile(filename):
    fp = open(filename)
    tupList = []
    for line in fp:
        tupList.append(tuple(line.strip('',).split('\t')))
    fp.close()
    return tupList

def refineL(listN):
    for item in listN:
        for item[0] in listN:
            item[0] = int(item[0])
        for item[1] in listN:
            item[1] = float(item[1])
        return listN
            
            

splitL = readFile("needleStart.csv")
#newsplitL = refineL(splitL)
print splitL
        