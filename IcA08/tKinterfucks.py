# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk() #lager et blankt vindu.


def printName():
    print "Hello, my name is martin"
    
    
button_1 = Button(root, text="Print my name", command=printName) #binder knappen til funksjonen printName

button_1.pack()

    
root.mainloop()