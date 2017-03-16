from gpiozero import Motor, DistanceSensor, AngularServo
from mpu6050 import mpu6050


# ultrasonic
sonar_echo = 15
sonar_trigger = 14
servo_input = 21
motor_rear_1 = 26
motor_rear_2 = 19
motor_front_1 = 13
motor_front_2 = 6

imu = mpu6050(0x68)
imu.set_accel_range(16)
sonar = DistanceSensor(sonar_echo, sonar_trigger)
sweep = AngularServo(servo_input, min_angle=-40, max_angle=45)
motor_rear = Motor(motor_rear_1, motor_rear_2)
motor_front = Motor(motor_front_1, motor_front_2)

sweep.angle = -5
