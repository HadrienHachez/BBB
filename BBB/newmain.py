from lib import Servo
import time

#The PWM signal on the BBB can only be generated when the board
#is supplied with a 5V DC PSU at P1 or on pins P9_5 ou P9_6

print('ok')
servoSG90 = Servo.Servo('P9_42','20000000','2000000')
print('ok1')
servoSG90.MotorOn()
time.sleep(15)
servoSG90.MotorOff()
print('ok2')
