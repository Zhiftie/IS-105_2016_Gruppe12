print "== Stein, Saks Papir ==\n"
print "P1: Velg stein 'a', Saks 'b'' eller Papir'c'"
a = "stein"
b = "saks"
c = "papir"
pone = input("a, b, eller c \n >>")

print "P2: Velg stein 'a', Saks 'b'' eller Papir'c'"
ptwo = input("a, b eller c \n >>")
    
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
        elif "saks" in pone and "papir" in ptwo:
            status = "player 1 wins"
            print status
        elif "papir" in pone and "saks" in ptwo:
            status = "player 2 wins"
            print status
        elif "saks" in pone and "stein" in ptwo:
            status = "Player 2 Wins"
            print status
        elif "papir" in pone and "stein" in ptwo:
            status = "Player 1 Wins"
            print status
            
            
cast()