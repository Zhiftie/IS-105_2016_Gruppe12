import random


class Card:
    ranks = (2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14)
    suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
    
def __init__(self, rank, suit):
    #Creates card with rank and suit
    self._rank = rank
    self._suit = suit
    
def getRank(self):
    return self._rank
def getSuit(self):
    return self._suit
def __str__(self):
    #Returns string representing card's value
    # dictionary for face cards
    translate = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    r = self._rank
    #Check for face cards
    if r in [11, 12, 13, 14]:
        myrank = translate[r]
    else:
        myrank = str(r)
    return myrank + "of" + self._suit

class Deck:
    #Fransk kortstokk med 52 kort.
    
    def __init__(self):
    #Return new deck of cards.
        self._cards = []
        #Add a signle card for each suit and rank. 
        for suit in Card.suits:
            for rank in Card.ranks:
                c = Card(rank, suit)
                self._cards.append(c)
    def shuffle(self):
        random.shuffle(self._cards)
        
    def deal(self):
        #Deal cards! Empty deck equals no dealing.
        if len(self) == 0:
            return None
        else: 
            #Remove top card from deck and deals it.
            return self._cards.pop()
        
    def __len__(self):
        #Returns number of cards left in the deck.
        return len(self._cards)
    def __str__(self):
        result = ""
        for c in self._cards:
            result = result + str(c) + "\n"
        return result
    

