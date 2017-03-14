from random import random, seed

def init(): # first time write to file
	dump = open('dump.txt', 'w')
	values = {'count' : 0, 'weight' : random(), \
	'threshold' : 0, 'flag' : 0, 'alpha' : 0.05}
	val_list = list(values.items())
	dump.write(val_list)
	dump.close()


def learn(distance):
	dump = open('dump.txt', 'r')
	#  read file
	values = dump.readlines()
	
	product = values[distance] * values[weight]
	print product
	
	if(product<threshold and distance==1.5):
		print "Stopped at "+str(distance)
		flag=1
	if not flag:
		threshold += 0.1
		print threshold