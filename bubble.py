from distance import calculate_distance
from interfacing import imu, sweep
from movement import bot_map, direction
from time import sleep
from bitonic import longest_bitonic
from learning import threshold, alpha


crash_flag = 0


def mayday():
    global crash_flag, direction
    distances = [calculate_distance() for sweep.angle in range(-40, 46, 2)]
    sweep.angle = -5
    direction = (-1, 0)
    sleep(3)
    route = longest_bitonic(distances)
    if route < 0:
        direction = (1, -1)
    else:
        direction = (1, 1)
    bot_map(direction)
    crash_flag = 0


def escape():
    global crash_flag, direction
    direction = (0, 0)
    bot_map(direction)  # change to escape
    mayday()


def bubble():
    global crash_flag, direction, threshold, alpha
    readings = imu.get_accel_data()
    data = [readings[key] for key in readings]
    for value in data:
        if abs(value) > 30:
            crash_flag = 1
            escape()
            threshold -= alpha
    if not crash_flag:
        direction = (1, 0)
    bot_map(direction)
