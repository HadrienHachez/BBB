import os.path
import LED
import GPIO
#import time

print('ok1')
led = LED.LED('gpio60','60')
#gpio = GPIO.GPIO('out','gpio60','60')
print('ok2')
#gpio.low()
led.Toggle(1)
# Activate GPIO P9_12
print("ok3")

#if os.path.exists('/sys/class/gpio/gpio60'):
	#print("ok3")
	#with open('/sys/class/gpio/export', 'w') as file:
		#file.write('60')
	#with open('/sys/class/gpio/gpio60/direction', 'w') as file:
		#file.write('out')
	#with open('/sys/class/gpio/gpio60/value', 'w') as file:
		#file.write('0')
