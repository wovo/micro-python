#
# makescript for downloading micro-python to a few targets
#

# specify a specific serial port
# PORT ?= COM4

ESP8266_GENERIC  ?= images/esp8266-1m-20200902-v1.13.bin 
ESP32_GENERIC    ?= images/esp32-idf4-20200902-v1.13.bin 
TTGO_WATCH       ?= images/lilygo-ttgo-watch.bin 

ifeq ($(OS),Windows_NT)
   # let the tools figure out which port to use
   PORT ?=
   # if a specific Python is present, use it
   ifneq ($(wildcard C:/Python38/python.exe ),)
      PYTHON ?= C:/Python38/python
   else   
      PYTHON ?= python
   endif
else
   # this seems to be common port on linux
   PORT   ?= /dev/ttyUSB0
   PYTHON ?= python
endif

ESPTOOL ?= $(PYTHON) esptool/esptool.py

ifeq ($(PORT),)
   PORTSPEC ?=
else
   PORTSPEC ?= --port $(PORT)
endif

.PHONY: esp8266, esp32, ttgo_watch
.PHONY: erase_8266, erase_32

erase_8266:
	@echo "erase ESP8266"
	$(ESPTOOL) --chip esp8266 $(PORTSPEC) erase_flash
   
erase_32:
	@echo "erase ESP32"
	$(ESPTOOL) --chip esp32 $(PORTSPEC) erase_flash

esp8266: erase_8266
	@echo "download generic ESP8266"
	$(ESPTOOL) --chip esp8266 $(PORTSPEC) write_flash --flash_mode dio --flash_size detect 0x0 $(ESP8266_GENERIC)

esp32: erase_32
	@echo "download generic ESP32"
	$(ESPTOOL) --chip esp32 $(PORTSPEC) write_flash -z 0x1000 0x1000 $(ESP32_GENERIC)

ttgo_watch: erase_32
	@echo "download generic ESP32"
	$(ESPTOOL) --chip esp32 $(PORTSPEC) write_flash -z 0x1000 0x1000 $(TTGO_WATCH)

