#!/usr/bin/env python3

import sys

# Track houses, "<x>,<y>,<count>"
houses = {"0,0":1} # first house gets a present
x = y = 0 # starting location

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File
with open(sys.argv[1]) as f:
	data = f.read()

	for i, move in enumerate(data):
		
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
		
		# print(f'  i: {i}, dir: {move} == x: {x} y: {y}')

		# First time visiting house
		if (f'{x},{y}' not in houses): 
			houses[f'{x},{y}'] = 0;	
		
		# Give them a gift
		if (f'{x},{y}' in houses): 
			houses[f'{x},{y}'] += 1;

# Print Results		
print(len(houses))

print("\ndone.");
