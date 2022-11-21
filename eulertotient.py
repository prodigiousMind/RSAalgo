#!/usr/bin/python3

import sys

# to check whether n is prime or not
def isPrime(n):
	
	'''In order to check primality, we need to find whether any number from 2 to n/2 divides n or not
		if it divides, then simply return 0 (not prime) else prime (return 1)'''
	
	for num in range(2, n//2+1):
		if n % num == 0:
			return 0
	else:
		return 1

def findAllPrime(n):
	
	'''this function produce a list of all prime numbers under a number n, if a number is found prime then it is appended to the list'''

	listOfPrime = [] # less than the number
	for num1 in range(2, n//2+1):
		isIt = isPrime(num1)
		if isIt == 1:
			listOfPrime.append(num1)
	return listOfPrime

def generateListOfPrime(listOfPr, num):
	
	'''this function try to find whether a product of two prime number is equal to number "num" by multiplying the smallest (to largest)
	with the largest (to smallest) using sorted (asc and desc list of numbers) in the list of all prime numbers less than the given number'''

	listOfPr = listOfPr
	listOfPrRev = listOfPr[::-1]

	for start in listOfPr:
		for end in listOfPrRev:
			if ((start * end == num) and (start != end)):
				return (start, end)

	else:
		return 2

def greatestCommonDivisor(num):
	
	'''This function finds all the number under num with gcd equal to 1, simply means, relatively-prime with number num
	if a number has gcd of 1 with the number num, it means, it is co-prime with num and appended to the euler's totient function'''
	
	listOfCoPrime = [1]
	for n in range(2, num):
		if num % n != 0:
			n1 = n//2
			for n2 in range(2, n1+1):
				if (n % n2 == 0 and num % n2 == 0):
					break
			else:
				listOfCoPrime.append(n)
	return listOfCoPrime

# if number is passed in CLI as argument
if len(sys.argv) == 2 and sys.argv[1].isdigit():

	number = int(sys.argv[1])
	
	# if num is a prime number (not divisible by any number execpt 1 or itself)
	is_prime = isPrime(number) # calling isPrime function with number

	# if the number is prime, the called function returns 1 else 0
	# if it is prime, then euler's totient function for a prime number is n-1 (n is number)
	if is_prime == 1: 
		
		et = number - 1
		print("Euler's totient function is {}".format(et))
	
	else:
		# if it is not prime then call findAllPrime function
		# the below line saves the return list of the function in a variable
		# this is to check whether we can pair any two prime numbers to compute the result equal to the number
		# if product of two prime number (p1, p2) is equal to a number n, then n has (p1-1) * (p2-1) euler's totient function

		listOfAllPrime = findAllPrime(number)

		# the below line saves the return result, whether two prime product == number

		case1Or2 = generateListOfPrime(listOfAllPrime, number)

		# if p1 * p2 == number, it means we can simply calculate euler's totient function
		# if return type is tuple, it means, product of two prime numbers is equal to the given number
		# else, we need to calculate each number from 1 upto number to find the gcd of equal to 1 (co-prime/relatively prime)
		
		if type(case1Or2) == tuple:
			
			firstPrime, secondPrime = case1Or2[0], case1Or2[1]
			et = (firstPrime - 1) * (secondPrime - 1)
			print("Prime number {} * {} = {}".format(firstPrime, secondPrime, number))
			print("Hence, Euler's totient function {} * {} = {}".format(firstPrime-1, secondPrime-1, et))
			print("Euler's totient function of {} is {}".format(number, (et)))

		else:

			# calculating all number 1 upto n with gcd == 1 and save list in a variable

			etList = greatestCommonDivisor(number)
			
			# length of the above list, simply, euler's totient function
			etLen = len(etList)

			print("Euler's totient function of {} is {}".format(number, (etLen)))
			print("Euler's totient function List of {} is {}".format(number, (etList)))


else:
	print("""Help [USAGE]:\npython3 eulertotient.py [INTEGER])""")

