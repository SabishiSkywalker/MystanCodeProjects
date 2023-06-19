"""
File: anagram.py
Name: Jason Lee
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit) ')

    while True:

        user_input = input('Find anagrams for: ')

        if user_input == EXIT:
            break
        start = time.time()
        dictionary = read_dictionary()
        anagrams = find_anagrams(user_input, dictionary)

        print(f'Found {len(anagrams)} anagrams:')
        print(f'{len(anagrams)} anagrams:', anagrams)

        end = time.time()
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    print('----------------------------------')


def read_dictionary():
    # Read the dictionary file and return a list of words
    word_list = []

    with open(FILE, 'r') as file:
        for line in file:
            word = line.strip()
            word_list.append(word)

    return word_list


def find_anagrams(s, dictionary):
    """
    :param s: The word to find anagrams for.
    :return: A list of all anagrams of the given word.
    """
    s = ''.join(sorted(s))   # Sort the input word to simplify the anagram checking

    anagrams = []       # Initialize an empty list to store the anagrams.
    stack = [('', s)]   # A stack to keep track of the current string and remaining letters

    while stack:
        # Pop the top two elements from the stack.
        current_string, remaining_letters = stack.pop()

        # If the remaining letters are empty, then we have found an anagram.
        if len(remaining_letters) == 0:
            # Check if the current string is in the dictionary and not already in the list of anagrams.
            if current_string in dictionary and current_string not in anagrams:
                print('Searching...')
                anagrams.append(current_string)
                print('Found:', current_string)
            continue

        # Iterate over the remaining letters.
        for i in range(len(remaining_letters)):
            # Get the current letter.
            letter = remaining_letters[i]

            # If the current letter is the same as the previous letter, skip it.
            if i > 0 and letter == remaining_letters[i - 1]:
                continue

            # Get the new list of remaining letters without the current letter.
            new_letters = remaining_letters[:i] + remaining_letters[i + 1:]

            # Check if the new string is a prefix of any word in the dictionary.
            if has_prefix(current_string + letter, dictionary):
                # Add the new string to the stack.
                stack.append((current_string + letter, new_letters))
    # Return the list of anagrams.
    return anagrams


def has_prefix(sub_s, dictionary):
    """
    Check if any word in the dictionary starts with a given prefix.
    :param sub_s: The prefix to check.
    :return: True if there is a word that starts with the prefix, False otherwise.
    """

    # Initialize the start and end indices of the search.
    start = 0
    end = len(dictionary) - 1

    # While the start index is less than or equal to the end index, do the following:
    while start <= end:
        mid = (start + end) // 2    # Calculate the middle index
        word = dictionary[mid]      # Get the word at the middle index

        # If the word at the middle index starts with the prefix, then return True.
        if word.startswith(sub_s):
            return True
        else:
            # If the word at the middle index is less than the prefix
            if word < sub_s:
                start = mid + 1         # Update the start index to search in the right half
            else:
                end = mid - 1           # Update the end index to search in the left half

    # If the start index is greater than the end index, then return False.
    return False


if __name__ == '__main__':
    main()



