import csv
import numpy as np
import matplotlib.pyplot as plt

with open("text.csv") as f:
    data = f.read()

data = data.split('\n')

x = [row.split('\t')[0] for row in data]
y = [row.split('\t')[1] for row in data]
print x
print y

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title...")    
ax1.set_xlabel('your x label..')
ax1.set_ylabel('your y label...')

ax1.plot(x,y, c='r', label='the data')

leg = ax1.legend()

plt.show()