"""
File: boggle.py
Name: Jason Lee
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	# Get the Boggle board from the user.
	boggle_board = get_boggle_board()

	start = time.time()

	find_words(boggle_board)

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start:} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	word_list = []
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip().lower()  # Remove leading/trailing whitespaces and convert the word to lowercase
			if len(word) >= 4:  # Check if the word has a length of 4 or more
				word_list.append(word)
	return word_list


def get_boggle_board():
	boggle_board = []  # Create an empty list to represent the boggle board
	for row in range(4):
		boggle_board.append([])  # Create an empty list for each row

		# Prompt the user to enter the letters for the current row
		row_input = input(f'{row+1} row of letters: ').strip().lower().split()

		# Validate the input for each letter in the row
		for i in range(len(row_input) - 1):
			# Check if the length of each letter is not 1 or the row length is not 4
			if len(row_input[i]) != 1 or len(row_input) != 4:
				print('Illegal input')
				exit()

		boggle_board[row] = row_input # Store the row of letters in the boggle board list

	return boggle_board


class TrieNode:
	def __init__(self):
		self.children = {}
		self.end = False


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
		node.end = True

	def search(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				return False
			node = node.children[char]
		return node.end

	def starts_with(self, prefix):
		node = self.root
		for char in prefix:
			if char not in node.children:
				return False
			node = node.children[char]
		return True


def find_words(boggle_board):
	words_found = set()  # Set to store the found words
	rows = len(boggle_board)  # Number of rows in the Boggle board
	cols = len(boggle_board[0])  # Number of columns in the Boggle board
	visited = set()  # Set to keep track of visited cells
	dictionary = read_dictionary()
	trie = Trie()  # Create a trie data structure for word prefix checking

	# Build a trie data structure with words from the dictionary for word prefix checking
	for word in dictionary:
		trie.insert(word)

	# Find all the words on the Boggle board.
	for row in range(rows):
		for col in range(cols):
			find_words_helper(row, col, boggle_board, '', words_found, visited, trie)

	print(f"There are {len(words_found)} words in total.")


def find_words_helper(row, col, boggle_board, word, words_found, visited, trie):
	visited.add((row, col))
	word += boggle_board[row][col]  # Append the current letter to the word

	# Check if the word meets the conditions to be considered as a valid word
	if len(word) >= 4 and trie.starts_with(word) and trie.search(word) and word not in words_found:
		words_found.add(word)
		print("Found:", '"' + str(word) + '"')

	# Explore all neighboring cells (including diagonals)
	for r in range(row-1, row+2):
		for c in range(col-1, col+2):
			# Check if the neighboring cell is within the board boundaries and not visited
			if 0 <= r < 4 and 0 <= c < 4 and (r, c) not in visited and trie.starts_with(word):
				find_words_helper(r, c, boggle_board, word, words_found, visited, trie)

	visited.remove((row, col))  # Remove the current cell from the visited set


# def has_prefix(sub_s, dictionary):
# 	"""
# 	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
# 	:return: (bool) If there is any words with prefix stored in sub_s
# 	"""
# 	trie = Trie()
# 	for word in dictionary:
# 		trie.insert(word)
# 	return trie.starts_with(sub_s)


if __name__ == '__main__':
	main()
