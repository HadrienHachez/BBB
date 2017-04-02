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
#led.On()
#led.Off()
print("ok3")
