import network
import urequests

def getpage( page ):
    r = requests.get("http:192.168.4.1/index5.html")
    print( r )
    
getpage( "index3.html" )
   

