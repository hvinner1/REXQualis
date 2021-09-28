#!/usr/bin/env python2
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

DO = 17   #the gpio port
GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)   #need to input the 3.3v or 0v

def Print(x):
    if x == 1:
        print ''
        print '   ***************'
        print '   * Not raining *'
        print '   ***************'
        print ''
    if x == 0:
        print ''
        print '   *************'
        print '   * Raining!! *'
        print '   *************'
        print ''

def loop():
    status = 1
    while True:
        print ADC.read(0)  #print the data of  PCF8591
        
        tmp = GPIO.input(DO);
        if tmp != status:
            Print(tmp)
            status = tmp
        
        time.sleep(0.2)  #sleep 0.2 s for next

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt: 
        pass    