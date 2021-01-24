import socket
import network

port = 10086
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind( ('192.168.178.50',port) ) 
s.bind( ('127.0.0.1',port) )
sta = network.WLAN(network.STA_IF)
print('network config:', sta.ifconfig())
print('waiting...')
while True:  
 data,addr=s.recvfrom(1024)
 print('received:',data,'from',addr)

