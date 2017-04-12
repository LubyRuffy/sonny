from distance import calculate_distance
from interfacing import imu, sweep
from movement import bot_map, direction
from time import sleep
from bitonic import longest_bitonic
from perceptron import learn, crash_flag, values
from scipy.signal import medfilt
from collections import deque

imu_buffer = deque([],10)

def mayday():
    global crash_flag, direction
    direction = (-1, 0)
    bot_map(direction)
    sleep(3.5)
    direction = (0, 0)
    bot_map(direction)
    sleep(1)
    distances = [calculate_distance() for sweep.angle in range(-40, 46)]
    sweep.angle = -5
    route = longest_bitonic(distances)
    if route > 42:
        direction = (1, -1)
        print "Optimal path: Left"
    else:
        direction = (1, 1)
        print "Optimal path: Right"
    bot_map(direction)
    sleep(5)
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
    readings = readings[0::2]
    readings = medfilt(readings)
    for value in readings:
        if value > 7:  #tune this
            print "Crash detected. Tuning weights and rerouting."
            imu_buffer.clear()
            imu_buffer.append(0)
            value = 0
            values['threshold'] += values['alpha']
            crash_flag = 1
            escape()
    if not crash_flag:
        direction = (1, 0)
        if learn(calculate_distance()):
            escape()
    dump = open('dump.txt', 'w')
    dump.write(str(values))
    dump.close()
    bot_map(direction)
