from Tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()

w.create_rectangle(200, 1000, 750, 0,  fill="blue")
w.create_rectangle(200, 1000, 0, 0, fill="green")
w.create_rectangle(1000, 0, 750, 800, fill="green")
#w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the left side.
w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the right side.

w.create_oval(850, 400, 800, 350, fill="yellow") # Chicken on the right side.
w.create_oval(860, 450, 900, 350, fill="white") # Grain on the right side.
w.create_oval(550, 300, 750, 250, fill="black") # Man in the boat on the right side.
w.create_oval(900, 300, 850, 330, fill="orange") # Fox on the right side.

mainloop()