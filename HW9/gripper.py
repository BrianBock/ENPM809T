
import RPi.GPIO as gpio
import time
import cv2
import imutils
import numpy as np


class gripper:
	def __init__(self):
		self.flag=0
		self.min=3.1
		self.max=7
		self.init()

	def init(self):
		gpio.setmode(gpio.BOARD)
		gpio.setup(36,gpio.OUT)
		self.pwm= gpio.PWM(36,50)
		
	def boundcheck(self,dcycle):
		if dcycle >self.max:
			dcycle=self.max
		elif dcycle<self.min:
			dcycle=self.min
		return dcycle

	def grip(self,dcycle):
		dcycle=self.boundcheck(dcycle)
		if self.flag==0:
			self.pwm.start(dcycle)
			self.flag=1
		else:	
			self.pwm.ChangeDutyCycle(dcycle)
#	def kill(self):
#		self.pwm.stop()
	#	gpio.cleanup()
	def __del__(self):
		self.pwm.stop()
		gpio.cleanup()

if __name__ == "__main__":
	mygripper= gripper()
#	mygripper.init()
#	dcycle = "a"
	while True:
		dcycle=input("Enter Duty Cycle:")
		print("ll")
		if dcycle == "p":
			break
		try:
			dcycle=float(dcycle)
		#	time.sleep(1)
			mygripper.grip(dcycle)
		except ValueError:
	#		if not dcycle == "p":
			print("Enter a valid digit")
