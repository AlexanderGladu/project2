import sys

def run():
	input = None
	try:
		input = sys.argv[1]
	except:
		input = 'blah'
	print input

if (__name__ == "__main__"):
	run()