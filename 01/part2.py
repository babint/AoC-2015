#!/usr/bin/env python3

import sys

current_floor = 0
first_basement_step = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File + Calculate Floor
with open(sys.argv[1]) as f:
	data = f.read()

	for i, instruction in enumerate(data):
		if (instruction == '('):
			current_floor = current_floor + 1
		elif (instruction == ')'):
			current_floor = current_floor - 1
	
		if (current_floor < 0 and first_basement_step == 0):
			first_basement_step = i+1

# Print Results		
print(f"\nFirst Seend Basement Step: {first_basement_step}");	
print(f"\nCurrent Floor: {current_floor}");
print("\ndone.");