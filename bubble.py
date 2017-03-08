from distance import calculate_distance
from math import pow
from random import random
from interfacing import imu
from movement import bot_map, direction


crash_flag = 0


def escape():
    global crash_flag, direction, count
    count += 1
    print count
    direction = (0, 0)
    bot_map(direction)  # change to escape


def bubble():
    global crash_flag, direction
    readings = imu.get_accel_data()
    data = [readings[key] for key in readings]
    for value in data:
        if abs(value) > 30:
            crash_flag = 1
            escape()
    if not crash_flag:
        direction = (1, 0)
    bot_map(direction)
