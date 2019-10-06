import RPi.GPIO as GPIO
import time

channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def transparent(pin):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(1)

def opaque(pin) :
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
	
def cleanup():
	GPIO.cleanup()
	

# Instructions to connect the circuit 
	# 1) connect GPIO 21, VCC and GND to respective pins on 5V relay
	# 2) connect positive terminals (one from adapter and other from ESG to NO pin and COM )
	# 3) the other pin is for gnd , (just don't cut the negatives)