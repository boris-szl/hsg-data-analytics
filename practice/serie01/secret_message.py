import random
import numpy as np
import math


def decrypt(encrypted_msg):
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	decrypted_msg = ""
	for i, n in enumerate(encrypted_msg):
		for j in range(len(alphabet)):
			if isinstance(n,int):
				sqrt_n = math.sqrt(n)
				if sqrt_n == j:
					encrypted_msg[i] = alphabet[j-1]
			else:
				pass
	for s in encrypted_msg:
		decrypted_msg += s
	return decrypted_msg


def encrypted_msg(message):
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	encrypted_msg = list(message)
	for i, n in enumerate(encrypted_msg):
		for j, m in enumerate(alphabet):
			if n == m:
				encrypted_msg[i] = pow(j+1,2)
			else:
				pass
	return encrypted_msg




def main():

	message = [4, 1, 324, 9, 25, 144, 225, 196, 1, ' ', 81, 361, ' ', 36, 1, 196, 400, 1 ,361, 400, 81, 9]
	print(decrypt(message))
	print(encrypted_msg("barcelona is fantastic"))
	print(encrypted_msg("fuck you"))
	print(decrypt(encrypted_msg("fuck you")))
git 

if __name__ == "__main__":
	main()
	