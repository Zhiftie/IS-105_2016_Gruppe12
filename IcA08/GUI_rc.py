# -*- coding: utf-8 -*-
from Tkinter import *
from tape import *
from state import State



class RiverCrossing:
    def __init__(self, master):
        self.tape = Tape()
        self.state = State()
        
        master.title("River Crossing")
        w = Canvas(master, width=900, height=900)
        w.pack()
        
        w.create_rectangle(200, 900, 750, 0,  fill="blue")
        w.create_rectangle(200, 900, 0, 0, fill="green")
        w.create_rectangle(900, 0, 750, 800, fill="green")
        #Lager landskapet(water, left, right)
        
        global boat 
        boat = w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat = L
        global chicken
        chicken = w.create_oval(150, 180, 180, 200, fill="yellow") # Chicken = L
        global grain 
        grain = w.create_oval(130, 180, 160, 170, fill="white") # Grain = L
        global man 
        man = w.create_oval(150, 250, 180, 200, fill="black") # Man = L 
        global fox 
        fox = w.create_oval(100, 130, 180, 150, fill="orange") # Fox = L 
        
        #Setter alle items på venstre side
        
        bottomFrame = Frame(master)
        bottomFrame.pack(side=BOTTOM)
        
        #eget området nederst i vinduet tilegnet interaktive knapper
        
        helpFrame = Frame(master)
        helpFrame.pack(side=RIGHT)
        
        def manGetX():
            if self.state.tape.man in 'left' or self.state.tape.man in 'right':
                if self.state.tape.man in 'left':
                    w.coords(man, 350, 250, 205, 210) #man in boat at left
                elif self.state.tape.man in 'right':
                    w.coords(man, 550, 250, 705, 215) #man in boat at right
                self.state.tape.set_man('boat') #sets the new position of the man in tape. 
            
            elif self.state.tape.man in 'boat' and self.state.tape.boat in 'left': 
                w.coords(man, 150, 250, 180, 200)
                self.state.tape.set_man('left')
            elif self.state.tape.man in 'boat' and self.state.tape.boat in 'right':
                w.coords(man, 850, 250, 760, 210)
                self.state.tape.set_man('right')
        
        
        
        def crossRiver():
            if self.state.tape.man in 'boat':
                if self.state.tape.boat in 'left': 
                    w.coords(boat, 550, 300, 750, 200)
                    w.coords(man, 550, 300, 750, 250)
                    self.state.tape.set_boat('right')
                    
                elif self.state.tape.boat in 'right':
                    w.coords(boat, 400, 300, 201, 200)
                    w.coords(man, 350, 250, 205, 210)
                    self.state.tape.set_boat('left')
                
                
                
                
        
        getIn = Button(bottomFrame, text="Get in or out of the boat", bg="white", fg="black", command=manGetX)
        putinC = Button(bottomFrame, text="Put chicken in boat", bg="white", fg="black")
        putinF = Button(bottomFrame, text="Put fox in boat", bg="white", fg="black")
        putinG = Button(bottomFrame, text="Put grain in boat", bg="white", fg="black")
        takeOutC = Button(bottomFrame, text="Take chicken out of boat", bg="white", fg="black")
        takeOutF = Button(bottomFrame, text="Take fox out of boat", bg="white", fg="black")
        takeOutG = Button(bottomFrame, text="Take grain out of boat", bg="white", fg="black")
        crossRiver = Button(bottomFrame, text="Cross River", bg="black", fg="white", command=crossRiver) 
                                                                                                                      
        help = Button(helpFrame, text="Help", bg="white", fg="red")
        quit = Button(helpFrame, text="Quit game", bg= "black", fg="red", command=w.quit)
        
        getIn.grid(row=0) 
        putinC.grid(row=0, column=2)
        putinF.grid(row=0, column=4)
        putinG.grid(row=0, column=5)
        takeOutC.grid(row=1)
        takeOutF.grid(row=1, column=2)
        takeOutG.grid(row=1, column=5)
        crossRiver.grid(row=2, column=2)
        
        help.pack()
        quit.pack(fill=X)
        
        
        

#Plasserer knappene

root = Tk()
rc = RiverCrossing(root)
root.mainloop()