import os.path

class PWMpin:

	def __init__(self):pass
	
	#Activate PWM pin
	def configurepin(self):
		print("Activating PWM")
		if not os.path.exists('/sys/devices/platform/bone_capemgr/slots'):
			with open('/sys/devices/platform/bone_capemgr/slots', 'w') as file:
				file.write('cape-bone-iio') #test: cape-universaln or  cape-bone-iio  				
		with open('/sys/devices/platform/ocp/ocp:P9_16_pinmux/state', 'w') as file:
			file.write('pwm') 
		if os.path.exists('/sys/class/pwm/pwmchip2/export'):
			with open('/sys/class/pwm/pwmchip2/export', 'w') as file:
				file.write('1')
				
	def setPwm(self):
		print("setting PWM period and duty cycle")
		with open('/sys/class/pwm/pwmchip2/pwm1/period', 'w') as file:
			file.write('1000000000') #period
		with open('/sys/class/pwm/pwmchip2/pwm1/duty_cycle', 'w') as file:
			file.write('500000000') #dutycycle
			
	def enablePwm(self):
		print("enable pwm")
		with open('/sys/class/pwm/pwmchip2/pwm1/enable', 'w') as file:
			file.write('1')
			
	def disablePwm(self):
		print("disable pwm")
		with open('/sys/class/pwm/pwmchip2/pwm1/enable', 'w') as file:
			file.write('0')
		with open('/sys/class/pwm/pwmchip2/unexport', 'w') as file:
			file.write('1')
