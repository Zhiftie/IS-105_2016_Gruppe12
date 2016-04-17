# -*- coding: utf-8 -*-
'''
    Simple udp socket server
    Silver Moon (m00n.silv3r@gmail.com)
'''


import socket
import sys
 
HOST = 'localhost'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
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
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
    string = "hei pa deg brah" #det som skal printes hvis linjen under kjores. 
    if data == "hei": #data = input fra brukeren. 
        s.sendto(string, addr) #dette er hva som faktisk sendes til brukeren. 
        
    reply = 'OK...' + data 
     
    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    """
    Trying to send state.py - the game - to the connected client. 
    Result: server prints the entire state.py syntax. 
    
    filename='state.py'
    f = open(filename,'r')
    l = f.read(1024)
    while (l):
        s.sendto(l, addr)
        print('Sent ',repr(l))
        l = f.read(1024)
    f.close()
    """
s.close()   