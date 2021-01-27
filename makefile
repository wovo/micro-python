#
# makescript for downloading micro-python to a few targets
#

# specify a specific serial port
# PORT ?= COM4

ESP8266_GENERIC  ?= ../images/esp8266-1m-20200902-v1.13.bin 
ESP32_GENERIC    ?= ../images/esp32-idf4-20200902-v1.13.bin 

ifeq ($(OS),Windows_NT)
   # let the tools figure out which port to use
   PORT ?=
   # if a specific Python is present, use it
   ifneq ($(wildcard C:/Python38/python.exe ),)
      PYTHON ?= C:/Python38/python
   else   
      PYTHON ?= python3
   endif
else
   # this seems to be common port on linux
   # PORT   ?= /dev/ttyUSB0
   # but the rease_flash causes a port reconnect and henec a name change :(
   PYTHON ?= python3
endif

ESPTOOL ?= cd esptool; $(PYTHON) esptool.py

ifeq ($(PORT),)
   PORTSPEC ?=
else
   PORTSPEC ?= --port $(PORT)
endif

.PHONY: esp8266 esp32 ttgo_watch
.PHONY: erase_esp8266 erase_esp32
.PHONY: download_esp8266 download_esp32

erase_esp8266:
	@echo "##### erase ESP8266 #####"
	$(ESPTOOL) --chip esp8266 $(PORTSPEC) erase_flash
   
erase_esp32:
	@echo "##### erase ESP32 #####"
	$(ESPTOOL) --chip esp32 $(PORTSPEC) erase_flash

download_esp8266: 
	@echo "##### download generic ESP8266 #####"
	$(ESPTOOL) --chip esp8266 $(PORTSPEC) write_flash --flash_mode dio --flash_size detect 0x0 $(ESP8266_GENERIC)

download_esp32: 
	@echo "##### download generic ESP32 #####"
	$(ESPTOOL) --chip esp32 $(PORTSPEC) write_flash -z 0x1000 $(ESP32_GENERIC)

esp8266: erase_esp8266, download_esp8266

esp32: erase_esp32, download_esp32


