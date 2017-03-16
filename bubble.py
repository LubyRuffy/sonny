from distance import calculate_distance
from interfacing import imu, sweep
from movement import bot_map, direction
from time import sleep
from bitonic import longest_bitonic
from perceptron import learn, crash_flag
from perceptron import values


def mayday():
    global crash_flag, direction
    direction = (-1, 0)
    sleep(3)
    distances = [calculate_distance() for sweep.angle in range(-40, 46, 2)]
    sweep.angle = -5
    route = longest_bitonic(distances)
    if route < 0:
        direction = (1, -1)
    else:
        direction = (1, 1)
    crash_flag = 0
    bot_map(direction)
    

def escape():
    global direction
    direction = (0, 0)
    bot_map(direction)  # change to escape
    mayday()


def bubble():
    global crash_flag, direction, values
    readings = imu.get_accel_data()
    data = [readings[key] for key in readings]
    for value in data:
        if abs(value) > 30:
            crash_flag = 1
            values['threshold'] -= values['alpha']
            escape()
    if not crash_flag:
        direction = (1, 0)
        learn(calculate_distance())
    bot_map(direction)
    