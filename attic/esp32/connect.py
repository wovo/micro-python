import network
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('War is no picnic 2.4', '43761675858774704684')
print('network config:', sta.ifconfig())

