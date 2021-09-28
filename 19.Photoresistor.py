#!/usr/bin/env python3
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

DO = 17
GPIO.setmode(GPIO.BCM)

def setup():
	ADC.setup(0x48)
	GPIO.setup(DO, GPIO.IN)


def loop():
	status = 1
	while True:
		print ('Value: ', ADC.read(0))
		
		time.sleep(0.2)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		pass	
		analogVal = ADC0834.getResult()
		print ('analog value = %d' % analogVal)
		led_val.ChangeDutyCycle(analogVal*100/255)
		time.sleep(0.2)

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the program destroy() will be executed.
		destroy()