import RPi.GPIO as gpio
import time
import cv2
import imutils
import numpy as np
import os
import statistics

#Define Pins
trig=16
echo=18

def distance():
	gpio.setmode(gpio.BOARD)
	gpio.setup(trig, gpio.OUT)
	gpio.setup(echo, gpio.IN)

	#Ensure output has novalue
	gpio.output(trig, False)
	time.sleep(0.010)

	#Generate the trigger pulse
	gpio.output(trig, True)
	time.sleep(0.00001)
	gpio.output(trig,False)

	#Generate Echo time signal
	while gpio.input(echo) ==0:
		pulse_start = time.time()

	while gpio.input(echo) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	# Convert time to Distance
	distance = pulse_duration*17150
	distance = round(distance, 2)

	
	# Clean up GPIO and return the distance
	gpio.cleanup()
	return distance

#dist = []
#for i in range(0,10):
#	dist.append(distance()) 
#	time.sleep(1)

#avg= statistics.mean(dist)
#print(avg)
#time.sleep(1)
#print("Distance: ",distance(), " cm")
