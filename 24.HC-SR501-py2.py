#!/usr/bin/env python2

import RPi.GPIO as GPIO

ledPin = 18    # define the ledPin
sensorPin = 17    # define the sensorPin

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
	GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
	GPIO.setup(sensorPin, GPIO.IN)    # Set sensorPin's mode is input

def loop():
	while True:
		if GPIO.input(sensorPin)==GPIO.HIGH:
			GPIO.output(ledPin,GPIO.HIGH)
			print 'led on ...'
		else :
			GPIO.output(ledPin,GPIO.LOW)
			print 'led off ...'

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

