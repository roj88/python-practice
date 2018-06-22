#!/usr/bin/env python 

import math

def prime_factorization(n):
	max_factor = int(math.sqrt(n))

	factor_list = []

	for i in range(1, max_factor):
		if(n % i ==0):
			factor_list.append(i)

	factor_list

print prime_factorization(100)

# TODO: check for primes