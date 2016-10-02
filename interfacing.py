import pigpio

pi = pigpio.pi()

# ultrasonic
echo = 1
trigger = 2

def init():
    # initialize pins
    pi.write(trigger, 0)