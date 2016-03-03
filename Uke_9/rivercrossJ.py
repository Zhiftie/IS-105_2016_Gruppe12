import SM

class River(sm.SM):
    river_db = []
    #Blir kalt hver gang klassen blir instansiert
    def __init__(self, initialValue):
        self.startState = initialValue
        self.river_db = self.startState
        print type(self.river_db)
    def view(self):
        #Her implementers logikken for "vakker" utskrift
    
        print " xx Here is the state of the river-world:"
        
        allAtLeft           = "xx [chicken fox grain man ---\\ \\_ _/ _______________/---]"
        onlyBoatAtRight     = "xx [chicken fox grain man ---\\___________________\\_ _/ /]"
        allAtLeftFInB       = "xx [chicken grain man     ---\\ \\_fox_/ ________________/]"
        
        #Bruk betningelse og finn ut tilstanden fra database (db, som er liste av lister)
        #For eksempel, hvis alt er på venstre siden av elven, skriv ut allAtLeft
        if self.river_db[0] == ['boat isat left']:
            print allAtLeft
        elif self.river_db.index(['boat isat right']):
            print onlyBoatAtRight
            
        def database(self):
            