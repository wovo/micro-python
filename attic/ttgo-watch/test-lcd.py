import machine
i0 = machine.I2C(sda=machine.Pin(21),scl=machine.Pin(22))
power_output_control = i0.readfrom_mem(53, 0x12, 1)[0]
power_output_control |= 4 # LDO2 enable
i0.writeto_mem(53, 0x12, bytes([power_output_control]))

backlight = machine.PWM(machine.Pin(12), freq=100, duty=200)

import machine
import st7789
spi=machine.SPI(2,baudrate=32000000, polarity=1, phase=0, bits=8, firstbit=0, sck=machine.Pin(18,machine.Pin.OUT),mosi=machine.Pin(19,machine.Pin.OUT))
disp=st7789.ST7789(spi,240,240,reset=None,cs=machine.Pin(5,machine.Pin.OUT),dc=machine.Pin(27,machine.Pin.OUT))
disp.init()
disp.fill(st7789.BLUE)
disp.fill_rect(40,40,160,160,st7789.WHITE)
disp.fill_rect(42,42,156,156,st7789.RED)