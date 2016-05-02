"""
Source GR2 - https://github.com/Cmoen11/IS-105_2016_Gruppe-2-/blob/master/uke14_oppgaver/state.py#L10
"""

# -*- coding: utf-8 -*-
from tape import * 


class State:
    def __init__(self):
        self.tape = Tape() #Creates a tape object
        #self.root = Tk() 
        #self.rc = RiverCrossing(root) #Creates a GUI
    
    
    def check_lose_combo(self):
        if (self.tape.chicken in self.tape.fox) and (self.tape.man not in self.tape.chicken) or \
           (self.tape.chicken in self.tape.grain) and (self.tape.man not in self.tape.chicken):
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
            elif self.items_on_boat() is self.tape.grain:
                self.man_left_item_boat(self.tape.grain)
            elif self.items_on_boat() is self.tape.fox:
                self.man_left_item_boat(self.tape.fox)
            else:
                pass # no items in boat
    def man_on_right(self):
        if self.tape.man in 'right':
            if self.items_on_boat() is self.tape.chicken:
                self.man_right_item_boat(self.tape.chicken)
            elif self.items_on_boat() is self.tape.grain:
                self.man_right_item_boat(self.tape.grain)
            elif self.items_on_boat() is self.tape.fox:
                self.man_right_item_boat(self.tape.fox)
            else:
                pass  # no items in boat      
    def items_on_boat(self):
            '''
            Check if there is any items on the boat
            :return: the variable of the item,
            with this veriable we can use 'is' to check witch variable it is.
            '''
            if 'boat' in (self.tape.chicken, self.tape.fox, self.tape.grain):
                if 'boat' in self.tape.chicken:
                    return self.tape.chicken
        
                elif 'boat' in self.tape.grain:
                    return self.tape.grain
        
                elif 'boat' in self.tape.fox:
                    return self.tape.fox
            else:
                return None    

    def check_state(self):
        if self.check_lose_combo():
            print "player is dead"
            return True
        if self.man_no_items_boat(): return None
        if self.man_in_boat(): return None
        self.man_on_left()
        self.man_on_right()
    
    def man_left_item_boat(self, item):
        '''
        If the man is at left, and there is an item inside the boat, give the user the ability to take the item out
        or go inside the bout himself.
        Also, he will write the new command that user has given the the program.
        '''
        take_out_boat = self.man_answer_items_boat_left_right(item)  # give the user ability to choose what he wants
        if take_out_boat == 1:
            self.tape.set_chicken('left')
        elif take_out_boat == 2:
            self.tape.set_grain('left')
        elif take_out_boat == 3:
            self.tape.set_fox('left')
        elif take_out_boat == 4:
            self.tape.set_man('boat')    
        print take_out_boat
        
        
    def man_right_item_boat(self, item):
        '''
        If the man is at right, and there is items inside the boat, give the user the ability to take the item out
        or go inside the bout himself.
        :param item: the item that are inside the bout, the veriable(!)
        Also, he will write the new command that user has given the the program.
        '''
        take_out_boat = self.man_answer_items_boat_left_right(item)  # give the user ability to choose what he wants
        if take_out_boat == 1:
            self.tape.set_chicken('right')
        elif take_out_boat == 2:
            self.tape.set_grain('right')
        elif take_out_boat == 3:
            self.tape.set_fox('right')
        elif take_out_boat == 4:
            self.tape.set_man('boat')    
            
            
    def man_answer_items_boat_left_right(self, item):
       #checks if the item in the boat actually is an item in the game. 
        take_out_boat = None
    
        if item is self.tape.chicken:
            answer = raw_input("Do you want to take the chicken out of the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 1
        elif item is self.tape.grain:
            answer = raw_input("Do you want to take the grain out of the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 2
        elif item is self.tape.fox:
            answer = raw_input("Do you want to take the fox out of the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 3
    
        # if the user has answered no on the previous question
        if take_out_boat is None:
            answer = raw_input("Do you want to go inside the boat? Y/N : ")
            answer = self.redefine_answer(answer)
            if answer: take_out_boat = 4
        return take_out_boat    
    
    
    def man_no_items_boat(self):
        '''
            if the man is at left, and no items inside the boat. The man is then allowed to pick one item to inside
            his boat. Depends on location
            '''
        if self.items_on_boat() != None: return None
        if self.tape.man in self.tape.chicken \
           and self.tape.man in self.tape.grain \
           and self.tape.man in self.tape.fox:
            answer = raw_input("Choose one: Go inside the boat type 1. Put chicken inside the boat type 2."
                               "Put grain inside the boat, type 3. Put fox inside the boat type 4: ")
    
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_chicken('boat')
            elif answer == '3':
                self.tape.set_grain('boat')
            elif answer == '4':
                self.tape.set_fox('boat')
            else:
                pass
            return True
    
        elif self.tape.man in self.tape.chicken \
             and self.tape.man in self.tape.grain:
            answer = raw_input("Choose one: Go inside the boat type 1. Put chicken inside the boat type 2."
                               "Put grain inside the boat, type 3.")
    
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_chicken('boat')
            elif answer == '3':
                self.tape.set_grain('boat')
            else:
                pass
            return True
    
    
        elif self.tape.man in self.tape.fox \
             and self.tape.man in self.tape.grain:
            answer = raw_input("Choose one: Go inside the boat type 1. Put fox inside the boat type 2."
                               "Put grain inside the boat, type 3.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_fox('boat')
            elif answer == '3':
                self.tape.set_grain('boat')
            else:
                pass
            return True
    
        elif self.tape.man in self.tape.fox \
             and self.tape.man in self.tape.chicken:
            answer = raw_input("Choose one: Go inside the boat type 1. Put fox inside the boat type 2."
                               "Put chicken inside the boat, type 3.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_fox('boat')
            elif answer == '3':
                self.tape.set_chicken('boat')
            else:
                pass
            return True
    
        elif self.tape.man in self.tape.chicken:
            answer = raw_input("Choose one: Go inside the boat type 1. Put chicken inside the boat type 2.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_chicken('boat')
            else:
                pass
            return True
    
        elif self.tape.man in self.tape.fox:
            answer = raw_input("Choose one: Go inside the boat type 1. Put fox inside the boat type 2.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_fox('boat')
            else:
                pass
            return True
    
        elif self.tape.man in self.tape.grain:
            answer = raw_input("Choose one: Go inside the boat type 1. Put grain inside the boat type 2.")
            if answer == '1':
                self.tape.set_man('boat')
            elif answer == '2':
                self.tape.set_grain('boat')
            else:
                pass
            return True  
        
    def redefine_answer(self, answer):
        if answer == 'y':
            answer = True
        else:
            answer = False
        return answer    
    
    
    
    
def test():
        state = State()
        dead = False
        while not dead:
            if state.check_state() is True:
                dead = True
    

if __name__ == '__main__':
    test()    