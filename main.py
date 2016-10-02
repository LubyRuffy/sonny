from distance import ultrasonic_read
import interfacing


def main():
	interfacing.init()
	print(ultrasonic_read)

if __name__ == '__main__':
	main()