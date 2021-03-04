![](images/micro-python.png)

# MicroPython - WORK IN PROGRESS

updated 2021-01-27

## Intro

[MicroPython]() is a Python interpreter running on a micro-controller.
To use it, first download the Python interpreter image for
your particular micro-controller onto the micro-controller.
The tool for doing so depends on your micro-controller.
If you don't screw up, you will have to do this only once.
Instructions for a few common ones can be found below.

To use the MicroPython interpreter on your micro-controller
you need a connection to it, usually serial-over-USB.
For this MicroPython supports the REPL 
(Read-Execute-Print-Loop) protocol.
Yiou can use this directly, 
like you would use as a Python interpreter prompt.
But it is much easier to use a Python IDE that can connects
to the micro-controller.
I use
[Thonny](https://thonny.org)
for this purpose.
There are Thonny installers for Windows, Linux and Mac,
and even one that runs directly on a Python interpreter.

## EPS8266, ESP32

MicroPython for the ESP83266 and ESP32 is an easy way to
create an small WiFi-connected system.
The ESP8266 is the cheaper of the two, 
but its amount of RAM and FLASH is much smaller,
so I prefer the ESP32.

For both chips, the download tool is called esptool.
Use *the one from this 
[github](https://github.com/espressif/esptool)*,
others might not (always) work.

MicroPython images can be found at
[this page](https://micropython.org/download/all).

Before downloading, you must erase the Flash. 
The commands are:

```bash
# ESP8266, replace <PORT> (or omit --port <PORT>) and <IMAGE>
python esptool.py --chip esp8266 --port <PORT> erase_flash
python esptool.py --chip esp8266 --port <PORT> write_flash --flash_mode dio --flash_size detect 0x0 <IMAGE>
```

```bash
# ESP32, replace <PORT> (or omit --port <PORT>) and <IMAGE>
python esptool.py --chip esp32 --port <PORT> erase_flash
python esptool.py --chip esp32 --port <PORT> write_flash -z 0x1000 <IMAGE>
```

For all esptool target commands, you can either specify the
serialport with --port <PORT>, or leave this out and have the
esptool scan all your ports. 
For Linux: after an erase_flash the target re-connects, 
which on my system caused it to switch to a different */dev/ttyUSBx*.

The github repository you are reading now includes the
epstool, and generic images for ESP8266 and ESP32.
To flash one, assuming you are on Linux and in the root of
the cloned repository, you can use one of the commands:

```bash
make eps8266
make esp32
```

For some reason this works perfecly for me on (Ubuntu) Linux, 
but it doesn't work reliably on windows, 
maybe because the USB-serial driver doesn't reset the target properly.

## Thonny

Connect your target that runs MicroPython via USB.
Start Thonny.
Under Run->Select interpreter you can select the Python
interpreter that you want your code to run on, and
(for MicroPython) the REPL connection port.
For me, *MicroPython (generic)* always worked.

In the bottom page, you see the REPL prompt. 
Here you can type MicroPython commands, 
and the output of MicroPython goes here.

You can edit Python code in the editor.
When you open or save a file, you will be asked whether
this must be done on *This computer* (your PC) or on the
*MicroPython device*.
When you run a file that is stored on your computer
on the MicroPython interpreter, it is automatically download
first, but note that any files you might import are not.

I found Thonny with REPL to be mostly woprking, but sometimes
it gets into an error-message loop.

## Generic xxamples

### Hello

Hello world for MicroPython is exactly the same for normal Python.

```Python
print( "Hello world\n" )
```

### Blinky

Most boards have an on-board LED, but the pin to which the LED is 
connected depends on the board.
The code below uses pin 2.

```Python
import machine, time
led = machine.Pin( 2, Pin.OUT )
while True:
  led.value( 1 )
  time.sleep( 0.5 )
  led.value( 0 )
  time.sleep( 0.5 )
```

### Show visible access points

```Python
import network, socket

sta = network.WLAN( network.STA_IF )
sta.active( True )
print( "network config %s\n" % str( sta.ifconfig() ) )
print( "visible access points:" )
for ap in sta.scan():
   print( "   %s" % str( ap ) )
```

### Serve a web page

```Python
```

### Read a web page

```Python
```

## Lilygo T-WATCH-2020

For targets that have specific peripherals there are specialized
MicroPython images, with have some of the drivers for the
peripherals built-in. 
So far I haven't found a stable one for this watch that supports all functions.
The watch subdirectorty has a file watch.py 
in which I gathered interface code that I found,
most on 
[this page](https://nick.zoic.org/art/lilygo-ttgo-t-watch-2020/),
the lcd is from
[here](https://gitlab.com/mooond/t-watch2020-esp32-with-micropython).
The following examples show these.

### Buzzer

```Python
import watch

b = watch.buzzer()
b.buzz( 0.2, 0.3 )
b.buzz( 0.2, 0.3 )
b.buzz( 0.2, 0.3 )
b.buzz( 0.8 )
```

### Accelerometer

```Python
import watch, time

a = watch.accelerometer()
while True:
    print( "%d %d %d" % a.read() )
    time.sleep( 0.1 )
```

### Real Time Clock

```Python
import watch, time

r = watch.rtc()
while True:
    print( "%02d:%02d:%02d" % r.read() )
    time.sleep( 1 )
```
### Touch

```Python
import watch, time

print( "touch demo - touch the display!" )
t = watch.touch()
while True:
    v = t.read()
    if v:
        print( v )
    time.sleep( 0.1 )
```




## Links
- [Thonny](https://thonny.org)
- [esptool](https://github.com/espressif/esptool)
- [a list of MicroPython libraries](https://awesome-micropython.com)
- [generic MicroPython images](https://micropython.org/download/all)
- [Lilygo T-WATCH-2020 image 1](https://gitlab.com/mooond/t-watch2020-esp32-with-micropython)
- [Lilygo T-WATCH-2020 image 2](https://github.com/OPHoperHPO/lilygo-ttgo-twatch-2020-micropython)
- [ampy](https://github.com/scientifichackers/ampy)
- [rshell](https://github.com/dhylands/rshell)
- [T-WATCH-20202 python low-level eaxmples](https://nick.zoic.org/art/lilygo-ttgo-t-watch-2020/)

updated py file for moond: https://github.com/jhfoo/t-watch-2020-micropython
e.g. ESP-WROOM-32 should be DIO

https://github.com/jhfoo/t-watch-2020-micropython

interfaces:
https://github.com/OPHoperHPO/lilygo-ttgo-twatch-2020-micropython/blob/master/ports/esp32/boards/LILYGO_T_WATCH_2020_V1/modules/ttgo.py

## todo
- notes on support for hardware features
- more examples
- ttgo image
- note need to press key
- pyserial might be needed for esptool
- seems not to work on windows??
- find serial port does not work on linux :(
- watch picture
- Thonny picture


