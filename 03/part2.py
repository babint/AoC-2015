#!/usr/bin/env python3

import sys

# Track houses, "<x>,<y>,<count>"
houses = {"0,0":2} # first house gets a present from each santa
santa_x = santa_y = robo_x = robo_y = 0 # starting location

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File
with open(sys.argv[1]) as f:
	data = f.read()

	for i, move in enumerate(data):
		
		# Figure out which santa is moving
		if (i % 2) == 0:
			x = santa_x
			y = santa_y
		else: 
			x = robo_x
			y = robo_y

		# Move to new Location
		if (move == '^'):
			x = x + 1
		elif (move == '>'):
			y = y + 1
		elif (move == 'v'):
			x = x - 1
		elif (move == '<'):
			y = y - 1
		else:
			print(f'invalid move: {move} at i: {i}')
		
		# First time visiting house
		if (f'{x},{y}' not in houses): 
			houses[f'{x},{y}'] = 0;	
		
		# Give them a gift
		if (f'{x},{y}' in houses): 
			houses[f'{x},{y}'] += 1;

		# Map back
		if (i % 2) == 0:
			santa_x = x
			santa_y = y
		else: 
			robo_x = x
			robo_y = y

# Print Results		
total_houses = len(houses)
print(f"\nVisted Houses: {total_houses}");
print("\ndone.");
