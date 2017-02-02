from gpiozero import Motor, DistanceSensor

# ultrasonic
echo = 15
trigger = 14

sonar = DistanceSensor(echo,trigger)