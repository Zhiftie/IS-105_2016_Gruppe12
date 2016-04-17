# -*- coding: utf-8 -*-
import socket
import sys

HOST = 'localhost'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

help = "This is the rivercrossing puzzle\nThe goal is to get all the animals to the other side \nwithout the fox eating the chicken or the chicken eating the corn \nOnly the man and one object can be in the boat at the same time\nFor a list of all the available commands type commandhelp"
left = ["c","m","f","g"]
boat = []
right= []
boatPos = "left"
done = False

def putIn():
    reply = "Put in who?"
    s.sendto(reply, addr)
    d = s.recvfrom(1024)
    data = d[0]
    if boatPos == "left":
        obj2Put = left.index(data)
        boat.append(left.pop(obj2Put))
    if boatPos == "right":
        obj2Put = right.index(data)
        boat.append(right.pop(obj2Put))


def showState():
    state = "Left Bank:"+ ",".join(left), "Boat: " + ",".join(boat) ,"Right bank: " +",".join(right) + "Boat position: " + boatPos
    return state

def manInBoat(): 
    if boatPos == "left":
        man = left.index("m")
        boat.append(left.pop(man))
    if boatPos == "right":
        man = right.index("m")
        boat.append(right.pop(man))

def crossRiver():
    global boatPos
    if boatPos == "left":
        boatPos = "right"
    else:
        boatPos = "left"
    checkState()

def unload():
    reply = "Unload who?"
    s.sendto(reply, addr)
    d = s.recvfrom(1024)
    data = d[0]    
    if boatPos == "left":
        o2U = boat.index(data)
        left.append(boat.pop(o2U))
    if boatPos == "right":
        o2U = boat.index(data)
        right.append(boat.pop(o2U))
"""
state check, ends process if an end state is reached
"""

def checkState():
    global done
    if set(['c','f']).issubset(set(left)) and "m" not in left:
        endS = "fox ate the chicken on the left bank"
        s.sendto(endS, addr) # 
        done = True
    if set(['c','g']).issubset(set(left)) and "m" not in left:
        endS = "chicken ate the grain on the left bank"
        s.sendto(endS, addr)
        done = True
    if set(['c','f']).issubset(set(right)) and "m" not in right:
        endS = "Fox ate chicken on the right bank"
        s.sendto(endS, addr)
        done = True
    if set(['c','g']).issubset(set(right)) and "m" not in right:
        endS = "chicken ate the grain on the right bank"
        s.sendto(endS, addr)
        done = True
    if ("f", "c","m","g") in right: # not done
        endS = "Everyone has crossed safely!"
        s.sendto(endS, addr)
        done = True    
    else:
        pass

def exitBoat():
    man = boat.index("m")
    if boatPos == "left":
        left.append(boat.pop(man))
    if boatPos == "right":
        right.append(boat.pop(man))
    
       
"""
Help functions not finished, move to client maybe.

"""
def cHelp():
    for k, v in cmdH.iteritems():
        return str(k + ":" + v)

cmdH = {"putin" : "Puts an item in the boat\n", 
        "show" : "View the current state of the game\n", 
        "maninboat" : "puts the man in the boatn\n", 
        "cross" : "Boat crosses the river\n", 
        "unload" : "Take one object from the boat and place on the bank\n", 
        "exitboat" : "moves the man from the boat to the bank\n",
        "help" : "Shows the game description and the objective\n"}

"""
List of all the available commands
"""
cmdL = {"putin" : putIn, "show" : showState, "maninboat": manInBoat, "cross" : crossRiver, "unload" : unload, "exitboat" : exitBoat }

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'


 
#now keep talking with the client
while not done:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
    if data in cmdL:
        cmdL[data]()
        reply = str(showState())
        s.sendto(reply, addr)
    elif data not in cmdL:
        reply = "Command not found"
        s.sendto(reply, addr)
s.close()   

"""
Dette er en veldig naiv versjon. Det forventes at en eventuell bruker vet nøyaktig hvilken forskjellige objekter som kan plasseres hvor og at reglene følges.
I en ferdig versjon ville vi brukt flere kontroller for å sjekke om den inputen som rcClient gir faktisk stemmer og kan gjennomføres uten at "serveren" crasher.
De fleste funksjonenen returnerer ikke noen verdi til klienten, men oppdaterer tilstanden på server, som igjen sender et oppdatert tilstandsbilde til klienten. 
Unntakene er putIn funksjonen, unload funksjonen, og checkState.
putIn og unload krever at klienten spesifiserer hvilken gjennstand som skal flyttes. checkState oppdaterer klienten dersom "serveren" de når en slutt tilstand

Socket koding i rcClient og rcServer hentet fra http://www.binarytides.com/programming-udp-sockets-in-python
"""