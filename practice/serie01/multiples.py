import random
import numpy as np







# Function that checks if a number x is a multiple of y
def gen_random_list(size_list,lower_limit,upper_limit):
	rand_list = []
	for i in range(0,size_list):
		rand_list.append(np.random.randint(lower_limit,upper_limit))
	return rand_list

def check_multiple(x,y):
	if x%y == 0:
		return 1
	else:
		return 0

def parity(y):
	if y > 0:
		return 1
	else:
		return 0

def main():
	n = int(input("Enter an arbitrary number n:\n"))

	list2 = gen_random_list(10,-10,10)
	print(list2)

	for i in list2:
		if parity(i) == 1:
			if check_multiple(i,n) == 1:
				print(f'{i} is a multiple of {n}')
			else:
				pass
		else:
			pass

if __name__ == "__main__":
	main()