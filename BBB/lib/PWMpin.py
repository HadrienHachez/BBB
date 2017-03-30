import os.path

class PWMpin:

	def __init__(self):
	
	#Activate PWM pin
	def configurepin(self):
		print("Activating PWM")
		if not os.path.exists('/sys/devices/platform/bone_capemgr.9/slots'):
			with open('sys/devices/platform/bone_capemgr.9/slots', 'w') as file:
				file.write('cape-bone-iio') #test: cape-universaln > /sys/devices/platform/bone_capemgr/slots
				
		with open('sys/devices/platform/ocp/ocp\:P9_14_pinmux/state', 'w') as file:
			file.write('pwm') 
		if os.path.exists('/sys/class/pwm/pwmchip2'):
			with open('/sys/class/pwm/pwmchip2/export', 'w') as file:
				file.write('0')
				
	def setPwm(self)
		print("setting PWM period and duty cycle")
		with open('/sys/class/pwm/pwmchip2/pwm0/period', 'w') as file:
			file.write('1000000000') #period
		with open('/sys/class/pwm/pwmchip2/pwm0/duty_cyvle', 'w') as file:
			file.write('500000000') #dutycycle
			
	def enablePwm(self)
		print("enable pwm")
		with open('/sys/class/pwm/pwmchip2/pwm0/enable', 'w') as file:
			file.write('1')
			
	def disablePwm(self)
		print("disable pwm")
		with open('/sys/class/pwm/pwmchip2/pwm0/enable', 'w') as file:
			file.write('0')
		#with open('/sys/class/pwm/pwmchip2/unexport', 'w') as file:
			#file.write('0')
		