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

def getTitle(string): 
    title = string[:-4]
    title = re.findall('[A-Z][^A-Z]*', title)
    title = title[2]
    return title

def plotMultiple(*arg): #plot csv files passed in parameter
    files = arg
    for filename in files:
        name = re.findall('[A-Z][^A-Z]*', filename)
        np = name[1] + " "+ name[2][:-4]
        x ,y = getCoordinates(filename)
        line = plt.plot(x, y, label = name[0] + " " + (np)) , plt.scatter(x, y)
    plt.xlabel("Size of List")
    plt.ylabel("Time")
    plt.title("Needle Position" +  ": " + getTitle(files[0]))
    plt.grid()
    plt.autoscale()
    plt.xscale("log")
    plt.legend(bbox_to_anchor=(1.0, 1), loc=2, borderaxespad=0.)
    plt.show()

"""
plotMultiple("SindreFastStart.csv", "ThomasFastStart.csv", "MartinFastStart.csv", #Compares fast and slow with needle at the start
            "SindreSlowStart.csv", "ThomasSlowStart.csv", "MartinSlowStart.csv")
"""

"""
plotMultiple("SindreFastMiddle.csv", "MartinFastMiddle.csv", "GuroFastMiddle.csv", #Compares fast and slow with needle in the middle
             "SindreSlowMiddle.csv", "MartinSlowMiddle.csv", "GuroSlowMiddle.csv")
"""
"""
plotMultiple("SindreFastEnd.csv", "ThomasFastEnd.csv", "MartinFastEnd.csv", #Compares fast and slow with needle at the end
             "SindreSlowEnd.csv", "ThomasSlowEnd.csv", "MartinSlowEnd.csv")
"""
"""
plotMultiple("GuroSlowStart.csv", "MartinSlowStart.csv", "SindreSlowStart.csv",#Compares slow method with needle at the start and at the end
             "GuroSlowEnd.csv", "MartinSlowEnd.csv", "SindreSlowEnd.csv")
"""