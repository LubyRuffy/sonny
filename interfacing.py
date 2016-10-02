import pigpio

# ultrasonic
echo = 1
trigger = 2

def init():
    # gpio initialization
    pi = pigpio.pi()

    # initialize pins
    pi.write(trigger, 0)