import machine
import time
i0 = machine.I2C(sda=machine.Pin(21),scl=machine.Pin(22))
assert i0.readfrom_mem(25, 0, 1) == b'\x13'
i0.writeto_mem(25, 0x7d, bytes([4]))

while True:
    x1, x2, y1, y2, z1, z2 = i0.readfrom_mem(25, 0x12, 6)
    x = (x2 << 4) + (x1 >> 4)
    y = (y2 << 4) + (y1 >> 4)
    z = (z2 << 4) + (z1 >> 4)
    if x >= 2048: x -= 4096
    if y >= 2048: y -= 4096
    if z >= 2048: z -= 4096
    print("%d %d %d" % (x,y,z))
    time.sleep(0.1)