import os.path
import time
import GPIO

class LED:
	"""A simple example class"""
	def __init__(self,gpioname,gpionumber):
		self.ledgpio = GPIO.GPIO('out',gpioname,gpionumber)

	def On(self):
		print('Turning led on')
		self.ledgpio.high()
	def Off(self):
		print('Turning led off')
		self.ledgpio.low()
	def Toggle(self, value):
		while True:
				self.ledgpio.high()
				time.sleep(value)
				self.ledgpio.low()
				time.sleep(value)
