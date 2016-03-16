# -*- coding: utf-8 -*-

from sm import SM
from db import Database as d

class River(SM):
    
    def __init__(self, initialValue): 
        self.startState = initialValue
        self.river_db = self.startState
     
    
    def putin(self, item):
        if boatLeft is True:
            if not d.boat:
                d.boat.append(item)
                d.leftB.remove(item)
                if len(d.boat) <= 2 and "Man" not in d.boat:
                    print "There is no one who can row the boat"
        else:
            if not d.boat:
                d.boat.append(item)
                d.rightB.remove(item)
                if len(d.boat) <= 2 and "Man" not in d.boat:
                    print "There is no one who can row the boat"
        
    def takeOut(self, item):
        if item in d.boat:
            if boatLeft is true:
                d.leftB.append(item)
                d.boat.remove(item)
            else:
                d.rightB.append(item)
                d.boat.remove(item)
                
    # Osv., - definer alle kommandoen som virker på "verden" her ...
    def CrossRiver(self):
        if boatLeft is True:
            boatLeft = False
        else:
            boatLeft = True
    
    
        
    def view(self):
        # Her implementeres logikken for "vakker" utskrift
        # ...
        print "** Here is the state of the river-world:"

        allAtLeft       = "** [chicken fox grain man ---\\ \\_ _/ ________________ /---]"
        onlyBoatAtRight = "** [chicken fox grain man ---\\ _________________\\_ _/ /---]"
        allAtLeftFInB   = "** [chicken grain man ---\\ \\_ fox _/ ________________ /---]"
        # .... slik kan alle tilstander "tegnes"
        
        
        # Bruk betingelse og finn ut tilstanden fra database (db, som er en liste av lister)
        # For eksempel, hvis alt er på venstre siden av elven, skriv ut allAtLeft "bilde"
        # Dette er ikke en korrekt kode, - man bør sjekke på flere tilstandsvariabler
        # eller implementere datastrukturer som genererer "bilder" automatisk, basert på innholdet
        # i databasen
        if ['boat isat left'] in self.river_db:
            print allAtLeft
        elif ['boat isat right'] in self.river_db:
            print onlyBoatAtRight
        else:
            print ";;; MISHAP - SOMETHING WENT WRONG!"
            
    # Denne funksjonen skal definere alle overgangene fra en tilstand til en annen
    # De kan være mange, så her må man skrive en smart kode
    # Eksperimentere først med enkelte kommandoer, og så implementere denne funksjonen
    def getNextValues(self, state, inp):
        # input her er et kommandonavn og den tilsvarende funksjonen må kalles opp
        pass
    
    # Database "saker", bør ligge i egen modul
    def database(self):
        print self.river_db
    def add(self, item):
        self.river_db.append(item)
    def remove(self, item):
        self.river_db.remove(item) # typisk MISHAP, hvis item ikke finnes i listen river_db
    
    def checkState(self):
        if d
        
# Test cases 
r = River([['boat isat left'],['chicken isat left'],['fox isat left'],['man isat left'], ['grain isat left']])
r.start()
r.database() # Data representasjon av verden til enhver tid
r.view()
r.crossriver() # Dette skulle ikke være mulig, men foreløpig ingen "constraints" er definert!
r.database()
r.view()
r.crossriver() # Dette skal ikke kunne gå heller ...
r.view()

        