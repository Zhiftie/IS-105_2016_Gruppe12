from Tkinter import *


root = Tk()
root.title("Do you want to go outside of the boat? or do you want to travel?: type 1, to go out "
                               "type 2 to travel")

myvar = StringVar()

def mywarWritten(*args):
    print myvar.get()

myvar.trace("w", mywarWritten)

label = Label(root, textvariable=myvar)
label.pack()

text_entry = Entry(root, textvariable=myvar)
text_entry.pack()

root.mainloop()