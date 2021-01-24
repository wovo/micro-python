import network
import socket
import utime

def getpage( page ):
    ai = socket.getaddrinfo( "192.168.4.1", 80 )
    #print( "Address infos:", ai)
    addr = ai[0][-1]
    #print( "Connect address:", addr)
    
    s = socket.socket()
    #print( "gona connect" )
    s.connect( addr )

    #print( "gona send" )
    t1 = utime.ticks_ms()
    s.send(b"GET / HTTP/1.0\r\n\r\n")
    #print( "gona rcv" )
    x = s.recv(100)
    t2 = utime.ticks_ms()
    print( t2 - t1, "[", x, "]")
    
getpage( "index3.html" )
   

