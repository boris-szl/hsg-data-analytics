



# Author: Szelcsanyi
# Date created: 20/11/2021
# Last updated: 20/11/2021


# faculty of any number of the set of natural numbers
# := n! = n * (n-1)!

def check_positive_input(n):
	if n < 0:
		print("Only positive numbers allowed")


# factorial by introducing a foor loop
def factorial_1(n):
	fac = 1
	for i in range(1,n+1):
		fac = fac * i
	return fac

# this funciton ulitzes a while-loop for calcualting
# the factorial
def factorial_2(n):
	fac = 1
	i = 1
	while i<n+1:
		fac = fac * i
		i += 1
	return fac

def factorial_3(n):
	# assert n>=0, 'Only positive numbers are allowed'
	if n <= 1:
		return 1
	else:
		return n * factorial_3(n-1)


def main():
	n = input("Please enter an arbitrary integer:\n")
	n = int(n)

	print(f'(Using for loop) Factorial of {n} = {factorial_1(n)}')
	print(f'(Using while loop) Factorial of {n} = {factorial_2(n)}')
	print(f'(Using recursion) Factorial of {n} = {factorial_3(n)}')


if __name__ == "__main__":
	main()



''' Testing
for 0 and 1
for negative numbers
for doubles / floats
for very big numbers
'''