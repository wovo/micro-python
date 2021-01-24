import network, socket
import time

port=5005
wlan = network.WLAN(network.STA_IF)

ip = wlan.ifconfig()[0]
print(ip)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

address = ('192.168.178.39', port)
s.connect(address)

n = 0
while True:
   time.sleep( 1.0 )
   n = n + 1
   print( n, "send" )

   data = str.encode("i: {}".format(n))
   s.send(data)
