import network, socket

sta = network.WLAN( network.STA_IF )
sta.active( True )
print( "network config %s\n" % str( sta.ifconfig() ) )
print( "visible access points:" )
for ap in sta.scan():
   print( "   %s" % str( ap ) )
