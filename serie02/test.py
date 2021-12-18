import numpy as np
import pandas as pd




def main():
	list1 = [3,7,4]
	list2 = [3,9,8]

	A = np.array(list1)
	A2 = np.array([2,3])
	B = np.array(list2)
	B2 = np.array([1,4])

	print(A.ndim)
	print(A2.ndim)
	print(B.ndim)
	print(B2.ndim)

	AxB = np.cross(A,B)
	print(AxB)

	# transpose B
	B_transposed = np.transpose(B)
	print(B_transposed)

	return 0












if __name__ == "__main__":
	main()