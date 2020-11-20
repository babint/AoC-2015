#!/usr/bin/env python3

import sys

nice_words = []
naught_words = []

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

def is_nice_word(word):

	has_seq_repeat = False
	has_leap_repeat = False
	prev_char = None 
	prev_char_2 = None
	seq = "None"

	# Loop through each char to test
	for i, char in enumerate(word):
		#print(f'i: {i} char: {char}')
		
		# Get substring of the 'rest' of the string
		tail = word[i+1:len(word)]		

		# Get previous 2 characters (if available)
		if ((i-1) > 0): prev_char = word[i-1]
		if ((i-2) > 0): prev_char_2 = word[i-2]
		
		# Set newest sequence
		if (prev_char): seq = prev_char+char

		# Test if this pair exists in the rest of the string
		if (seq in tail): has_seq_repeat = True

		# Test we've seen this same character two characters ago (leaps)
		if (char == prev_char_2): has_leap_repeat = True

		# Track previous character in next round	
		prev_char = char

	
	# Check if we had repeating two-char sequence
	if (not has_seq_repeat): return False

	# Check if we had a char repeat with one char between it and the next occurrence 
	if (not has_leap_repeat): return False


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
print("\nnice.");