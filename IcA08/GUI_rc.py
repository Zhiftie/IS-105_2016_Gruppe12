# -*- coding: utf-8 -*-
"""

Source: GR 2 https://github.com/Cmoen11/IS-105_2016_Gruppe-2-/blob/master/uke14_oppgaver/New_Art.py#L93
Most of the game's functionality, tape, state is imported from this ^ source. The GUI itself is created by us.
"""

from Tkinter import *
from tape import *
from state import *




class RiverCrossing:
    def __init__(self, master):
        self.tape = Tape()
        self.state = State()
        
        master.title("River Crossing")
        global w
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
        
        
        """
        Forsøk på å implementere "conditions" for hva som utløser game over.
        """
        #def isItDead(self):
            #while (self.state.check_lose_combo()):  
                #master.title("Game over")
                #global w
                #w = w.delete(ALL) #Removes all items. 
                #w = Label(master, text="R.I.P M8.")
                #w.pack()        
                
        
        def manGetX():
            if self.state.tape.man in 'left' or self.state.tape.man in 'right':
                if self.state.tape.man in 'left':
                    w.coords(man, 350, 250, 205, 210) #man in boat at left
                elif self.state.tape.man in 'right':
                    w.coords(man, 550, 250, 705, 215) #man in boat at right
                self.state.tape.set_man('boat') #sets the new position of the man in tape. 
                
            # below is the code for taking the man out of the boat
            elif self.state.tape.man in 'boat' and self.state.tape.boat in 'left': 
                w.coords(man, 150, 250, 180, 200) 
                self.state.tape.set_man('left')
            elif self.state.tape.man in 'boat' and self.state.tape.boat in 'right':
                w.coords(man, 850, 250, 760, 210)
                self.state.tape.set_man('right')
            #isItDead(self)
            
        
        def putInc():
            while (self.state.tape.grain in 'boat' \
                  or self.state.tape.fox in 'boat' \
                  or self.state.tape.man in 'boat'):
                #global w
                #w = Label(master, text ="boat is full!") #must add timer to get rid of the label.
                return None
            if self.state.tape.boat in 'left' or self.state.tape.boat in 'right':
                if self.state.tape.chicken in 'left':
                    w.coords(chicken, 220, 220, 250, 280)
                    self.state.tape.set_chicken('boat') #chicken in boat at left
                elif self.state.tape.chicken in 'right':
                    w.coords(chicken, 550, 225, 700, 200)
                    self.state.tape.set_chicken('boat') #chicken at right            
                    
        def takeOutC():
            if self.state.tape.chicken in 'boat' and self.state.tape.boat in 'left':
                w.coords(chicken, 150, 180, 180, 200)
                self.state.tape.set_chicken('left') #moves chicken to left land
            elif self.state.tape.chicken in 'boat' and self.state.tape.boat in 'right':
                w.coords(chicken, 850, 400, 800, 350)
                self.state.tape.set_chicken('right') #moves chicken to right land
                
        
                    
                
        def putInF():
            while (self.state.tape.grain in 'boat' \
                    or self.state.tape.chicken in 'boat' \
                    or self.state.tape.man in 'boat'):
                return None
            if self.state.tape.boat in 'left' or self.state.tape.boat in 'right':
                if self.state.tape.fox in 'left':
                    w.coords(fox, 213, 222, 250, 280)
                    self.state.tape.set_fox('boat') # fox in boat at left
                elif self.state.tape.fox in 'right':
                    w.coords(fox, 550, 250, 700, 220)
                    self.state.tape.set_fox('boat') #fox in boat at right
                    
        def takeOutF():
            if self.state.tape.fox in 'boat' and self.tape.boat in 'left':
                w.coords(fox, 100, 130, 180, 150)
                self.state.tape.set_fox('left') #sets fox back at left land
                
            elif self.state.tape.fox in 'boat' and self.state.tape.boat in 'right':
                w.coords(fox, 850, 400, 800, 350)
                self.state.tape.set_fox('right') #sets fox to right land
                #bugged - will set fox back to start position(left land)
                
                
                
        
        def putInG():
            while (self.state.tape.fox in 'boat' \
                    or self.state.tape.chicken in 'boat' \
                    or self.state.tape.man in 'boat'):
                return None
            if self.state.tape.boat in 'left' or self.state.tape.boat in 'right':
                if self.state.tape.grain in 'left':
                    w.coords(grain, 213, 222, 250, 280)
                    self.state.tape.set_grain('boat') #grain in boat at left
                elif self.state.tape.grain in 'right':
                    w.coords(grain, 550, 250, 700, 220) 
                    self.state.tape.set_grain('boat') #grain in boat at right
            
        def takeOutG():
            if self.state.tape.grain in 'boat' and self.state.tape.boat in 'left':
                w.coords(grain, 130, 180, 160, 170)
                self.state.tape.set_grain('left') #Grain at left land
            elif self.state.tape.grain in 'boat' and self.state.tape.boat in 'right':
                w.coords(grain, 850, 400, 800, 350)
                self.state.tape.set_grain('right') #grain at right land
                
                
            
                
                
            
        
            
                    
                    
                  
                      
               
              
                    
        
        def crossRiver():
            if self.state.tape.man in 'boat':
                if self.state.tape.boat in 'left': 
                    w.coords(boat, 550, 300, 750, 200)
                    w.coords(man, 550, 300, 750, 250)
                    self.state.tape.set_boat('right')
                    if self.state.tape.chicken in 'boat':
                        w.coords(chicken, 550, 225, 700, 200)
                    elif self.state.tape.fox in 'boat':
                        w.coords(fox, 550, 250, 700, 220)
                    elif self.state.tape.grain in 'boat':
                        w.coords(grain, 550, 250, 700, 220)
                        
                        
                    
                elif self.state.tape.boat in 'right':
                    w.coords(boat, 400, 300, 201, 200)
                    w.coords(man, 350, 250, 205, 210)
                    self.state.tape.set_boat('left')
                    if self.state.tape.chicken in 'boat':
                        w.coords(chicken, 220, 220, 250, 280)
                    elif self.state.tape.fox in 'boat':
                        w.coords(fox, 213, 222, 250, 280)
                    elif self.state.tape.grain in 'boat':
                        w.coords(grain, 213, 222, 250, 280)

                    
            #isItDead(self) 
                
                
        
            
                
            
        #PIx = Put in x 
        #TOx = Take out x
        
        getIn = Button(bottomFrame, text="Get in or out of the boat", bg="white", fg="black", command=manGetX)
        PIC = Button(bottomFrame, text="Put chicken in boat", bg="white", fg="black", command=putInc)
        PIF = Button(bottomFrame, text="Put fox in boat", bg="white", fg="black", command=putInF)
        PIG = Button(bottomFrame, text="Put grain in boat", bg="white", fg="black", command=putInG)
        TOC = Button(bottomFrame, text="Take chicken out of boat", bg="white", fg="black",command=takeOutC)
        TOF = Button(bottomFrame, text="Take fox out of boat", bg="white", fg="black", command=takeOutF)
        TOG = Button(bottomFrame, text="Take grain out of boat", bg="white", fg="black", command=takeOutG)
        crossRiver = Button(bottomFrame, text="Cross River", bg="black", fg="white", command=crossRiver) 
                                                                                                                      
        help = Button(helpFrame, text="Help", bg="white", fg="red")
        quit = Button(helpFrame, text="Quit game", bg= "black", fg="red", command=w.quit)
        
        getIn.grid(row=0) 
        PIC.grid(row=0, column=2)
        PIF.grid(row=0, column=4)
        PIG.grid(row=0, column=5)
        TOC.grid(row=1)
        TOF.grid(row=1, column=2)
        TOG.grid(row=1, column=5)
        crossRiver.grid(row=2, column=2)
        
        help.pack(fill=X)
        quit.pack(fill=X)
        
        
        

#Plasserer knappene

root = Tk()
rc = RiverCrossing(root)
root.mainloop()