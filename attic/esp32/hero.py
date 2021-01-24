from machine import Pin, PWM
from time import sleep

class motor:
   def __init__( self, p1n, p2n, f = 2000 ):
       self.p1n = p1n
       self.p2n = p2n
       self.f = f
       self.p1 = Pin( p1n, Pin.OUT )
       self.p2 = Pin( p2n, Pin.OUT )
       self.set( 0 )
       
   def set( self, v ):
       if v == 0 :
           self.p1.value( 1 )
           self.p2.value( 1 )
       elif v > 0:
           self.p1.value( 1 )
           self.p2.value( 0 )
       else:
           self.p1.value( 0 )
           self.p2.value( 1 )
                     
class hero:
   def __init__( self ):
      self.m1 = motor( 25, 26 )
      self.m2 = motor( 5, 16 )
      
   def motors( self, m1, m2,  ):
       self.m1.set( m1 )
       self.m2.set( m2 )
       
   def forward( self, t ):
       self.motors( 1, 1 )
       sleep( t )
       self.motors( 0, 0 )
       
   def backward( self, t ):
       self.motors( -1, -1 )
       sleep( t )
       self.motors( 0, 0 )
       
   def turn_left( self ):
       self.motors( -1, 1 )
       sleep( 0.5 )
       self.motors( 0, 0 )
                     
   def turn_right( self ):
       self.motors( 1, -1 )
       sleep( 0.5 )
       self.motors( 0, 0 )
       
def test():       
   h = hero()                  
   print( "start" )
   h.forward( 1.0 )
   h.backward( 1.0 )
   h.turn_right()
   h.turn_left()
   print( "done" )

test()       