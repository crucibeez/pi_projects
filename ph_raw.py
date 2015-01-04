#!/usr/bin/env python

#raw read of MCP3008 Pin 1 Data (from PH Sensor)
adcnum = 0
ph_reading = 0

while True:
	#read analog pin 
	read_adc0 = readadc(adcnum, SPICLK, SPIMOSI, SPIMISO, SPICS)
	ph_reading = 0.0178 * read_adc0 - 1.889
	print read_adc0
	print ph_reading

