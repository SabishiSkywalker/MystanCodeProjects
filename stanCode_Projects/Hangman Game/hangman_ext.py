"""
File: hangman.py
Name: Jason Lee
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program show the hangman game process with a hangman pattern.
    """
    n = N_TURNS
    # Store the times of the wrong guess in a variable named count.
    count = 0
    result = random_word()
    # Use an empty string to string the answer with dashed lines.
    new = ''
    for i in range(len(result)):
        new += '-'
    print('THe word looks like ' + new)
    print('You have ' + str(n) + ' wrong guesses left. ')

    while True:
        # Let the guess character be uppercase and store in a variable named guess_ch.
        guess_ch = input('Your guess: ').upper()
        # Guess input is not an alphabet.
        if not guess_ch.isalpha() or len(guess_ch) > 1:
            print('Illegal format. ')
        # If guess input is not in the answer.
        elif guess_ch not in result:
            n -= 1
            count += 1
            print("There is no " + guess_ch + "'s in the word")
            print('THe word looks like ' + new)
            print_hangman(count)
            if n >= 1:
                print('You have ' + str(n) + ' wrong guesses left. ')
        # If guess input is in the answer.
        else:
            print('You are correct!')
            ans = replace(result, new, guess_ch)
            new = ans
            if new.find('-') != -1:
                print('THe world looks like ' + new)
                print('You have ' + str(n) + ' wrong guesses left. ')
                print_hangman(count)
        # If the number of guess becomes 0 and the right answer is not yet to gain.
        if n == 0 and new != result:
            print('You are completely hung : (')
            print('The word was: ' + result)
            break
        # If the player still have guess chance and gain the right answer.
        elif n >= 1 and new == result:
            print('You win!! ')
            print('The word was: ' + result)
            break


def replace(result, new, guess_ch):
    """
    :param result: The answer
    :param new: The answer blanked by the dashed line
    :param guess_ch: The character guessed by the player
    :return: The dashed lines are replaced by the character in the answer
    """
    ans = ''
    for i in range(len(result)):
        if guess_ch == result[i]:
            ans += guess_ch
        else:
            ans += new[i]
    return ans


def print_hangman(count):
    """
    :param count: The number of wrong guess
    :return: output a hangman pattern
    """
    if count == 0:
        print('+----+')
        print('|/    ')
        print('|     ')
        print('|     ')
        print('|     ')
        print('|___')
    elif count == 1:
        print('+----+')
        print('|/   |')
        print('|     ')
        print('|     ')
        print('|     ')
        print('|___')
    elif count == 2:
        print('+----+')
        print('|/   |')
        print('|    O')
        print('|     ')
        print('|     ')
        print('|___')
    elif count == 3:
        print('+----+')
        print('|/   |')
        print('|    O')
        print('|    |')
        print('|     ')
        print('|___')
    elif count == 4:
        print('+----+')
        print('|/   |')
        print('|    O')
        print('|   /|')
        print('|     ')
        print('|___')
    elif count == 5:
        print('+----+')
        print('|/   |')
        print('|    O')
        print('|   /|\\')
        print('|     ')
        print('|___')
    elif count == 6:
        print('+----+')
        print('|/   |')
        print('|    O')
        print('|   /|\\ ')
        print('|   / ')
        print('|___')
    elif count == 7:
        print('+----+')
        print('|/   |')
        print('|    O')
        print('|   /|\\')
        print('|   / \\')
        print('|___')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
