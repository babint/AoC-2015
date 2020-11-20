#!/usr/bin/env python3

import sys

nice_words = []
naught_words = []
blacklisted_seq = ['ab', 'cd', 'pq', 'xy']
vowels = set("aeiou") 

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

def is_nice_word(word):

	vowels_count = 0
	has_repeated = False
	prev_char = None 

	# Loop through each char to test
	for char in word:

		# Count Values
		if (char in vowels): vowels_count += 1

		# Test Repeated
		if (char == prev_char): has_repeated = True

		# Track previous character in next round	
		prev_char = char

	# Check if we have enough vowels
	if (vowels_count < 3): return False

	# Check we had at least repeated character 
	if (not has_repeated): return False

	# Check for banned sequences
	for seq in blacklisted_seq:
		if (seq in word): return False

	return True


# Read File
with open(sys.argv[1]) as f:
	lines = f.read().splitlines()

	for word in lines:
		if (is_nice_word(word)):	
			nice_words.append(word)
		else: 
			naught_words.append(word)

# Print Results		
print(f'nice words: {len(nice_words)}')
print(f'naughty words: {len(naught_words)}')
print("\ndone.");