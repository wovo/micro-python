import watch

# werkt WEL vanaf reset - mist er iets?
# werkt soms ook niet na een andere code...

p = watch.PMU()
p.enablePower( watch.AXP202_LDO2 )
p.enablePower( watch.AXP202_DCDC3 )

import machine
backlight = machine.PWM(machine.Pin(12), freq=100, duty=200)
pp = machine.PWM(machine.Pin(12), freq=1000, duty=512)

spi=machine.SPI(2,baudrate=32000000, polarity=1, phase=0, bits=8, firstbit=0, sck=machine.Pin(18,machine.Pin.OUT),mosi=machine.Pin(19,machine.Pin.OUT))
disp=watch.ST7789(spi,240,240,reset=None,cs=machine.Pin(5,machine.Pin.OUT),dc=machine.Pin(27,machine.Pin.OUT))
disp.init()
disp.fill(watch.BLUE)
disp.fill_rect(40,40,160,160,watch.WHITE)
disp.fill_rect(42,42,156,156,watch.RED)
