#!/usr/bin/python

import argparse
import sys
import os
import math

def get_arguments():
	try:
		parser=argparse.ArgumentParser()

		inputs = {
            'list_max' : 'max integer to look into',
            }

		for key, value in inputs.items():
			parser.add_argument('--{KEY}'.format(KEY=key), help=value)

		args=parser.parse_args()

		print "Your arguments are the following..."
		print args
		print sys

		return args

    # if there is an error in parsing args
	except:
		print "Could not parse your arugments properly. Exiting program..."
		sys.exit(1)

## parse arguments
args = get_arguments()

def find_primes():
	max_num = int(args.list_max)
	
	a_list = range(2, max_num + 1)

	max_divisor = math.sqrt(max_num)

	for i in range(2, int(max_divisor)):
		for j in a_list:
			if j % i == 0:
				if i != j:
					a_list.remove(j)
	return a_list


print find_primes()
