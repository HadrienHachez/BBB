import PWMpin

class Servo:
	"""ServoMotor Class"""

	def __init__(self, pin_name, period_ns, high_impulsetime_ns):
		self.pin_name = pin_name
		self.pwmPin = PWMpin.PWMpin(pin_name, period_ns, high_impulsetime_ns)

	def MotorOn(self):
		print('Turning Motor On')
		if self.pin_name == 'P9_42':
			self.pwmPin.configurepin()
			self.pwmPin.setPwm()
			self.pwmPin.enablePwm()
		else:
			print("This library doesn't support any other pwm pins than P9_42 at current moment")

	def MotorOff(self):
		if self.pin_name == 'P9_42':
			print('Turning motor Off')
			self.pwmPin.disablePwm()
