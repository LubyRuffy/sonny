from interfacing import motor_rear, motor_front

linear = 0
turn = 0


direction = (linear, turn)


def bot_stop():
    motor_front.forward(0)
    motor_rear.forward(0)


def bot_forward(turn_flag):
    if turn_flag == 0:
        motor_front.forward(0)
    elif turn_flag == 1:
        motor_front.forward(1)
    else:
        motor_front.backward(1)
    motor_rear.forward(0.3)


def bot_backward(turn_flag):
    if turn_flag == 0:
        motor_front.forward(0)
    elif turn_flag == 1:
        motor_front.forward(1)
    else:
        motor_front.backward(1)
    motor_rear.backward(0.3)


def bot_map(direction):
    if direction[linear] == 0:
        bot_stop()
    elif direction[linear] == 1:
        bot_forward(direction[turn])
    else:
        bot_backward(direction[turn])
