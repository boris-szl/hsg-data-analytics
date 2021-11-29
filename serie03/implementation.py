import numpy as np
import pandas as pd
import time
from numba import jit



def p_loop(x,coef):
	print("Start loop implementation...")
	total = 0 # Keep track of the sum
	for i, a in enumerate(coef):
		total += (a*(x**i))
		print("Adding the coefficient {} mutiplied by x**{}".format(a,i))
	return total

def p_ma(x, coef):
	print("Start matrix algebra implementation")
	X = np.empty(len(coef))
	print("Create an empty vector of x:\n{}".format(X))
	X[0] = 1
	print("Assign 1 to the first elemen of the vector:\n".format(X))
	X[1:] = x
	print("Assign x to the remaining elements of the vector:\n".format(X))
	X = np.cumprod(X)
	print("Power each x to the appropriate power:\n{}".format(X))
	return np.dot(coef,X)


# measuring performance
def p_loop2(x, coef):
	total = 0
	for i, a in enumerate(coef):
		totale += (a*(x**i))
	return total

def p_ma2(x, coef):
	X = np.empty(len(coef))
	X[0] = 1
	X[1:] = x
	X = np.cumprod(X)
	return np.dot(coef,X)

def main():
	n_coef = 5
	lower_bound = 1
	upper_bound = 50
	sample_coef = np.random.randint(lower_bound, upper_bound, size=n_coef)
	print("The list of coefficients is n {}\n".format(sample_coef))
	eval_x = 2

	loop_output = p_loop(eval_x, sample_coef)
	print("The loop implementation as result {} \n".format(loop_output))

	ma_output = p_ma(eval_x, sample_coef)
	print("The matrix algebra implementaion returns as result {} \n".format(ma_output))

	start = time.time()
	loop_result = p_loop(eval_x,sample_coef)
	end = time.time()
	print("Our loop implementation returns as output {} in {} seconds".format(loop_result,(end-start)))

	start = time.time()
	ma_result = p_ma(eval_x,sample_coef)
	end = time.time()
	print("Our matrix algebra implementation returns as output {} in {} seconds".format(ma_result,(end-start)))
	return 0

	# using numba library
	p_loop_numba = jit(p_loop)
	p_ma_numba = jit(p_ma)

	start = time.time()
	loop_result = p_loop_numba(eval_x, sample_coef)
	end = time.time()
	print("Our JIT loop implementation returns as output {} in {} seconds".format(loop_result,(end-time)))

	# start = time.time()
	# ma_result = p_ma_numba(eval_x, sample_coef)
	# end = time.time()
	# print("Our JIT loop implementation returns as output {} in {} secods".format(ma_result,(end-time)))

	start = time.time()
	loop_result = p_loop_numba(eval_x,sample_coef)
	end = time.time()
	print("Our JIT loop implementation returns as output {} in {} seconds".format(loop_result,(end - start)))









if __name__ == "__main__":
	main()