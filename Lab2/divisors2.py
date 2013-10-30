def divisors(n):	
		x = 1	
		while (x < int(n)):
			if (int(n) % x == 0):
				print x
				x += 1
	
if __name__ == '__main__':
	n = raw_input("Give me a number ")
	divisors(int(n))
