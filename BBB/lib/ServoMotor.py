#import os.path
#import time
import PWMpin

class ServoMotor:
	 """Servo motor class"""
	
	def __init__(self, pin_name, period_ns, high_impulsetime_ns):
		self.pwmPin = PWMpin.PWMpin(pin_name, period_ns, high_impulsetime_ns)

	def MotorOn(self):
		if not self.pin_name == 'P9_42'
	        	print ('Starting pwm')
				self.pwmPin.configure()
				self.pwmPin.setPwm()
				self.pwmPin.enablePwm()
		else:
			print("This library does not support any other pins than the P9_42 at this time")
			
	 def MotorOff(self):
		if self.pin_name == 'P9_42'
        		print('Turning motor off')
			self.pwmPin.disablePwm()
