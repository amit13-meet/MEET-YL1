def divisors(y):	
		x = 1	
		while (x < y):
			if (y % x == 0):
				print x
				x += 1
	
if __name__ == '__main__':
	n = raw_input("Give me a number ")
	y = int(n)
	divisors(y)
