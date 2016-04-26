# -*- coding: utf-8 -*-


class Tape:
    def __init__(self):
        self.boat = "left"
        self.man = "left"
        self.fox = "left"
        self.grain = "left"
        self.chicken = "left"
        
        #Starts the game with all items at left side.


    def set_boat(self, new_pos):
        if new_pos in ("left", "right"):
            self.boat = new_pos
            return True
        else:
            return False #returns false on invalid input, e.g boat on left and new_pos = "left"

    def set_man(self, new_pos):
        if new_pos in ("left", "right", "boat"):
            self.man = new_pos
            return True
        else: 
            return False
    
    def set_chicken(self, new_pos):
        if new_pos in ("left", "right", "boat"):
            self.chicken = new_pos
            return True
        else: 
            return False
        
    def set_fox(self, new_pos): 
        if new_pos in ("left", "right", "boat"):
            self.fox = new_pos
            return True
        else: 
            return False
    
    def set_grain(self, new_pos):
        if new_pos in ("left", "right", "boat"):
            self.grain = new_pos
            return True
        else: 
            return False
    