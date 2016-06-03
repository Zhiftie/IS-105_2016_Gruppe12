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
    
    def getIn(self):
        if boatLeft is True: 
            if len(d.boat) <= 2 or "Man" not in d.boat:
                d.boat.append("Man") # adds man to boat
                d.leftB.remove("Man") # removes man from left bank
            
        elif boatLeft is False:
            if len(d.boat) <= 2 or "Man" not in d.boat:
                d.boat.append("Man") #adds man to boat
                d.rightB.remove("Man") # removes man fram right bank.
            else: 
                print "There is either too many items in the boat, or the man is already in the boat."
    
    
    def getOut(self):
        if boatLeft is True and "Man" in d.boat:
            d.leftB.append("Man") 
            d.boat.remove("Man")
        elif boatLeft is False and "Man" in d.boat:
            d.rightB.append("Man")
            d.boat.remove("Man")
            
        else: 
            print "The man is already in the boat."
            
        
    def takeOut(self, item):
        if item in d.boat:
            if boatLeft is true:
                d.leftB.append(item)
                d.boat.remove(item)
            else:
                d.rightB.append(item)
                d.boat.remove(item)
                
    """
    * Skal sjekke hva slags items som er i båten, og hvor båten er. Sjekker også man mannen er i båten. 
    * Her ser vi at siden vi (dessverre) har valgt å ikke bruke manipulerbare felt blir det vanskelig å implementere en funksjonell metode som kan ta items som parameter og bruke de.
    """
    def crossRiver(self, item):
        if boatLeft is True and "Man" in d.boat:
            boatLeft = False # Sets boat to right with man in boat.
        
        elif boatLeft is False and "Man" in d.boat:
            boatLeft = True # Sets boat to left with man in boat.
        
        
        elif boatLeft is True and "Man" in d.boat:
            if item in d.boat: 
                boatLeft = False #Sets boat to right with man and item x in boat.
        elif boatLeft is False and "Man" in d.boat:
            if item in d.boat:
                boatLeft is True #Sets boat to left with man and item x in boat. 
        
        
                
          
    
    
        
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
    
    
        
# Test cases 
r = River([['boat isat left'],['chicken isat left'],['fox isat left'],['man isat left'], ['grain isat left']])
r.start()
r.database() # Data representasjon av verden til enhver tid
r.view()
r.crossRiver()
r.database()
r.view()
r.crossriver() 
r.view()

        