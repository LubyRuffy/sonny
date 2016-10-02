from pigpio import RISING_EDGE, FALLING_EDGE
import interfacing
from interfacing import pi

start_time=0
stop_time=0

# get start tick
def echo_start():
    global start_time
    start_time = pi.get_current_tick()


# get stop tick
def echo_stop():
    global stop_time
    stop_time = pi.get_current_tick()


# calculate distance
def ultrasonic_read():
    
    # trigger on
    trigger_on_time = pi.get_current_tick()
    pi.write(interfacing.trigger, 1)
    
    # delay for 10 us before turning trigger back off
    while (trigger_on_time >= (pi.get_current_tick() - 10)):
        pass
    pi.write(interfacing.trigger, 0)
    
    # reading echo
    pi.callback(
        interfacing.echo, RISING_EDGE, echo_start())
    pi.callback(interfacing.echo, FALLING_EDGE, echo_stop())
    
def calculate_distance():
    ultrasonic_read()
    round_trip_time = (stop_time - start_time)
    
    # calculating distance
    distance = 17150 * round_trip_time
    
    return distance