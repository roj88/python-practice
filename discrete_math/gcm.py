#!/usr/bin/python

import argparse
import sys
import os
import math

def get_arguments():
	try:
		parser=argparse.ArgumentParser()

		inputs = {
            'arg1' : 'first arugment',
            'arg2' : 'first arugment',
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


args = get_arguments()

def gcd(a, b):

    while b:
        a, b = b, a%b
    return a

print gcd(int(args.arg1), int(args.arg2))