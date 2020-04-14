
import RPi.GPIO as gpio

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31,gpio.OUT)
	gpio.setup(33,gpio.OUT)
	gpio.setup(35,gpio.OUT)
	gpio.setup(37,gpio.OUT)
	gpio.setup(36,gpio.OUT)
def gameover():
	gpio.output(31,False)
	gpio.output(33,False)
	gpio.output(35,False)
	gpio.output(37,False)
	gpio.output(36,False)
init()
gameover()
gpio.cleanup()
