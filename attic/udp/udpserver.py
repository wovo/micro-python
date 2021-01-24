#!/usr/bin/env python3
import socket
import sys
import subprocess

HOST = ''   # All available interfaces
PORT = 10000 # Random port (don't forget the Windows firewall)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print('> Socket listening on port:',PORT)

while True:
    print('\nwaiting to receive message')
    data, address = s.recvfrom(4096)
    
    print('received %s bytes from %s' % (len(data), address))
    print(data)
    
    if data:
        sent = s.sendto(data, address)
        print('sent %s bytes back to %s' % (sent, address))
