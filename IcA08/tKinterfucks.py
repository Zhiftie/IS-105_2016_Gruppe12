# -*- coding: utf-8 -*-
from Tkinter import *


class MartinsKnapper:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(frame, text="quit", command=frame.quit) #Avslutter mainloop - aka lukker vinduet
        self.quitButton.pack(side=LEFT)
        
    def printMessage(self):
        print "wow, it worked!"
        






root = Tk() #lager et blankt vindu.
m = MartinsKnapper(root)
root.mainloop()