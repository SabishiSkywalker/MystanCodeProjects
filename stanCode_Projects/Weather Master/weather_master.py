"""
File: weather_master.py
Name: Jason Lee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program shows the highest, lowest, average temperatures, and cold days according to the input datum.
	"""
	print("stanCode \"Weather Master 4.0!\" ")
	# User input a natural number.
	t = int(input('Next temperature: (or -100 to quit)? '))
	if t == EXIT:
		print('No temperatures were entered. ')
	else:
		# Count how many cold days
		if t < 16:
			count_1 = 1
		else:
			count_1 = 0
		highest = t
		lowest = t
		total = t
		# Count how many input datum
		count_2 = 1
		# Calculate the average value of the input datum
		average = total / count_2
		while True:
			t = int(input('Next temperature: (or -100 to quit)? '))
			if t == EXIT:
				break
			else:
				count_2 += 1
				if t < 16:
					count_1 += 1
				if t > highest:
					highest = t
				if t < lowest:
					lowest = t
				# Sum the input datum and refresh the value
				total = total+t
				average = total/count_2
		print('Highest temperature =' + str(highest))
		print('Lowest temperature =' + str(lowest))
		print('Average =' + str(average))
		print(str(count_1) + ' cold day(s)')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
