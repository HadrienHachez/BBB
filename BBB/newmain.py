from lib import Servo
import time

print('ok')
servoSG90 = Servo.Servo('P9_42','20000000','2000000')
print('ok1')
servoSG90.MotorOn()
time.sleep(15)
servoSG90.MotorOff()
print('ok2')
