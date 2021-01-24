from machine import Pin, PWM
from time import sleep

class motor:
   def __init__( self, p1n, p2n, f = 2000 ):
       self.p1n = p1n
       self.p2n = p2n
       self.f = f
       self.p1 = PWM( Pin( p1n ) )
       self.p1.freq( self.f )
       self.p2 = Pin( p2n, Pin.OUT )
       self.set( 0 )
       
   def set( self, v ):
       if v >= 0:
           self.p2.value( 1 )
       else:
           self.p2.value( 0 )
           v *= -1
           p1.duty( v * f // 100  )
           
m1 = motor( 25, 26 )
m2 = motor( 16, 5 )

print( "start" )

m1.set( 100 )
sleep( 1.0 )
m1.set( 0 )
sleep( 1.0 )

m2.set( 100 )
sleep( 1.0 )
m2.set( 0 )
sleep( 1.0 )

print( "done" )

       