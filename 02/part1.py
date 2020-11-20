#!/usr/bin/env python3

import sys

paper_needed = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File
with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

	for line in lines:
		dimensions = line.split('x')
		shortest = sys.maxsize 
		paper = 0
		
		l = int(dimensions[0])
		w = int(dimensions[1])
		h = int(dimensions[2])

		if (shortest > l*w): shortest = l*w
		if (shortest > w*h): shortest = w*h
		if (shortest > h*l): shortest = h*l
		
		paper = (2*l*w) + (2*w*h) + (2*h*l) + (shortest)
		paper_needed = paper_needed + paper
		#print(f"Dimensions: {line} paper: {paper} shortest: {shortest}")
		
# Print Results		
print(f"\npaper_needed: {paper_needed} square feet of paper");
print("\ndone.");
