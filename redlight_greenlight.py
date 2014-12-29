#!/usr/bin/env python
 
import RPi.GPIO as GPIO, time
import sys
DEBUG = 1
 
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(GREEN_LED, True)
GPIO.output(RED_LED, False)


def greenlighton():
        GPIO.output(GREEN_LED, True)
def greenlightoff():
        GPIO.output(GREEN_LED, False)
def redlighton():
        GPIO.output(RED_LED, True)
def redlightoff():
        GPIO.output(RED_LED, False)


try: 

        while True:

                print "I'm turning the Green LED ON!"
                greenlighton()
                time.sleep(2)
                print "I'm turning the Red LED ON!"
                redlighton()
                time.sleep(2)
                print "I'm turning the Green LED OFF!"
                greenlightoff()
                time.sleep(2)
                print "I'm turning the Red LED OFF!"
                redlightoff()
                time.sleep(2)

except KeyboardInterrupt:
        GPIO.cleanup()


