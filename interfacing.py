#import pigpio
from gpiozero import DistanceSensor,Motor,AngularServo

#pi = pigpio.pi()

# ultrasonic
echo = 15
trigger = 14

sensor = DistanceSensor(echo, trigger)

#motor
rear_motor = Motor(26,19)
front_motor = Motor(13,6)

#servo
servo = AngularServo(21,max_angle=90,min_angle=-90)

# def init():
#     # initialize pins
#     pi.write(trigger, 0)