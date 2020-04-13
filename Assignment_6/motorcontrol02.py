import RPi.GPIO as gpio
import time


def init_pins():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31,gpio.OUT) #IN1
	gpio.setup(33,gpio.OUT) #IN2
	gpio.setup(35,gpio.OUT) #IN3
	gpio.setup(37,gpio.OUT) #IN4
	#gpio.setup(36,False)


def gameover():
	#set all pins low
	gpio.setup(31 , False)
	gpio.setup(33,False)
	gpio.setup(35,False)
	gpio.setup(37,False)
	gpio.cleanup()



def forward(tf):
	# init()
	#Left wheels
	gpio.output(31,True)
	gpio.output(33,False)
	#Right Wheels
	gpio.output(35,False)
	gpio.output(37,True)
	#Wait
	time.sleep(tf)
	#Send all pins low & cleanup
	# gameover()
	# gpio.cleanup()


def reverse(tf):
	# init()
	#Left wheels
	gpio.output(31,False)
	gpio.output(33,True)
	#Right Wheels
	gpio.output(35,True)
	gpio.output(37,False)
	#Wait
	time.sleep(tf)
	#Send all pins low & cleanup
	# gameover()
	# gpio.cleanup()



def left(tf):
	# init()
	#Left wheels
	gpio.output(31,False)
	gpio.output(33,True)
	#Right Wheels
	gpio.output(35,False)
	gpio.output(37,True)
	#Wait
	time.sleep(tf)
	#Send all pins low & cleanup
	# gameover()
	# gpio.cleanup()


def right(tf):
	# init()
	#Left wheels
	gpio.output(31,True)
	gpio.output(33,False)
	#Right Wheels
	gpio.output(35,True)
	gpio.output(37,False)
	#Wait
	time.sleep(tf)
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

