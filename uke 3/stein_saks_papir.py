import random
print "Velg stein 'a', Saks 'b'' eller Papir'c'"

<<<<<<< HEAD

choices = ["STEIN", "SAKS", "PAPIR"]
choices1 = ["STEIN", "SAKS", "PAPIR"]


p1 = "player one rolls:"
p2 = "player two rolls:"

print p1, (choices[random.randint(0,2)])
choices = (choices[random.randint(0,2)])
print "VS"
choices1 = (choices1[random.randint(0,2)])
print p2, (choices1[random.randint(0,2)])

if choices == choices1:
    print "Draw!"
    

 
=======
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

            
        
        
        
        
        
    
        
    
>>>>>>> 3d0812dceec4a5104263600540cf4d5a0ad36031
