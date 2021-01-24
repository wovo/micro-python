import machine
pp = machine.PWM(machine.Pin(12), freq=1000, duty=512)