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
            
def main():
    kortstokk = makeKortStokk()
    kortstokk.stokkOmKort()
    
    players = []
    
    numOfPlayers = -1
    while numOfPlayers < 1 or numOfPlayers > 7:
        numOfPlayers = int(input('Antall Spillere: '))
        
    spillerInput = -1
    while spillerInput < 1 or spillerInput > 7:
        spillerInput = int(input('Sett inn antall kort: 1-7: '))
        
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
                print "\n"
                counter = 0 # resett counter after running the game, preparing it for next game.
        
  

main()