from gpiozero import Motor, AngularServo
from time import sleep

sweep = AngularServo(21,min_angle=-40,max_angle=45)
motor = Motor(26,19)

motor.forward(0.1)
sleep(2)
motor.forward(0.3)
sleep(2)
motor.forward(0.4)
sleep(2)
motor.forward(0.6)
sleep(2)
motor.forward(0.8)
sleep(2)
motor.forward(1)
sleep(2)
motor.forward(0)

flag = 1
i=0

for j in range(3):
	while flag:
		sweep.angle=i
		i+=1
		sleep(0.1)
		if i==45:
			flag=0
	while not flag:
		sweep.angle=i
		i-=1
		sleep(0.1)
		if i==-40:
			flag=1