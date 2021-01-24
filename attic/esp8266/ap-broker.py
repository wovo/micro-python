import network
import socket

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="datapoint", password="datapoint")
while ap.active() == False:
  pass
print( "Access point is active" )
print( ap.ifconfig() )

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, World!</h1></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  request = conn.recv(1024)
  response = web_page()
  conn.send(response)
  conn.close()
  #print('Got a connection from %s' % str(addr))
  #print('Content = %s' % str(request))
