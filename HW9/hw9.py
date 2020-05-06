import time
import os
import sys
import cv2
import gripper
import sodar
import imutils
import motorcontrol02 as drive
import imu02 as imu
import RPi.GPIO as gpio
from picamera.array import PiRGBArray
from picamera import PiCamera


mygripper = gripper.gripper()
drive.init_pins()
sodar.init_spins()

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 30
rawCapture = PiRGBArray(camera , size = (640,480))
time.sleep(0.1)

# define HSV mask for Blue
lower_B = (89, 78 , 64)
upper_B = (161,255,255)

mygripper.grip(7)
time.sleep(1)
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=False):
	img = frame.array
	time.sleep(0.1)
	img=cv2.flip(img,0)
	img=cv2.flip(img,1)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv , lower_B, upper_B)
	cnt = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnt = imutils.grab_contours(cnt)

	font = cv2.FONT_HERSHEY_SIMPLEX
	coord = (50,50)
	fontscale = 0.5
	color =(255,255,255)
	thickness = 1

	if len(cnt)>0:
		cn = max(cnt, key= cv2.contourArea)
		((x,y),radius) = cv2.minEnclosingCircle(cn)

		M = cv2.moments(cn)
		if(M["m00"] > 0):
			x = int(M["m10"] / M["m00"])
			y = int(M["m01"] / M["m00"])
		contoured= cv2.circle(img, (x,y), int(radius) ,(0,255,0),5)
		contoured= cv2.circle(contoured, (x,y), 1,(0,255,0),3)
		cv2.putText(contoured,'('+str(x)+','+str(y)+')',coord,font,fontscale,color,thickness,cv2.LINE_AA)
		c=cv2.line(contoured,(320,200),(320,280),(255,255,255),1)
		c=cv2.line(c,(280,240),(360,240),(255,255,255),1)
		#cv2.imshow("cont",c)
		key = cv2.waitKey(1) & 0xFF
	else:
		contoured = img
		cv2.imshow(contoured)

		#cv2.waitKey(0)
	rawCapture.truncate(0)

	if x>=320:
		angle = (x-320)*0.061
		imu.right(angle)

	else:
		angle = (320-x)*0.061
		imu.left(angle)
	if key == ord("q"):
		break
imu.gameover()
#cv2.destroyAllWindows()
