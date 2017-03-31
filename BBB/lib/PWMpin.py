import os.path

class PWMpin:

	def __init__(self,name, period_ns, impulsetime_ns):
		self.name = name
		self.period = period_ns
		self.dutycycle = impulsetime_ns
	
	#Activate PWM pin
	def configurepin(self):
		print("Activating PWM")
		if not os.path.exists('/sys/devices/platform/bone_capemgr/slots'):
			with open('/sys/devices/platform/bone_capemgr/slots', 'w') as file:
				file.write('cape-universaln') #test: cape-universaln or  cape-bone-iio  				
		with open("/sys/devices/platform/ocp/ocp:%s_pinmux/state"%(self.name), 'w') as file:
			file.write('pwm') #config-pin P9.42 pwm
		if not os.path.exists('/sys/class/pwm/pwmchip6/pwm0'):
			with open('/sys/class/pwm/pwmchip6/export', 'w') as file:
				file.write('0') #export pwm0, module ECAP0 at addr 48300100, one of few models that can take different period & dutycycles on BBB
				
	def setPwm(self):
		print("setting PWM period and duty cycle")
		with open('/sys/class/pwm/pwmchip6/pwm0/period', 'w') as file:
			file.write("%s"%(self.period)) #period de 20 ms comme indique dans le datasheet,(unit = ns)
		with open('/sys/class/pwm/pwmchip6/pwm0/duty_cycle', 'w') as file:
			file.write("%s"%(self.dutycycle)) #impulsion de 2ms == Position '90' du serveur moteur SG90
			
	def enablePwm(self):
		print("enable pwm")
		with open('/sys/class/pwm/pwmchip6/pwm0/enable', 'w') as file:
			file.write('1') #lancez pwm
			
	def disablePwm(self):
		print("disable pwm")
		with open('/sys/class/pwm/pwmchip6/pwm0/enable', 'w') as file:
			file.write('0') #arretez pwm
		#with open('/sys/class/pwm/pwmchip2/unexport', 'w') as file:
			#file.write('1')