class Hand:

    def __init__(self, deck):
        if ( len(deck) <5):
            print ("Ooops! Not enough cards in the deck!")
            return None
        self._cards = []
        for i in range(5):
            card = deck.deal()
            self._cards.append(card)
        self._myranks = [0] * 14
        self._mysuits = [0] * 4
        self.makeHand()
        self._cards.sort(reverse = True)
    
    def __str__(self):
        result = ""
        for card in self._cards:
            result = result +str(card)+ "\n"
        return result
    
    def makeHand(self):
        #get suit and rank for each card
        for card in self._cards:
            rank = card.getRank()
            rankIndex = Card.ranks.index(rank)
            self._myranks[rankIndex] += 1
            suit = card.getSuit()
            suitIndex = Card.suits.index(suit)
            self.mysuits[suitIndex] += 1
        return self._myranks[rankIndex]
   
    def myranksContains(self, n):
        return ( n in self._myranks)
    def mysuitCointains(self, n):
        return ( n in self._mysuits)
   
    def hasFlush(self):
        return self.mysuitCointains(5)
    
    def hasFourofAKind(self):
        return self.myranksContains(3)
    def hasFourofAKindTwo(self):
        return self._myranks[0] == 4
    def hasFourofAKindThree(self):
        return self._myranks[1] == 4
    def hasFourofAKindFour(self):
        return self._myranks[2] == 4
    def hasFourofAKindFive(self):
        return self._myranks[3] == 4
    def hasFourofAKindSix(self):
        return self._myranks[4] == 4
    def hasFourofAKindSeven(self):
        return self._myranks[5] == 4
    def hasFourofAKindEight(self):
        return self._myranks[6] == 4
    def hasFourofAKindNine(self):
        return self._myranks[7] == 4
    def hasFourofAKindTen(self):
        return self._myranks[8] == 4
    def hasFourofAKindJack(self):
        return self._myranks[9] == 4
    def hasFourofAKindQueen(self):
        return self._myranks[10] == 4
    def hasFourofAKindKing(self):
        return self._myranks[11] == 4
    def hasFourofAKindAce(self):
        return self._myranks[12] == 4
    
    def hasThreeofAKind(self):
        return self.myranksCointains(3)
    def hasThreeofAKindTwo(self):
        return self._myranks[0] == 3
    def hasThreeofAKindThree(self):
        return self._myranks[1] == 3
    def hasThreeofAKindFour(self):
        return self._myranks[2] == 3
    def hasThreeofAKindFive(self):
        return self._myranks[3] == 3
    def hasThreeofAKindSix(self):
        return self._myranks[4] == 3
    def hasFourofAKindSeven(self):
        return self._myranks[5] == 3
    def hasFourofAKindEight(self):
        return self._myranks[6] == 3
    def hasFourofAKindNine(self):
        return self._myranks[7] == 3
    def hasFourofAKindTen(self):
        return self._myranks[8] == 3
    def hasFourofAKindJack(self):
        return self._myranks[9] == 3
    def hasFourofAKindQueen(self):
        return self._myranks[10] == 3
    def hasFourofAKindKing(self):
        return self._myranks[11] == 3
    def hasFourofAKindAce(self):
        return self._myranks[12] == 3
 
    def hasPair(self):
        return self.myranksContains(2)
    def hasPairofTwo(self):
        return self._myranks[0] == 2
    def hasPairofThree(self):
        return self._myrank[1] == 2
    def hasPairofFour(self):
        return self._myrank[2] == 2
    def hasPairofFive(self):
        return self._myranks[3] == 2
    def hasPairofSix(self):
        return self._myranks[4] == 2
    def hasPairofSeven(self):
        return self._myranks[5] == 2
    def hasPairofEight(self):
        return self._myranks[6] == 2
    def hasPairofNine(self):
        return self._myranks[7] == 2
    def hasPairofTen(self):
        return self._myranks[8] == 2
    def hasPairofJack(self):
        return self._myranks[9] == 2
    def hasPairofQueen(self):
        return self._myranks[10] == 2
    def hasPairofKing(self):
        return self._myranks[11] == 2
    def hasPairofAce(self):
        return self._myranks[12] == 2
    def hasTwoPair(self):
        return self._myranks.count(2) == 2
    
    
    def hasFullHouse(self):
        return self.hasPair() and self.hasThreeofAKind()
    
    def hasRoyalStraight(self):
        return (   self._myranks[9] == 1
                   and self._myranks[10] == 1
                   and self._myranks[11] == 1
                   and self._myranks[12] == 1
                   and self._myranks[13] == 1 )
    
    def hasStraight(self):
        for i in range(9):
            if ( self._myranks[i] == 1 and
                 self._myranks[i+1] == 1 and
                 self._myranks[i+2] == 1 and
                 self._myranks[i+3] == 1 and
                 self._myranks[i+4] == 1 ):
                return True
            if self.hasRoyalStraight():
                return True
            return False
                
    def hasStraightFlush(self):
        return self.hasStraight() and self.hasFlush()
            
    def hasRoyalFlush(self):
        return self.hasRoyalStraight() and self.hasFlush()
    
    def score(self):
        if self.hasRoyalFlush():
            return 45
        elif self.hasStraightFlush():
            return 44
        elif self.hasFourofAKindAce():
            return 43
        elif self.hasFourofAKindKing():
            return 42
        elif self.hasFourofAKindQueen():
            return 41
        elif self.hasFourofAKindJack():
            return 40
        elif self.hasFourofAKindTen():
            return 39
        elif self.hasFourofAKindNine():
            return 38
        elif self.hasFourofAKindEight():
            return 37
        elif self.hasFourofAKindSeven():
            return 36
        elif self.hasFourofAKindSix():
            return 35
        elif self.hasFourofAKindFive():
            return 34
        elif self.hasFourofAKindFour():
            return 33
        elif self.hasFourofAKindThree():
            return 32
        elif self.hasFourofAKindTwo():
            return 31
        elif self.hasFullHouse():
            return 30
        elif self.hasFlush(): 
            return 29
        elif self.hasStraight():
            return 28
        elif self.hasThreeofAKindAce():
            return 27
        elif self.hasThreeofAKindKing():
            return 26
        elif self.hasThreeofAKindQueen():
            return 25
        elif self.hasThreeofAKindJack():
            return 24
        elif self.hasThreeofAKindTen():
            return 23
        elif self.hasThreeofAKindNine():
            return 22
        elif self.hasThreeofAKindEight():
            return 21
        elif self.hasThreeofAKindSeven():
            return 20
        elif self.hasThreeofAKindSix():
            return 19
        elif self.hasThreeofAKindFive():
            return 18
        elif self.hasThreeofAKindFour():
            return 17
        elif self.hasThreeofAKindThree():
            return 16
        elif self.hasThreeofAKindTwo():
            return 15
        elif self.hasTwoPair(): 
            return 14
        elif self.hasPairofAce():
            return 13
        elif self.hasPairofKing():
            return 12
        elif self.hasPairofQueen():
            return 11
        elif self.hasPairofJack():
            return 10
        elif self.hasPairofTen():
            return 9
        elif self.hasPairofNine():
            return 8
        elif self.hasPairofEight():
            return 7
        elif self.hasPairofSeven():
            return 6
        elif self.hasPairofSix():
            return 5
        elif self.hasPairofFive():
            return 4
        elif self.hasPairofFour():
            return 3
        elif self.hasPairofThree():
            return 2
        elif self.hasPairofTwo():
            return 1
        else:
            return 0
        
       
        
        def evaluateHand(self):
            if self.hasRoyalFlush():
                return "JACKPOT! Royal Flush"
            elif self.hasStraightFlush():
                return "Straight Flush"
            elif self.hasFourofAKindAce():
                return "Four of a kind - Aces"
            elif self.hasFourofAKindKing():
                return "Four of a kind - Kings"
            elif self.hasFourofAKindQueen():
                return "Four of a kind - Queens"
            elif self.hasFourofAKindJack():
                return "Four of a kind - Jacks"
            elif self.hasFourofAKindTen():
                return "Four of a Kind - Ten"
            elif self.hasFourofAKindNine():
                return "Four of a kind - Nine"
            elif self.hasFourofAKindEight():
                return "Four of a kind - Eight"
            elif self.hasFourofAKindSeven():
                return "Four of a kind - Seven"
            elif self.hasFourofAKindSix():
                return "Four of a kind - Six'"
            elif self.hasFourofAKindFive():
                return "Four of a kind - Fives"
            elif self.hasFourofAKindFour():
                return "Four of a kind - Fours"
            elif self.hasFourofAKindThree():
                return "Four of a kind - Threes"
            elif self.hasFourofAkindTwo():
                return "Four of a kind - Twos"
            elif self.hasFullHouse():
                return "Full House"
            elif self.hasFlush():
                return "Flush"
            elif self.hasStraight():
                return "Straight"
            elif self.hasThreeofAKindAce():
                return "Three of a kind - Aces"
            elif self.hasThreeofAKindKing():
                return "Three of a kind - Kings"
            elif self.hasThreeofAKindQueen():
                return "Three of a kind - Queens"
            elif self.hasThreeofAKindJack():
                return "Three of a kind - Jacks"
            elif self.hasThreeofAKindTen():
                return "Three of a kind - Tens"
            elif self.hasThreeofAKindNine():
                return "Three of a kind - Nines"
            elif self.hasThreeofAKindEight():
                return "Three of a kind - Eights"
            elif self.hasThreeofAKindSeven():
                return "Three of a kind - Sevens"
            elif self.hasThreeofAKindSix():
                return "Three of a kind - Six'"
            elif self.hasThreeofAKindFive():
                return "Three of a kind - Fives"
            elif self.hasThreeofAKindFour():
                return "Three of a kind - Fours"
            elif self.hasThreeofAKindThree():
                return "Three of a kind - Threes"
            elif self.hasThreeofAKindTwo():
                return "Three of a kind - Tows"
            elif self.hasTwoPair():
                return "Two Pair"
            elif self.hasPairofAce():
                return "Pair of Aces"
            elif self.hasPairofKing():
                return "Pair of Kings"
            elif self.hasPairofQueen():
                return "Pair of Queens"
            elif self.hasPairofJack():
                return "Pair of Jacks"
            elif self.hasPairofTen():
                return "Pair of Tens"
            elif self.hasPairofNine():
                return "Pair of Nines"
            elif self.hasPairofEight():
                return "Pair of Eights"
            elif self.hasPairofSeven():
                return "Pair of Sevens"
            elif self.hasPairofSix():
                return "Pair of Six'"
            elif self.hasPairofFive():
                return "Pair of Fives"
            elif self.hasPairofFour():
                return "Pair of Fours"
            elif self.hasPairofThree():
                return "Pair of Threes"
            elif self.hasPairofTwo():
                return "Pair of Twos"
            else:
                return nothing
            