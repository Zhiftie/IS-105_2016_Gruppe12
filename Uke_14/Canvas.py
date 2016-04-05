from Tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()

w.create_rectangle(200, 1000, 750, 0,  fill="blue")
w.create_rectangle(200, 1000, 0, 0, fill="green")
w.create_rectangle(0, 0, 0, 0, fill="green")

mainloop()