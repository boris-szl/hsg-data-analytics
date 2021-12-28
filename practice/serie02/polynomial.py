import numpy as np
import pandas as pd

def main():
	# netiher using numpy or pandas
	vector1 = []
	exp = []
	polynomial = []
	n = input("Size of vector: ")
	n = int(n)
	# scan coefficients for vector size n
	while (len(vector1) < n):
		for i in range(n):
			coefficient = input((f'v[{i}] = '))
			coefficient = int(coefficient)
			vector1.append(coefficient)
	# print vector coefficients for size n
	print(vector1)
	# set variable x
	x = input("Let x = ")
	x = int(x)
	for j in range(n):
		exp.append(x**j)
		print(exp)
	# compute polynomial
	total = 0
	count = 0
	for i in vector1:
		total = i*x**count
		polynomial.append(total)
		count += 1
	print(polynomial)



	# using numpy
	# we actually dont need to invoke the np.array() method on the list
	polynomial = np.cross(vector1, exp)
	print(polynomial)
	# np.array creates a one dimensional vector
	# vector2 = np.array([vector1])
	# exp2 = np.array([exp])
	# print(exp2.ndim)
	# print(vector2.ndim)

	
	
	x = [1,2,3]
	y = [2,4,2]
	result = np.cross(x,y)
	print(result)

	# result = np.cross(vector2,exp2)
	# result2 = np.cross(vector2,np.transpose(exp2))
	# print(result)
	# print(result2)


if __name__ == "__main__":
	main()

# Testing
# Complexity O(n)
# Complexity = Anzahl der Operationen (Vergleich, Zuweisung (ausser 0), mathematische Operation)