

import time
import os
import sys
import cv2
import glob
import gripper
import sodar
import motorcontrol02 as drive
import RPi.GPIO as gpio
from picamera.array import PiRGBArray
from picamera import PiCamera


today = time.strftime("%y%m%d-%H%M%S")
print(today)
#os.system("sudo mkdir "+ today)
mygripper=gripper.gripper()
#mygripper.init()
key_press="a"
#dcycle = "a"

drive.init_pins()
sodar.init_spins()
camera = PiCamera()
camera.resolution = (1280,720)
camera.framerate= 40
rawCapture = PiRGBArray(camera, size=(1280,720))
time.sleep(0.1)

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('teleop.avi',fourcc,1,(1280,720))
i=0
cd='/home/pi/ENPM809T/Assignment_6/timelapse'
os.chdir(cd)
while not key_press == "p":
	i=i+1
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
		#image = "sudo raspistill -w 1280 -h 720 -hf -vf -o /home/pi/ENPM809T/Assignment_6/" + today + "/" + str(i) + ".jpg"
		#os.system(image)
		camera.capture(rawCapture,format="bgr")
		og = rawCapture.array
		print("Saved Image: ",i)
		time.sleep(0.1)
		og=cv2.flip(og,0)
		#og= cv2.imread(image)
		dcstr="Duty Cycle: %0.1f %%" % dcycle
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(og, dcstr, (10, 40), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
		cv2.imwrite(str(i)+".jpg",og)
		#print("Distance: "+str(sodar.distance()))
		dist=sodar.distance()
		distr="Distance: %0.3f cm "% dist
		cv2.putText(og, distr, (10, 80), font, 1, (0,255, 0), 2, cv2.LINE_AA)
		rawCapture.truncate(0)
		out.write(og)
print("Clearing pins and exiting")
drive.gameover()
