#!/usr/bin/env python3

import sys

paper_needed = 0
ribbon_needed = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File
with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

	for line in lines:
		dimensions = line.split('x')
		shortest = sys.maxsize 
		short_a = short_b = 0
		paper = 0
		ribbon = 0
		
		# Get dimensions
		l = int(dimensions[0])
		w = int(dimensions[1])
		h = int(dimensions[2])

		# Figure out shortest sides
		if (shortest > l*w):
			short_a = l
			short_b = w	
			shortest = short_a * short_b				
		if (shortest > w*h): 
			short_a = w
			short_b = h	
			shortest = short_a * short_b		
		if (shortest > h*l): 
			short_a = h
			short_b = l	
			shortest = short_a * short_b				

		# Calcuate paper and ribbon needed to wrap presents
		paper = (2*l*w) + (2*w*h) + (2*h*l) + (shortest)
		ribbon = (short_a + short_a + short_b + short_b) + ()

		# Track total needed
		paper_needed = paper_needed + paper
		ribbon_needed = ribbon_needed + ribbon

		#print(f"Dimensions: {line}, paper: {paper}, ribbon: {ribbon}, short_a: {short_a}, short_b: {short_b}, shortest: {shortest}")
		
# Print Results		
print(f"\npaper_needed: {paper_needed} square feet of paper");
print(f"ribbon_needed: {ribbon_needed} feet of ribbon");
print("\ndone.");


# ---- 2+2+3+3 = 10 feet of ribbon
# ---- 2*3*4 = 24 feet for ribbon for bow