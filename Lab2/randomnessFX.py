import random
arr = []

def flip():
        x = 0 
        times = raw_input("How many times should I flip the coin? ")
        while (x < int(times)):
                n = random.randint(0,1)
                if (n == 0):
                        arr.append("Heads")
                else:
                        arr.append("Tails")
                x += 1

flip()
print arr
