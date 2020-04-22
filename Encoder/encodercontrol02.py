import RPi.GPIO as gpio
import time
import numpy as np		


def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31, gpio.OUT)
	gpio.setup(33, gpio.OUT)
	gpio.setup(35, gpio.OUT)
	gpio.setup(37, gpio.OUT)

	gpio.setup(12, gpio.IN, pull_up_down= gpio.PUD_UP)

def gameover():
	gpio.output(31, False)
	gpio.output(33, False)
	gpio.output(35, False)
	gpio.output(37, False)
	
	gpio.cleanup()

#main #

init()
counter = int(0)
button = int(0)
file1 = open("Encoder_data.txt","a")

# Initialize pwm signal to control motor
pwm = gpio.PWM(37,50)
val =15
pwm.start(val)
time.sleep(0.1)

for i in range (0,1000000):
	print("counter = ",counter,"GPIO state: ", gpio.input(12))
	file1.write(str(gpio.input(12))+"\n")
	if int(gpio.input(12) != int(button)):
		button = int(gpio.input(12))
		counter = counter+1
	if counter >= 20:
		pwm.stop()
		gameover()
		print("Thanks for Playing")
		file1.close()
		break
