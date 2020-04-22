import RPi.GPIO as gpio
import time
import numpy as np		


def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31, gpio.OUT)
	gpio.setup(33, gpio.OUT)
	gpio.setup(35, gpio.OUT)
	gpio.setup(37, gpio.OUT)

	gpio.setup(7, gpio.IN, pull_up_down= gpio.PUD_UP)
	gpio.setup(12, gpio.IN, pull_up_down= gpio.PUD_UP)

def gameover():
	gpio.output(31, False)
	gpio.output(33, False)
	gpio.output(35, False)
	gpio.output(37, False)
	
	gpio.cleanup()


init()
counterBR = np.uint64(0)
counterFL = np.uint64(0)

buttonBR = int(0)
buttonFL = int(0)


file1 = open("Encoder_data_3.txt","a")

# Initialize pwm signal to control motor
pwm1 = gpio.PWM(31,50)
pwm2 = gpio.PWM(37,50)
val = 22
pwm1.start(val)
pwm2.start(val)
time.sleep(0.1)

for i in range (0,100000):
	print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
	file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n")

	if int(gpio.input(12) != int(buttonBR)):
		buttonBR = int(gpio.input(12))
		counterBR += 1

	if int(gpio.input(7) != int(buttonFL)):
		buttonFL = int(gpio.input(7))
		counterFL = counterFL+1
	
	if counterFL >= 20:
		pwm1.stop()
		
	if counterBR >=20:
		pwm2.stop()


	if counterBR >=20 and counterFL >=20:	
		gameover()
		print("Thanks for Playing")
		file1.close()
		break
