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

x , y = getCoordinates("text.csv") # specify name of file to get plot points

plt.scatter(x,y)
plt.plot(x,y)
plt.xscale("log")
plt.autoscale()
plt.grid()
plt.show()
