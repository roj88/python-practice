#!/usr/bin/python

list_a = [1, 5, 3, 6, 203, -12, 353, 543, 525, 453, 234, 542, 4342901, 43, 231, 12, -34, 432]
list_b = [353, 543, 525, 453, 234, 43, 231, 12, -34, 432, -12, 1, 5, 3, 6, 203, 4342901]


def missing_item(list_a, list_b):
	bigger_list_a = len(list_a) > len(list_b)
	missing_element = 0

	diffa = set(list_a).difference(list_b)
	diffb = set(list_a).difference(list_b)

	return "Print the difference from a is %s the difference from b is %s" % (diffa, diffb)

print missing_item(list_a, list_b)
