# -*- coding: utf-8 -*-
import random

class Kort:
    
    def __init__(self, rank, suite, colour):
        self.setRank(rank)
        self.setSuite(suite)
        self.setColour(colour)
        
    def getRank(self):
        return self.rank
    
    def getSuite(self):
        return self.suite
        
    def getColour(self):
        return self.colour
    
    def setRank(self, rank):
        self.rank = rank
        
    def setSuite(self, suite):
        self.suite = suite
    
    def setColour(self, colour):
        self.colour = colour

class Kortstokk:
    
    def __init__(self, cards):
        self.setCards(cards)
    
    def getCards(self):
        return self.cards
            
    def setCards(self, cards):
        self.cards = cards
        
    def stokkOmKort(self):
        random.shuffle(self.cards)
            
    def remove(self, index):
        del self.cards[index]
            
    def antallKortIgjenIStokken(self):
        self.cards.length

            


def makeKortStokk():
    cards = [] 
    for suite in ['spar', 'hjerter', 'ruter', 'kløver']:
        for rank in ['ess', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'knekt', 'dame', 'konge']:
            colour = ''
            if suite == 'spar' or suite == 'kløver':
                colour = 'svart'
            elif suite == 'hjerter' or suite == 'ruter':
                colour = 'rød'
                
            cards.append(Kort(rank, suite, colour))
    return Kortstokk(cards)

"""
Her ville mulige hender blitt definert.
f.eks. 9 if suite.hand = 5. 
8 if straight and flush.
"""

"""
For å lage en liste med rangerende verdi på kortene måtte vi gjort det her, ved f.eks:
ranks = [ 14 if r == 'A' else
13 if r == 'K' else

]
"""
            
def main():
    kortstokk = makeKortStokk()
    kortstokk.stokkOmKort()
    
    players = []
    
    numOfPlayers = 5 #Antall spillere
    spillerInput = 5 #Antall kort
        
    for player in range(numOfPlayers):
        hand = []
        for i in range(spillerInput):
            card = kortstokk.getCards().pop()
            hand.append(card)
        
        players.append(hand)
        
    for player in range(numOfPlayers):
        counter = 0 
        for i in range(spillerInput):
            card = players[player][i]
            print "Spiller" + str((player+1)) + ": " + card.getRank() + " " + card.getColour() + " " + card.getSuite() + "\n"
            counter +=1
            if counter == 5:
                print "\n" #Counts 5 lines then make a white line to seperate the players. 
                counter = 0 # resett counter after running the game, preparing it for next game.
        
  

main()

