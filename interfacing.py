import pigpio

pi = pigpio.pi()

# ultrasonic
echo = 15
trigger = 14

def init():
    # initialize pins
    pi.write(trigger, 0)