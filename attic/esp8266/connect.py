import network
import socket

sta = network.WLAN(network.STA_IF)
sta.active( True )
for ap in sta.scan():
   print( ap )
sta.connect("datapoint","datapoint")
while not sta.isconnected():
    pass
print('network config:', sta.ifconfig())
print( "connected" )

