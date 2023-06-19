"""
File: coin_flip_runs.py
Name: Jason Lee
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	print("Let's flip a coin! ")
	# get number of runs from user
	num_run = int(input('Number of runs: '))

	# Initialize variables
	pre_flip = ''
	num_run_so_far = 0
	is_in_a_row = False

	# loop over desired number of flips
	while num_run_so_far != num_run:
		# flip coin
		if r.randint(0, 1) == 0:
			flip = 'H'
		else:
			flip = 'T'

		# Add the flip to the pre_flip string
		pre_flip += flip

		# Count consecutive runs
		if len(pre_flip) > 1 and pre_flip[len(pre_flip)-2] == flip:
			if not is_in_a_row:
				num_run_so_far += 1
				is_in_a_row = True
		else:
			is_in_a_row = False
	print(pre_flip)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
