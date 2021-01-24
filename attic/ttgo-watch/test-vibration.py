import machine
import time
p = machine.Pin(4, machine.Pin.OUT)
p(1)
time.sleep(0.2)
p(0)