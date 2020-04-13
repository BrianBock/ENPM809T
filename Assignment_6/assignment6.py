

import time
import os
import sys
import cv2
import glob
import gripper
import sodar
import motorcontrol02 as drive

mygripper=gripper.gripper()
#mygripper.init()
key_press="a"
#dcycle = "a"

drive.init_pins()

while not key_press == "p":
	dcycle=input("Enter d cycle of gripper")
	try:
		dcycle=float(dcycle)
		mygripper.grip(dcycle)
		time.sleep(1)
	except ValueError:
		if not dcycle == "p":
			print("Enter a valid digit") 

	key_press = input("Select driving mode:")
	
	if not key_press =="p":
		drive.key_input(key_press)

		#print("Distance: "+str(sodar.distance()))

print("Clearing pins and exiting")
drive.gameover()
