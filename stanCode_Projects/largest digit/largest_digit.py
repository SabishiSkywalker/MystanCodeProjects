"""
File: largest_digit.py
Name: Jason Lee
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# Convert negative number to positive
	if n < 0:
		n *= -1

	# Base case: single-digit number
	if n < 10:
		return n

	# Recursive case
	last_digit = n % 10
	remaining_digits = n // 10
	largest_digit = find_largest_digit(remaining_digits)

	# Compare the last digit with the largest digit found
	if last_digit > largest_digit:
		return last_digit
	else:
		return largest_digit


if __name__ == '__main__':
	main()
