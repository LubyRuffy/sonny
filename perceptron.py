from random import random, seed
from json import loads, dumps
from movement import bot_map, direction
from bubble import crash_flag

seed()
turn_radius = 1.5


def init():  # first time write to file
    dump = open('dump.txt', 'w')
    values = {'count': 0, 'weight': random(),
              'threshold': 0, 'flag': 0, 'alpha': 0.05}
    values = dumps(values)
    dump.write(values)
    dump.close()


def learn(distance):
    global direction
    dump = open('dump.txt', 'r')
    #  read file
    values = dump.read()
    dump.close()

    values = loads(values)
    product = distance * values['weight']
    print product
    if(product < values['threshold'] or distance <= turn_radius):
        direction = (0, 0)
        bot_map(direction)
