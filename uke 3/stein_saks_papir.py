import string
import random
print "Velg stein 'a', Saks 'b'' eller Papir'c'"

a = "stein"
b = "saks"
c = "papir"

pone = raw_input
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
        elif "stein" in pone and "papir" in ptwo:
            status = "player 2 wins"
            print status

            
        
        
        
        
        
    
        
    
