import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

print( "STA", sta_if.active() )
print( "AP", ap_if.active(), ap_if.ifconfig() )
