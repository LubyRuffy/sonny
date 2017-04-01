from distance import calculate_distance
from interfacing import imu, sweep
from movement import bot_map, direction
from time import sleep
from bitonic import longest_bitonic
from perceptron import learn, crash_flag
from perceptron import values
from scipy.signal import medfilt
from copy import deepcopy
from collections import deque

imu_buffer = deque([],5)

def mayday():
    global crash_flag, direction
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
    sleep(2)
    crash_flag = 0


def escape():
    global direction
    direction = (0, 0)
    bot_map(direction)
    mayday()


def bubble():
    global crash_flag, direction, values, imu_buffer
    imu_buffer.append(imu.get_accel_data()['x'])
    readings = [abs(data) for data in imu_buffer]
    readings = medfilt(readings)
    for value in readings:
        if value > 6:  #  tune this
            imu_buffer.clear()
            imu_buffer.append(0)
            value = 0
            values['threshold'] += values['alpha']
            crash_flag = 1
            escape()
    if not crash_flag:
        direction = (1, 0)
        learn(calculate_distance())
    dump = open('dump.txt', 'w')
    dump.write(str(values))
    dump.close()
    bot_map(direction)
