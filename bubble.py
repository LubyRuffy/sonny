from distance import calculate_distance
from math import pow
from random import random
from imu import calculate_speed


weight_speed = round(random(), 2)
weight_distance = round(random(), 2)
threshold = round(random(), 2)


bias = (weight_speed * pow(calculate_speed(), 2)) - (
    weight_distance * calculate_distance())


def decision_factor():
    distance_to_obstacle = calculate_distance()
    decision_factor = (weight_speed * pow(calculate_speed(), 2)) / (
        (weight_distance * distance_to_obstacle) + bias)
    return decision_factor


def update_weights():
    global weight_speed
    global weight_distance
    global weight_threshold
    weight_distance -= weight_distance * round(random(), 2)
    weight_speed += weight_speed * round(random(), 2)


def bubble():
    if(threshold<decision_factor()):
        #stop
