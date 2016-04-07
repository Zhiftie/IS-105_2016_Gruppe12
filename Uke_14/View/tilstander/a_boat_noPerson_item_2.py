from Tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()

w.create_rectangle(200, 1000, 750, 0,  fill="blue")
w.create_rectangle(200, 1000, 0, 0, fill="green")
w.create_rectangle(1000, 0, 750, 800, fill="green")
w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the right side.
#w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the left side.

w.create_oval(220, 220, 250, 280, fill="yellow") # Chicken on the right side.
w.create_oval(130, 180, 160, 170, fill="white") # Grain on the right side.
w.create_oval(150, 250, 180, 200, fill="black") # Man in the boat on the right side.
w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the right side.

mainloop()



# nr4 flytter oppover

#nr 3 flytter til høyre
