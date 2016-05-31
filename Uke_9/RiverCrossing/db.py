# -*- coding: utf-8 -*-
class Database():
    """
    Vi valgte å bruke lister for båten og hver side av elva, samt en boolean verdi for båtens posisjon
    """
    
    leftB = ["Fox", "Chicken", "Grain", "Man"]
    rightB =[]
    boat = []
    boatLeft = True
    
    def __init__(self):
            pass
    """
    Hensikten her var å gjøre om tilstandene i de forskjellige listene og gjøre de om til en string, som igjen kan brukes til å
    bestemme hvilken tilstand som skal vises i view. ble ikke helt ferdig
    """    
    def convList(self): #Combines all the lists from the class, creating a snapshot of the current state
        state = "".join(self.leftB) + "LB"
        state += "".join(self.rightB) + "RB"
        state += "".join(self.boat) + "inBoat"
        if self.boatLeft is True:
            state += "boatL"
        else:
            state += "boatR"
        return state

