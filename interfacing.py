from gpiozero import Motor, DistanceSensor, AngularServo
from MPU6050 import MPU6050

# ultrasonic
sonar_echo = 15
sonar_trigger = 14
servo_input = 21
motor_rear_1 = 26
motor_rear_2 = 19
#motor_front_1 =
#motor_front_2 =

imu = MPU6050(0x68)
sonar = DistanceSensor(sonar_echo,sonar_trigger)
sweep = AngularServo(servo_input,min_angle=-40,max_angle=45)
motor_rear = Motor(motor_rear_1,motor_rear_2)
#motor_front = Motor(motor_front_1,motor_front_2)