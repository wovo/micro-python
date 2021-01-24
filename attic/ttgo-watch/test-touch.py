import machine
import time
i1 = machine.I2C(sda=machine.Pin(23),scl=machine.Pin(32))
while True:
    ts, xh, xl, yh, yl = i1.readfrom_mem(56, 2, 5)
    if ts & 3:
        print((xh&15)*256+xl, (yh&15)*256+yl)
    time.sleep(0.1)