import random

def comp(a, b):
	if (a > b):
		return 1
	elif (a == b):
		return 0
	else:
		return -1
# For number of total outputs
output = 0

for i in range(1, 200):
	if (i % 2 == 0 and i % 3 == 0):
		x = i * 3.5
		r = random.random()
		if (r < 0.5):
			y = i * 5
			print ("Ouput: %2s" % (comp(x, y)))
			output += 1
		else:
			y = i * 2
			print ("Ouput: %2s" % (comp(x, y)))
			output += 1

print ("Number of outputs: %s" % (output))