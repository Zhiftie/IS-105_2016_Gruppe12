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
def cmd():
    pass
def test():
    print "Hello World"

def rCmd():
    if d[0] in l1:
        reply = l1[d[0]]()
        s.sendto(reply , addr)
            
    else:
        reply ="Command not found"
        s.sendto(reply , addr)
               
    
l1 = {"test" : test}
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if data:
        rCmd()
        
    elif not data: 
        break
     
    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()


s.close()