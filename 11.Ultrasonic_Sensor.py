#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

TRIG = 16  #define the 16 ---input
ECHO = 18  #define the 18 ---input


#notion BROAD
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)   #0.000002 s low

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)  #0.000001 s high
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:     #get the triger_begin
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:     #get the triger_end
		a = 1
	time2 = time.time()   #voice begin-end time

	during = time2 - time1
	return during * 340 / 2 * 100  #the speed of voice 314m/s

def loop():
	while True:
		dis = distance()
		print ('Distance: %.2f' % dis)
		time.sleep(0.3)

def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
	