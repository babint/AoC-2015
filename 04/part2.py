#!/usr/bin/env python3

import sys
import hashlib

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py puzzle_input")
	exit(1)

# Get Secret
puzzle_input = sys.argv[1]
input_num = 0

# Calcuate 
for i in range(sys.maxsize):
	digest = hashlib.md5(puzzle_input.encode('utf-8')+str(i).encode('utf-8')).hexdigest()
	if (digest.startswith('000000')): # must start with 6 zeros
		input_num = i
		break;

# Print Results		
print(f'puzzle_input: {puzzle_input} solved with {input_num}')

print("\ndone.");
