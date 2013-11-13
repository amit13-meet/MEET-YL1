import random

def flip():
	x = 0 
	while (x < int(times)):
		n = random.randint(0,1)
		if (n == 0):
			print "Heads"
		else:
			print "Tails"
		x += 1

if __name__ == '__main__':
	times = raw_input("How many times should I flip the coin? ")
	flip()
