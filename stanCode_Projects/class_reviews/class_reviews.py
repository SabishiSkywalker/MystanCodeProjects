"""
File: class_reviews.py
Name: Jason Lee
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program will show the maximum, minimum and average grade of the designated class
    """
    # Use two count variables to store the number of the score in each class
    count_001 = 0
    count_101 = 0
    # String should be case-insensitive
    class_code = input('Which class? ').upper()
    if class_code == str(EXIT):
        print('No class scores were entered ')
    else:
        if class_code == 'SC001':
            count_001 += 1
        if class_code == 'SC101':
            count_101 += 1
        score = int(input('Score: '))
        max_001 = score
        min_001 = score
        total_001 = score
        max_101 = score
        min_101 = score
        total_101 = score
        while True:
            # String should be case-insensitive
            class_code = input('Which class? ').upper()
            if class_code == str(EXIT):
                break
            elif class_code == 'SC001':
                score = int(input('Score: '))
                count_001 += 1
                if score > max_001:
                    max_001 = score
                if score < min_001:
                    min_001 = score
                total_001 += score
            elif class_code == 'SC101':
                score = int(input('Score: '))
                count_101 += 1
                if score > max_101:
                    max_101 = score
                if score < min_101:
                    min_101 = score
                total_101 += score
            # If the class number is neither SC001 nor SC101
            else:
                print("Invalid class code. Please try again.")
        # Calculate the average score of class SC001 if there are at least one score
        if count_001 > 0:
            avg_001 = total_001 / count_001
            print('=============SC001=============')
            print('Max(001): ' + str(max_001))
            print('Min(001): ' + str(min_001))
            print('Avg(001): ' + str(avg_001))
        # If there is no score in SC001
        else:
            print('=============SC001=============')
            print('No score for SC001 ')
        # Calculate the average score of class SC101 if there are at least one score
        if count_101 > 0:
            avg_101 = total_101 / count_101
            print('=============SC101=============')
            print('Max(101): ' + str(max_101))
            print('Min(101): ' + str(min_101))
            print('Avg(101): ' + str(avg_101))
        # If there is no score in SC101
        else:
            print('=============SC101=============')
            print('No score for SC101 ')




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
