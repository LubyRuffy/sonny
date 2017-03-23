from distance import calculate_distance
from interfacing import imu, sweep
from movement import bot_map, direction
from time import sleep
from bitonic import longest_bitonic
from perceptron import learn, crash_flag
from perceptron import values

data_old = [10, 10]

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
    if route > 0:
        direction = (1, -1)
    else:
        direction = (1, 1)
    bot_map(direction)
    sleep(2)
    crash_flag = 0


def escape():
    global direction
    direction = (0, 0)
    bot_map(direction)  # change to escape
    mayday()


def bubble():
    global crash_flag, direction, values, data_old
    readings = imu.get_accel_data()
    data = [readings[key] for key in readings]
    for value in range(len(data) - 1):
        if (abs((abs(data[value]) - abs(data_old[value]))) > 25) \
                or (calculate_distance() < 5):
            crash_flag = 1
            values['threshold'] += values['alpha']
            escape()
    if not crash_flag:
        direction = (1, 0)
        learn(calculate_distance())
    data_old = data
    dump = open('dump.txt', 'w')
    dump.write(str(values))
    dump.close()
    bot_map(direction)
