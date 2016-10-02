import interfacing


# get start tick
def echo_start():
    echo_start_time = pi.get_current_tick()
    return echo_start_time


# get stop tick
def echo_stop():
    echo_stop_time = pi.get_current_tick()
    return echo_stop_time


# calculate distance
def ultrasonic_read():
    
    # trigger on
    trigger_on_time = pi.get_current_tick()
    pi.write(interfacing.trigger, 1)
    
    # delay for 10 us before turning trigger back off
    while (trigger_on_time >= (pi.get_current_tick() - 10))
    pi.write(interfacing.trigger, 0)
    
    # reading echo
    start_time = pi.callback(
        interfacing.echo, pigpio.RISING_EDGE, echo_start())
    stop_time = pi.callback(interfacing.echo, pigpio.FALLING_EDGE, echo_stop())
    
    round_trip_time = (stop_time - start_time)
    
    # calculating distance
    distance = 17150 * round_trip_time
    
    return distance