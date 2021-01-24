import machine
import time
i0 = machine.I2C(sda=machine.Pin(21),scl=machine.Pin(22))
while True:
    s, m, h = i0.readfrom_mem(81, 2, 3)
    print("%d%d:%d%d:%d%d" % ((h>>4)&3, h&0xF, (m>>4)&7, m&0xF, (s>>4)&7, s&0xF))
    time.sleep(1)