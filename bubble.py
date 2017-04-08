from distance import calculate_distance
from interfacing import imu, sweep, reroute_flag
from movement import bot_map, direction
from time import sleep
from bitonic import longest_bitonic
from perceptron import learn, crash_flag, values
from scipy.signal import medfilt
from collections import deque

imu_buffer = deque([],10)

def mayday():
    global crash_flag, direction, reroute_flag
    direction = (-1, 0)
    bot_map(direction)
    sleep(1)
    direction = (0, 0)
    bot_map(direction)
    sleep(1)
    distances = [calculate_distance() for sweep.angle in range(-40, 46)]
    sweep.angle = -5
    route = longest_bitonic(distances)
    if route > 42:
        direction = (1, -1)
        print "left"
    else:
        direction = (1, 1)
        print "right"
    bot_map(direction)
    sleep(5)
    crash_flag = 0
    reroute_flag = 0


def escape():
    global direction
    direction = (0, 0)
    bot_map(direction)
    mayday()


def bubble():
    global crash_flag, direction, values, imu_buffer, reroute_flag
    if reroute_flag:
        escape()
    imu_buffer.append(imu.get_accel_data()['x'])
    sleep(0.2)
    readings = [abs(data) for data in imu_buffer]
    readings = readings[0::2]
    print readings
    readings = medfilt(readings)
    for value in readings:
        if value > 5:  #tune this
            print "thoka"
            imu_buffer.clear()
            imu_buffer.append(0)
            value = 0
            values['threshold'] += values['alpha']
            crash_flag = 1
            escape()
    if not crash_flag:
        direction = (1, 0)
        learn(calculate_distance())
        print "reroute_flag "+str(reroute_flag)
    dump = open('dump.txt', 'w')
    dump.write(str(values))
    dump.close()
    bot_map(direction)
