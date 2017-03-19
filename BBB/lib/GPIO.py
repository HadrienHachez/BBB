import os.path

class GPIO:
	"""GPIO class used to control a GPIO on BBB"""

	def __init__(self,gpioinout, name, gpionbr):
		self.direction = gpioinout
		self.name = name
		self.number = gpionbr

	def high(self):
		print('GPIO = 1')
		self.configdirection()
		if self.direction == 'out':
			with open("/sys/class/gpio/%s/value"%(self.name), 'w') as file:
				file.write('1')
	def low(self):
		print('GPIO = 0')
		self.configdirection()
		if self.direction == 'out':
			with open("/sys/class/gpio/%s/value"%(self.name), 'w') as file:
				file.write('0')
	def configdirection(self):
		print "GPIO direction = %s"%(self.direction)
		if not os.path.exists("/sys/class/gpio/%s"%(self.name)):
			with open('/sys/class/gpio/export', 'w') as file:
				file.write("%s"%(self.number))
		with open("/sys/class/gpio/%s/direction"%(self.name), "w") as file:
				file.write("%s"%(self.direction)) 
