import network
import socket

sta = network.WLAN(network.STA_IF)
sta.active( True )
print('network config:', sta.ifconfig())
for ap in sta.scan():
   print( ap )

