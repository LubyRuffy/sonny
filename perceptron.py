from random import random, seed
from ast import literal_eval
from movement import bot_map, direction

crash_flag = 0

seed()
values = {'weight': random(), 'threshold': 0, 'alpha': 30}


def init():  # first time write to file
    global values
    dump = open('dump.txt', 'w')
    dump.write(str(values))
    dump.close()


def learn(distance):
    global direction, values
    print values
    # dump = open('dump.txt', 'r')
    # #  read file
    # values = literal_eval(dump.read())
    # dump.close()
    weight = values['weight']
    threshold = values['threshold']
    product = distance * weight
    if product < threshold:
        print "Crash predicted. Commencing pre-emptive rerouting."
        direction = (0, 0)
        bot_map(direction)
        return 1
    else:
        return 0
