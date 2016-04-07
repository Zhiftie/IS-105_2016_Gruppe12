from Tkinter import *


class Canvas(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        Tk()
        self.entrythingy = Entry()
        self.entrythingy.pack()
        
        self.contens = StringVar()
        self.contens.set("heiheiheikaffesnas")
        self.entrythingy["textvariable"] = self.contens
        
        self.entrything.bind('<Key-Return>',
                             self.print_contens)
    
    def print_contens(self, event):
        print "hi. contens of entry is now --->", \
              self.contens.get()
canv1 = Canvas(Frame)
canv1.print_contens(event)
#master = Tk()
#Tk()
#w = Canvas(master, width=1000, height=1000)
#w.pack()

#w.create_rectangle(200, 1000, 750, 0,  fill="blue")
#w.create_rectangle(200, 1000, 0, 0, fill="green")
#w.create_rectangle(1000, 0, 750, 800, fill="green")
#w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the right side.
#w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the left side.

#w.create_oval(150, 180, 180, 200, fill="yellow") # Chicken on the right side.
#w.create_oval(130, 180, 160, 170, fill="white") # Grain on the right side.
#w.create_oval(350, 250, 205, 210, fill="black") # Man in the boat on the right side.
#w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the right side.

#mainloop()