class Database():
    """
    Vi valgte � bruke lister for b�ten og hver side av elva, samt en boolean verdi for b�tens posisjon
    """
    
    leftB = ["Fox", "Chicken", "Grain", "Man"]
    rightB =[]
    boat = []
    boatLeft = True
    
    def __init__(self):
            pass
    """
    Hensikten her var � gj�re om tilstandene i de forskjellige listene og gj�re de om til en string, som igjen kan brukes til �
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

