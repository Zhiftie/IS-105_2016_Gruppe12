
import socket
import sys

HOST = 'localhost'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port


left = ["c","m","f","g"]
boat = []
right= []
boatLeft = True

def putIn():
    if boatLeft:
        obj2Put = left.index(raw_input("Choose on of the object to put into the boat >> "))
        boat.append(left.pop(obj2Put))
        showState()
    if not boatLeft:
        obj2Put = right.index(raw_input("Choose on of the object to put into the boat"))
        boat.append(right.pop(obj2Put))
        showState()

def showState():
    state = "Left Bank:"+ ",".join(left), "Boat: " + ",".join(boat) ,"Right bank: " +",".join(right)
    #if boatLeft:
        #state += " Boat at left"
    #else:
        #state += " Boat at Right"
    return state

def manInBoat():
    if boatLeft:
        man = left.index("m")
        boat.append(left.pop(man))
    if not boatLeft:
        man = right.index("m")
        boat.append(right.pop(man))
    showState()

def crossRiver():
    global boatLeft
    if boatLeft:
        boatLeft = False
    else:
        boatLeft = True
    checkState()
    showState()

def unload():
    if boatLeft:
        o2U = boat.index(raw_input("Choose object to unload >> "))
        left.append(boat.pop(o2U))
    if not boatLeft:
        o2U = boat.index(raw_input("Choose object to unload >> "))
        right.append(boat.pop(o2U))
    showState()

def checkState():
    if set(['c','f']).issubset(set(left)) and "m" not in left:
        print "fox ate the chicken on the left bank" #flesh out
    if set(['c','g']).issubset(set(left)) and "m" not in left:
        print "chicken ate the grain on the left bank"
    if set(['c','f']).issubset(set(right)) and "m" not in right:
        print "Fox ate chicken on the right bank"
    if set(['c','g']).issubset(set(right)) and "m" not in right:
        print "chicken ate the grain on the right bank"
    else:
        pass
def exitBoat():
    man = boat.index("m")
    if boatLeft:
        left.append(boat.pop(man))
    if not boatLeft:
        right.append(boat.pop(man))
    return showState()
       
def cmd(data):
    cmd = data
    if cmd in cmdL:
        cmdL[cmd]
    else:
        return "Command not found"

def help():
    return "This is the rivercrossing puzzle \nThe goal is to get all the animals to the other side \nwithout the fox eating the chicken or the chicken eating the corn \n" ,\
          "Only the man and one object can be in the boat at the same time \n", \
          "For a list of all the available commands type commandhelp"
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

cmdL = {"putin" : putIn, "show" : showState, "maninboat": manInBoat, "cross" : crossRiver, "unload" : unload, "exitboat" : exitBoat, "help" : help, "commandhelp" : cHelp }

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
while (1):
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
    if data:
        reply = str(cmd(data))
        reply
        s.sendto(reply, addr) 
s.close()   