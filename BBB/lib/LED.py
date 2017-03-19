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
			# Ativate ADC
			#if os.path.exists('/sys/devices/bone_capemgr.9/slots'):
				#with open('/sys/devices/bone_capemgr.9/slots', 'w') as file:
					#file.write('cape-bone-iio')
				#with open('/sys/devices/ocp.3/helper.15/AIN0', 'r') as file:
					#value = (1799 / int(file.read())) / 100.0
				self.ledgpio.high()
				time.sleep(value)
				self.ledgpio.low()
				time.sleep(value)
