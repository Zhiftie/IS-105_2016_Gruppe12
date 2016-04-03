def view(self):
    # Her implementeres logikken for "vakker" utskrift
    # ...
    print "** Here is the state of the river-world:"

    # Venstre side
    allAtLeft       = "** [chicken fox grain man ---\\ \\_ _/ ________________ /---]"
    foxInBoatLeft   = "** [chicken grain man ---\\ \\_ fox _/ ________________ /---]"
    grainInBoatLeft   = "** [chicken man fox ---\\ \\_ grain _/ ________________ /---]"
    manInBoatLeft   = "** [chicken fox grain ---\\ \\_ man _/ ________________ /---]"
    chickenInBoatLeft   = "** [fox grain man ---\\ \\_ chicken _/ ________________ /---]"
    foxManInBoatLeft  = "** [chicken grain ---\\ \\_ fox, man _/ ________________ /---]"
    grainManInBoat  = "** [chicken fox ---\\ \\_ grain, man _/ ________________ /---]"
    chickenManInBoat  = "** [fox grain---\\ \\_ chicken, man _/ ________________ /---]"
    foxGrainInBoatLeft  = "** [chicken man ---\\ \\_ fox, grain _/ ________________ /---]"
    foxChickenInBoatLeft  = "** [grain man ---\\ \\_ fox, chicken _/ ________________ /---]"
    grainCchickenInBoatLeft  = "** [fox man ---\\ \\_ grain, chicken _/ ________________ /---]"
    manLoadOutChickenRight  = "** [fox grain ---\\ _________________\\_ chicken _/ /--- man]"
    foxOnRightWithBoat   = "** [chicken grain ---\\ _________________\\_ man _/ /--- fox]"
    grainOnRightWithBoat   = "** [chicken fox ---\\ _________________\\_ man _/ /--- grain]"
    manOnRightWithBoat   = "** [chicken fox grain ---\\ _________________\\_ _/ /--- man]"
    chickenOnRightWithBoat   = "** [fox grain ---\\ _________________\\_ man _/ /--- chicken]"
    foxOnRight  = "** [chicken grain man ---\\ \\_ _/ ________________ /--- fox]"
    grainOnRight  = "** [chicken fox man ---\\ \\_ _/ ________________ /--- grain]"
    manOnRight  = "** [chicken fox grain ---\\ \\_ _/ ________________ /--- man]"
    chickenOnRight  = "** fox grain man ---\\ \\_ _/ ________________ /--- chicken"
    chickenManOnRight  = "** [fox grain ---\\ _________________\\_ _/ /--- chicken, man]"
    foxManOnRight  = "** [chicken grain ---\\ _________________\\_ _/ /--- fox man]"
    grainManOnRight  = "** chicken fox ---\\ _________________\\_ _/ /--- grain man"
    # Høyre side
    allAtRight      = "** [---\\ _________________\\_ _/ /--- chicken fox grain man]"
    foxInBoatRight  = "** [---\\ _________________\\_ fox _/ /--- chicken grain man]"
    grainInBoatRight  = "** [---\\ _________________\\_ grain _/ /--- chicken fox man]"
    maninBoatRight  = "** [---\\ _________________\\_ man _/ /--- chicken fox grain]"
    chickenInBoatRight  = "** [---\\ _________________\\_ chicken _/ /--- fox grain man]"
    foxManInBoatRight = "** [---\\ _________________\\_ fox, man _/ /--- chicken grain]"
    grainManInBoatRight = "** [---\\ _________________\\_ grain, man _/ /--- chicken fox]"
    chickenManInBoatRight = "** [---\\ _________________\\_ chicken, man _/ /--- fox grain]"
    foxGrainInBoatRight = "** [---\\ _________________\\_ fox, grain _/ /--- chicken man]"
    foxCchickenInBoatRight = "** [---\\ _________________\\_ fox, chicken _/ /--- grain man]"
    chickenGrainInBoatRight = "** [---\\ _________________\\_ chicken, grain _/ /--- fox man]"
    manLoadOutChickenLeft = "** [man ---\\ \\_ chicken _/ ________________ /--- fox grain]"
    foxOnLeftWithBoat = "** [fox ---\\ \\_ man _/ ________________ /--- chicken grain"
    grainOnLeftWithBoat = "** [grain ---\\ \\_ man _/ ________________ /--- chicken fox]"
    manOnLeftWithBoat = "** [man ---\\ \\_ _/ ________________ /--- chicken fox grain]"
    chickenOnLeftWithBoat = "** [chicken ---\\ \\_ man _/ ________________ /--- fox grain]"
    foxOnLeft   = "** [fox ---\\ _________________\\_ _/ /--- chicken grain man]"
    grainOnLeft   = "** [grain ---\\ _________________\\_ _/ /--- chicken fox man]"
    manOnLeft   = "** [man ---\\ _________________\\_ _/ /--- chicken fox grain]"
    chickenOnLeft   = "** chicken ---\\ _________________\\_ _/ /--- fox grain man"
    chickenManOnLeft  = "** [chicken man ---\\ \\_ _/ ________________ /--- fox grain]"
    foxManOnLeft  = "** [fox man ---\\ \\_ _/ ________________ /--- chicken grain]"
    grainManOnLeft  = "** [grain man ---\\ \\_ _/ ________________ /--- chicken fox]"
    
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