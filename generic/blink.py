# blink the blue pin

import time
from machine import Pin

print( "servo demo" )

def pulse( pin, delay1, delay2 ):
   pin.value( 1 )
   time.sleep( delay1 )
   pin.value( 0 )
   time.sleep( delay2 )

def servo_pulse( pin_nr, position ):
   """
   Send a servo pulse on the specified gpio pin 
   that causes the servo to turn to the specified position, and
   then waits 20 ms.
   
   The position must be in the range 0 .. 100.
   For this range, the pulse must be in the range 0.5 ms .. 2.5 ms
   
   Before this function is called, 
   the gpio pin must be configured as output.
   """
   pulse( pin_nr, 0.0005 + ( position / 50000.0 ), 0.02 )
   
print( "wave.py" )   

servo = Pin( 15, Pin.OUT )
while True:
   for i in range( 0, 100, 1 ):
      servo_pulse( servo, i )
   for i in range( 100, 0, -1 ):
      servo_pulse( servo, i )