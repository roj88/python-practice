#!/usr/bin/env python 

import random
import collections
import pandas as pd
import matplotlib.pyplot as plt


def bday_paradox(j, k):

	output_list = []

	for i in range(1, k + 1):

		num_repeat_bdays = 0

		for trial in range(j):
			listOfNumbers = []
			for x in range (0, i):
				listOfNumbers.append(random.randint(1, 366))

			counter = collections.Counter(listOfNumbers)

			if max(counter.values()) > 1:
				num_repeat_bdays += 1


		output_list.append([i, float(num_repeat_bdays) / j])

		print i
	return output_list

bday = pd.DataFrame(bday_paradox(5000, 100))

x = bday[0]
y = bday[1]

plt.plot(x, y, 'o', color='black');

plt.show()