import RPi.GPIO as gpio
import time

in1=31
in2=33
in3=35
in4=37

def init_pins():
	gpio.setmode(gpio.BOARD)
	gpio.setup(in1,gpio.OUT) #IN1
	gpio.setup(in2,gpio.OUT) #IN2
	gpio.setup(in3,gpio.OUT) #IN3
	gpio.setup(in4,gpio.OUT) #IN4
	#gpio.setup(36,False)


def gameover():
	#set all pins low
	gpio.setup(in1, False)
	gpio.setup(in2, False)
	gpio.setup(in3, False)
	gpio.setup(in4, False)
	gpio.cleanup()


def stop_wheels():
	gpio.output(in1,False)
	gpio.output(in2,False)
	gpio.output(in3,False)
	gpio.output(in4,False)


def forward(tf):
	# init()
	#Left wheels
	gpio.output(in1,True)
	gpio.output(in2,False)
	#Right Wheels
	gpio.output(in3,False)
	gpio.output(in4,True)
	#Wait
	time.sleep(tf)

	stop_wheels()
	#Send all pins low & cleanup
	# gameover()
	# gpio.cleanup()


def reverse(tf):
	# init()
	#Left wheels
	gpio.output(in1,False)
	gpio.output(in2,True)
	#Right Wheels
	gpio.output(in3,True)
	gpio.output(in4,False)
	#Wait
	time.sleep(tf)

	stop_wheels()
	#Send all pins low & cleanup
	# gameover()
	# gpio.cleanup()



def left(tf):
	# init()
	#Left wheels
	gpio.output(in1,False)
	gpio.output(in2,True)
	#Right Wheels
	gpio.output(in3,False)
	gpio.output(in4,True)
	#Wait
	time.sleep(tf)

	stop_wheels()
	#Send all pins low & cleanup
	# gameover()
	# gpio.cleanup()


def right(tf):
	# init()
	#Left wheels
	gpio.output(in1,True)
	gpio.output(in2,False)
	#Right Wheels
	gpio.output(in3,True)
	gpio.output(in4,False)
	#Wait
	time.sleep(tf)

	stop_wheels()
	#Send all pins low & cleanup
	# gameover()
	# gpio.cleanup()




#forward(2)
#reverse(2)
#left(2)
#right(2)

def key_input(event):
	# init_pins()
	print("Key: " ,event)
	key_press = event
	tf=1
	if key_press.lower() == 'w':
		forward(tf)
	elif key_press.lower() == 's':
		reverse(tf)
	elif key_press.lower() == 'a':
		left(tf)
	elif key_press.lower() == 'd':
		right(tf)
	else:
		print("Invalid")
		#gameover()
		#gpio.cleanup()

#while True:
#	key_press = input("Select driving mode:")
#	if key_press =='p':
#		break
#	key_input(key_press)

