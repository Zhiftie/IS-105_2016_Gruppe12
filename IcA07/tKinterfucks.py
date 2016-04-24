from Tkinter import *

root = Tk() #lager et blankt vindu.


topFrame = Frame(root) #usynlig frame
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) #layers

button1 = Button(topFrame, text="button1", fg="red") #@param: variabel, innhold, farge.
button2 = Button(topFrame, text="button1", fg="green") #@param: variabel, innhold, farge.
button3 = Button(topFrame, text="button1", fg="purple") #@param: variabel, innhold, farge.
button4 = Button(bottomFrame, text="nope", fg="red") #@param: variabel, innhold, farge.


button1.pack(side=LEFT, fill=X) #skalerer med vinduet
button2.pack(side=LEFT)
button3.pack()
button4.pack()
root.mainloop()