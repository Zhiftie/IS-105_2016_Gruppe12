import re
import csv
import matplotlib.pyplot as plt

def getCoordinates(filename):
    with open(filename, "rb") as f:
        r = csv.reader(f)
        rawData = map(tuple, r)
        x , y = zip(*rawData) 
        xInt = []
        yFloat = []
        for i in xrange(len(x)):
            xInt.append(int(x[i]))
        
        for i in xrange(len(y)):
            yFloat.append(float(y[i]))
        
    return xInt, yFloat


def plotGraph(filename):# specify name of file to get plot points
    x, y = getCoordinates(filename)
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.xscale("log")
    plt.autoscale()
    plt.grid()
    plt.show()

def plotMulti(file1,file2,file3,file4,file5,file6, title): 
    files = [file1,file2,file3,file4,file5,file6]
    graphs = []
    for item in files:
        graphs.append(item)
    for filename in graphs:
        name = re.findall('[A-Z][^A-Z]*', filename)
        x ,y = getCoordinates(filename)
        line = plt.plot(x, y, label = name[0] + " " + name[1]) , plt.scatter(x, y)
    plt.xlabel("Size of List")
    plt.ylabel("Time")
    plt.title(title)
    plt.grid()
    plt.autoscale()
    plt.xscale("log")
    plt.legend()
    plt.show()
"""
plotMulti("AskeFast.csv", "EspenFast.csv", "LaddenFast.csv", "PerFast.csv", "TomSlow.csv",
          "SindreSlow.csv", "Fast Method Needle Start")
"""
def getTitle(string):
    title = string[:-4]
    title = re.findall('[A-Z][^A-Z]*', title)
    title = title[2]
    return title

def plotMulti2(*arg): #
    files = arg
    for filename in files:
        name = re.findall('[A-Z][^A-Z]*', filename)
        x ,y = getCoordinates(filename)
        line = plt.plot(x, y, label = name[0] + " " + name[1]) , plt.scatter(x, y)
    plt.xlabel("Size of List")
    plt.ylabel("Time")
    plt.title("Needle Position" +  ": " + getTitle(files[0]))
    plt.grid()
    plt.autoscale()
    plt.xscale("log")
    plt.legend()
    plt.show()

plotMulti2("SindreFastStart.csv", "SindreFastStart2.csv")