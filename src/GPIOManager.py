# GPIOManager handles all commands to GPIO
import os
if os.name != 'nt':
    import RPi.GPIO as GPIO
import threading
from datetime import datetime
import time

class GPIOManager:

    # original values from "StopWatch.py" --> define the pins connect to 74HC595
    __LSBFIRST = 1
    __MSBFIRST = 2
    __dataPin = 18      # DS Pin of 74HC595
    __latchPin = 16      # ST_CP Pin of 74HC595
    __clockPin = 12       # SH_CP Pin of 74HC595
    __digitPin = (11,13,15,19)
    __clearScreenCode = 0xff
    __digitAtPos = (0x01,0x02,0x04,0x08)
    __digit = (0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90)
    __currentNumber = 0

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

    def __shiftOut(self,dPin,cPin,order,val):
        for i in range(0,8):
            GPIO.output(cPin,GPIO.LOW)
            if(order == self.__LSBFIRST):
                GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
            elif(order == self.__MSBFIRST):
                GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
            GPIO.output(cPin,GPIO.HIGH)

    def __outData(self, digit):
        GPIO.output(self.__latchPin,GPIO.LOW)
        self.__shiftOut(self.__dataPin,self.__clockPin,self.__MSBFIRST,digit)
        GPIO.output(self.__latchPin,GPIO.HIGH)

    def __selectDigit(self, digitCode):
        GPIO.output(self.__digitPin[0],GPIO.LOW if ((digitCode&0x08) == 0x08) else GPIO.HIGH)
        GPIO.output(self.__digitPin[1],GPIO.LOW if ((digitCode&0x04) == 0x04) else GPIO.HIGH)
        GPIO.output(self.__digitPin[2],GPIO.LOW if ((digitCode&0x02) == 0x02) else GPIO.HIGH)
        GPIO.output(self.__digitPin[3],GPIO.LOW if ((digitCode&0x01) == 0x01) else GPIO.HIGH)

    def __displayDigit(self, digitCode, index):
        self.__clearScreen()   # eliminate residual display
        self.__selectDigit(digitCode)   # Select the first, and display the single digit
        self.__outData(self.__digit[index])
        time.sleep(0.003) 
    
    def __clearScreen(self):
        self.__outData(self.__clearScreenCode)

    def __displayNumber(self):
        for i in range(0, 3):
            if self.__currentNumber < 10**i:
                self.__clearScreen()
            else:
                self.__displayDigit(self.__digitAtPos[i], self.__currentNumber%10**(i+1)//10**i)

    def __displayLoop(self):
        endtime = int(round(time.time() * 1000)) + 1000
        while (int(round(time.time() * 1000)) < endtime):
            self.__displayNumber()

    def display(self, number):
        self.__currentNumber = number
        if os.name == 'posix': # on raspberry pi zero
            self.__displayLoop()