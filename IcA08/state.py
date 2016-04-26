# -*- coding: utf-8 -*-
from tape import * 
from GUI_rc import *

class State:
    def __init__(self):
        self.tape = Tape() #Creates a tape object
        self.rc = RiverCrossing() #Creates a GUI
    
    
    def check_lose_combo(self):
        if (self.tape in self.tape.fox) and (self.tape.man not in self.tape.chicken) or \
           (self.tape.chicken in self.tape.corn) and (self.tape.man not in self.tape.chicken):
            return True #R.I.P.
        return False #Carry on
    
    def man_in_boat(self):
        if self.tape.man in "boat":
            answer = raw_input("Type 1 to go outside of boat, and 2 to travel to the other side.")
            if self.tape.boat in "left":
                if answer == "1":
                    self.tape.set_man("left")
                else:
                    self.tape.set_boat("right")
            elif self.tape.boat in "right":
                if answer == "1":
                    self.tape.set_man("right")
                else: 
                    self.tape.set_boat("right")
            return True
        return False
    
    def man_on_left(self):
        if self.tape.man in "left":
            if self.items_on_boat() is self.tape.chicken:
                self.man_left_item_boat(self.tape.chicken)
            elif self.items_on_boat() is self.tape.corn:
                self.man_left_item_boat(self.tape.corn)
            elif self.items_on_boat() is self.tape.fox:
                self.man_left_item_boat(self.tape.fox)
            else:
                pass # no items in boat
    def man_on_left(self):
        if self.tape.man in 'right':
            if self.items_on_boat() is self.tape.chicken:
                self.man_right_item_boat(self.tape.chicken)
            elif self.items_on_boat() is self.tape.corn:
                self.man_right_item_boat(self.tape.corn)
            elif self.items_on_boat() is self.tape.fox:
                self.man_right_item_boat(self.tape.fox)
            else:
                pass  # no items in boat      
                    
        
    def check_state(self):
        if self.check_lose_combo():
            print "player is dead"
            return True
        if self.man_no_items_boat(): return None
        if self.man_in_boat(): return None
        self.man_on_left()
        self.man_on_right()
        