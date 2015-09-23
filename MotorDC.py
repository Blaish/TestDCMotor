import RPi.GPIO as GPIO
import time

def MotorDC (pin17,pin21,pin23,pin24,n=5):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin17, GPIO.OUT)
	GPIO.setup(pin21, GPIO.OUT)
	GPIO.setup(pin23, GPIO.OUT)
	GPIO.setup(pin24, GPIO.OUT)
	for i in xrange(n):
		GPIO.output(pin17, GPIO.HIGH)
		GPIO.output(pin21, GPIO.LOW)
		GPIO.output(pin23, GPIO.HIGH)
		GPIO.output(pin24, GPIO.LOW)
		time.sleep(1)
		
if __name__ == "__main__":
	MotorDC(17,21,23,24)