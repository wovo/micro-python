import time
from machine import Pin

print( "neopixels demo" )

clock_pin = led = Pin( 14, Pin.OUT )
data_pin = led = Pin( 12, Pin.OUT )

def apa102_send_bytes( clock_pin, data_pin, bytes ):
    for value in bytes:
        for dummy in range( 0, 8 ):
        
           if ( value % 256 ) >= 128:
              data_pin.value( True )
           else:
              data_pin.value( False )
           value = value * 2
        
           clock_pin.value( True )
           clock_pin.value( False )     

def apa102( clock_pin, data_pin, colors ):
    apa102_send_bytes( clock_pin, data_pin, [ 0, 0, 0, 0 ] )
    for c in colors:
        apa102_send_bytes( clock_pin, data_pin, [ 255 ] )
        apa102_send_bytes( clock_pin, data_pin, c )

blue = [ 8, 0, 0 ]
green = [ 0, 255, 0 ]
red = [ 0, 0, 255 ]

def colors( x, n, on, off ):
   result = []
   for i in range( 0, n ):
      if i == x:
           result.append( on )
      else:
           result.append( off )
   return result           

def walk( clock_pin, data_pin, delay, n = 8):
   while True:
      for x in range( 0, n ):
         apa102( clock_pin, data_pin, colors( x, n, red, blue ) )
         time.sleep( delay )
      for x in range( n - 1, 1, -1 ):
         apa102( clock_pin, data_pin, colors( x, n, red, blue ) )
         time.sleep( delay )
         
walk( clock_pin, data_pin, 0.03 )                 
