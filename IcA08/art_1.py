from Tkinter import *

def tilstand_1():
    master = Tk()
    
    w = Canvas(master, width=1000, height=1000)
    w.pack()
    
    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat = L
    
    
    w.create_oval(220, 220, 250, 280, fill="yellow") # Chicken in boat at L
    w.create_oval(130, 180, 160, 170, fill="white") # Grain = L 
    w.create_oval(150, 250, 180, 200, fill="black") # Man = L 
    w.create_oval(100, 130, 180, 150, fill="orange") # Fox = L
    
    mainloop()    

def tilstand_2():
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
    w.create_oval(350, 250, 205, 210, fill="black") # Man in the boat on the right side.
    w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the right side.
    
    mainloop()
    
def tilstand_3():
    master = Tk()
    
    w = Canvas(master, width=1000, height=1000)
    w.pack()
    
    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the right side.
    #w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the left side.
    
    w.create_oval(150, 180, 180, 200, fill="yellow") # Chicken on the right side.
    w.create_oval(130, 180, 160, 170, fill="white") # Grain on the right side.
    w.create_oval(150, 250, 180, 200, fill="black") # Man in the boat on the right side.
    w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the right side.
    
    mainloop()    

def tilstand_4():
    master = Tk()
    
    w = Canvas(master, width=1000, height=1000)
    w.pack()
    
    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    #w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the left side.
    w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the right side.
    
    w.create_oval(550, 225, 700, 200, fill="yellow") # Chicken in the boat on the right side
    w.create_oval(130, 180, 160, 170, fill="white") # Grain on the left side.
    w.create_oval(550, 250, 705, 215,  fill="black") # Man in the boat on the right side 
    w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the left side.
    
    mainloop()
    
def tilstand_5():
    master = Tk()
    
    w = Canvas(master, width=1000, height=1000)
    w.pack()
    
    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    #w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the right side.
    w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the left side.
    
    w.create_oval(150, 180, 180, 200, fill="yellow") # Chicken on the right side.
    w.create_oval(800, 190, 760, 170, fill="white") # Grain on the right side.
    w.create_oval(850, 250, 760, 210, fill="black") # Man in the boat on the right side.
    w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the right side.
    
    mainloop()    
    
def tilstand_6():
    master = Tk()
    
    w = Canvas(master, width=1000, height=1000)
    w.pack()
    
    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    #w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the left side.
    w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the right side.
    
    w.create_oval(150, 180, 180, 200, fill="yellow") # Chicken on the left side.
    w.create_oval(130, 180, 160, 170, fill="white") # Grain on the left side.
    w.create_oval(550, 250, 705, 215,  fill="black") # Man in the boat on the right side 
    w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the left side.
    
    mainloop()
    
def tilstand_7():
    master = Tk()

    w = Canvas(master, width=1000, height=1000)
    w.pack()

    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the right side.

    w.create_oval(850, 400, 800, 350, fill="yellow") # Chicken on the right side.
    w.create_oval(860, 450, 900, 350, fill="white") # Grain on the right side.
    w.create_oval(550, 300, 750, 250, fill="black") # Man in the boat on the right side.
    w.create_oval(550, 250, 700, 220, fill="orange") # Fox on the right side.

    mainloop()

def tilstand_8():
    master = Tk()

    w = Canvas(master, width=1000, height=1000)
    w.pack()

    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    w.create_rectangle(550, 300, 750, 200, fill="brown") # Boat on the right side.

    w.create_oval(850, 400, 800, 350, fill="yellow") # Chicken on the right side.
    w.create_oval(860, 450, 900, 350, fill="white") # Grain on the right side.
    w.create_oval(550, 300, 750, 250, fill="black") # Man in the boat on the right side.
    w.create_oval(900, 300, 850, 330, fill="orange") # Fox on the right side.

    mainloop()
    
def tilstand_9():
    master = Tk()

    w = Canvas(master, width=1000, height=1000)
    w.pack()

    w.create_rectangle(200, 1000, 750, 0,  fill="blue")
    w.create_rectangle(200, 1000, 0, 0, fill="green")
    w.create_rectangle(1000, 0, 750, 800, fill="green")
    w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the left side.

    w.create_oval(150, 180, 180, 200, fill="yellow") # Chicken on the right side.
    w.create_oval(130, 180, 160, 170, fill="white") # Grain on the left side.
    w.create_oval(350, 250, 205, 210, fill="black") # Man in the boat on the left side.
    w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the left side.

    mainloop()