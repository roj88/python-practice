#!/usr/bin/python

import csv

with open('~/Downloads/nba_2017_nba_players_with_salary.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row