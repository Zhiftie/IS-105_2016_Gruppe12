import os
os.chdir("C:\Users\Martin\Documents\GitHub\IS-105_2016_Gruppe12\uke_5")
from PokerU5 import *

def all_same(items):
    return all(x == items[0] for x in items)

def dealHands():
    d = Deck()
    d.shuffle()

d = Deck(self)
hlist = []
s = []

while True:
    str = raw_input("How many players are playing?" )
    if not str.isdigit():
        print ("Positive number of players is required. Try again." )
    else: n = int( str )
    break
      
for i in range(n):
    if (len(d) < n):
        print ("\nBrace yourself, dealing a new deck!")
        d = Deck()
        d.shuffle()
    h = Hand(d)
    print ("Player " + `i` + "'s hand is: ")
    print h
    handrank = h.evaluateHand()
    handscore = h.score()
    s.append(handscore)
    hlist.append(handrank)
print hlist
print s


if s[0] == max(s):
    print "Player 1 wins with a " + hlist[0]
if s[1] == max(s):
    print "Player 2 wins with a " + hlist[1]
if s[2] == max(s):
    print "Player 3 wins with a " + hlist[2]
if s[3] == max(s): 
    print "Player 4 wins with a " + hlist[3]
if s[4] == max(s):
    print "Player 5 wins with a " + hlist[4]
if s.count(max(s)) > 1:
    print "The game is draw!"
dealHands()
