print("oled test")

if 0:
 import machine, ssd1306
 i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
 print(i2c.scan())
 oled = ssd1306.SSD1306_I2C(128, 64, i2c)
 oled.fill(0) 
 oled.text('MicroPython on', 0, 0)
 oled.text('an ESP32 with an', 0, 10)
 oled.text('attached SSD1306', 0, 20)
 oled.text('OLED display', 0, 30)
 oled.show()


from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
while True:
  led.value(not led.value())
  sleep(0.5)