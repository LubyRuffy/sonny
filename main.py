from bubble import bubble
from perceptron import init
from movement import bot_stop


def main():
    bubble()


if __name__ == '__main__':
    bot_stop()
    init()
    while True:
        main()
