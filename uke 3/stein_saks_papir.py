import string
import random
print "Velg STEIN, SAKS eller PAPIR"

<<<<<<< HEAD

choices = ["STEIN", "SAKS", "PAPIR"]
choices1 = ["STEIN", "SAKS", "PAPIR"]

p1 = "player one rolls:"
p2 = "player two rolls:"
print p1, (choices[random.randint(0,2)])
print "VS"
print p2, (choices1[random.randint(0,2)])








=======
pone = raw_input(' ')
ptwo = raw_input(' ')
status = "' '"

def cast():
    print "Player 1 brukte %s, Player 2 brukte %s" % (pone, ptwo)
    check(pone, ptwo)

def check(pone,ptwo):
    if pone == ptwo:
        status = "Draw"
    #else pone != ptwo:
        
    
        
    
>>>>>>> cacfdd8db894d42cad203152080c491c316f566b
