#!/usr/bin/python

import random
import collections


def bday_paradox(j, k):
	for i in range(1, k + 1):

		num_repeat_bdays = 0

		for trial in range(j):
			listOfNumbers = []
			for x in range (0, i):
				listOfNumbers.append(random.randint(1, 366))

			counter = collections.Counter(listOfNumbers)

			if max(counter.values()) > 1:
				num_repeat_bdays += 1


		print (i, float(num_repeat_bdays) / j)

print bday_paradox(10000, 25)