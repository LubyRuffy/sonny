from interfacing import sonar
from time import sleep

def calculate_distance():
    dist = round(sonar.distance*100,2)
    sleep(0.2)
    return dist