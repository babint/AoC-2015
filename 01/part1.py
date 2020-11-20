#!/usr/bin/env python3

import sys

current_floor = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File + Calculate Floor
with open(sys.argv[1]) as f:
	data = f.read()

	for instruction in data:
		if (instruction == '('):
			current_floor = current_floor + 1
		elif (instruction == ')'):
			current_floor = current_floor - 1

	
print(f"\nCurrent Floor: {current_floor}");
print("\ndone.");