import string
import random
print "Velg STEIN, SAKS eller PAPIR"

pone = raw_input(' ')
ptwo = raw_input(' ')
status = "' '"

def cast():
    print "Player 1 brukte %s, Player 2 brukte %s" % (pone, ptwo)
    check(pone, ptwo)

def check(pone,ptwo):
    if pone == ptwo:
        status = "Draw"
        print status
    elif (pone != ptwo):
        print "%r vs %r" % (pone, ptwo)
        if "stein" in pone and "saks" in ptwo:
            status = "player 1 wins"
            print status

            
        
        
        
        
        
    
        
    
