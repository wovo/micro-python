import machine, ssd1306
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
print( i2c.scan() )

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
        
oled.show()