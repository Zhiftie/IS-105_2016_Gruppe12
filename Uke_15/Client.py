"""from test import test1 as t

def t1():
    print "t1"
def t2():
    print "t2"

def connectS():
"""
    #Connect through predefined socket. Socket modul, socket server.
"""
def listCmd():
"""
    #print list of all the different commands the player can use
    #List of all the commands kept in state modul?
"""
    for k in l1:
        print k + " : Desc of key"
def cmd(cmdW):
"""
    #Use cmdW to find the appropriate command in the state module
"""
def cmd(): # Calls a cmd from dictionary with all the different commands based on the word entered as a parameter
    #l1[raw_input("Insert Command >>> ")]()
    inp = raw_input(">>> ")
    if inp in l1:
        l1[inp]()
        return inp
    else:
        print "Command not found"
    
def quit():
"""
    #ends the process
"""
    print "quit"

l1 = { "hello" : t1, "test2" : t2, "quit" : quit, "ls" : listCmd  } #dict with all the commands, needs to be extended to cover all the different commands in state.py


while True:
    command = cmd()
    if command is "quit":
        break
"""    
    
'''
        udp socket client
        Silver Moon
        http://www.binarytides.com/programming-udp-sockets-in-python
        
'''
     
import socket   #for sockets
import sys  #for exit
     
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
     
host = 'localhost';
port = 8888;
     
while(1) :
    cmd = raw_input('Enter message to send : ')
         
    try :
            #Set the whole string
        s.sendto(cmd, (host, port))
             
            # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
             
        print 'Server reply : ' + reply
         
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()        