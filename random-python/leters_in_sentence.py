#!/usr/bin/python

import re

sentence = 'Hello, my name is Roland.'

def letters_in_sentence(input_sentence):
	counter = 0
	for x in range(0, len(input_sentence)):
		if re.match(r"[a-zA-Z]", input_sentence[x]):
			counter = counter + 1
	return counter

print letters_in_sentence(sentence)