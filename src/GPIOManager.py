# GPIOManager handles all commands to GPIO
import os
if os.name != 'nt':
    import RPi.GPIO as GPIO
import threading

class GPIOManager:

    # original values from "StopWatch.py" --> define the pins connect to 74HC595
    __LSBFIRST = 1
    __MSBFIRST = 2
    __dataPin = 18      # DS Pin of 74HC595
    __latchPin = 16      # ST_CP Pin of 74HC595
    __clockPin = 12       # SH_CP Pin of 74HC595
    __digitPin = (11,13,15,19)
    __number = (0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90)

    def setup(self):
        GPIO.setmode(GPIO.BOARD)     # use PHYSICAL GPIO Numbering
        GPIO.setup(self.__dataPin, GPIO.OUT)       # Set pin mode to OUTPUT
        GPIO.setup(self.__latchPin, GPIO.OUT)
        GPIO.setup(self.__clockPin, GPIO.OUT)
        for pin in self.__digitPin:
            GPIO.setup(pin,GPIO.OUT)
            
    def __init__(self):
        print("running on os.name =", os.name)
        if os.name != 'nt':
            self.setup()
        pass

    def display(self, number):
        print("display(",number,")")
        if os.name == 'arm':
            print("name == arm")
        pass