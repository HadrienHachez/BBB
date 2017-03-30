#import os.path
#import time
import PWMpin

class ServoMotor:
    """A simple example class"""
	def __init__(self):
		self.pwmPin = PWMpin.PWMpin()
	
    def MotorOn(self):
        print ('Starting pwm')
			self.configPWMpin()
			self.pwmPin.setPwm()
			self.pwmPin.enablePwm()
			
    def MotorOff(self):
        print('Turning motor off')
			self.pwmPin.disablePwm()
			
	def configPWMpin(self):
        print('Configuring pwm pin')
		self.pwmPin.configure()