from random import shuffle


class SudokuBoard(object):

	def __init__(self, remaining = 25):
		"""
		This class creates a new sudoku board.
		When a new instance is initialized a new board gets created and numbers
		get removed to get the puzzle that has to be solved.
		:param remaining:
		"""
		self.counter = 0
		self.path = []
		self.board = self.__create_board()
		self.remove_numbers_from_board(remaining)

	def __create_board(self):
		"""
		This function creates a new board. This board will be fully filled in and valid.
		:return:
		"""

		# create an initial matrix, or a list of a list
		self.board = [[0 for i in range(9)] for j in range(9)]

		'''
		self.board looks like this
		[
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
			[0. 0. 0. 0. 0. 0. 0. 0. 0.]
		]
		'''

		self.__generate_solution(self.board)

		# Return the constructed board
		return self.board

	def __generate_solution(self, board):
		"""
		This function is very similar to the way I solve the puzzles.
		It creates a new valid board with Recursive backtracking.
		:param board:
		:return:
		"""
		"""generates a full solution with backtracking"""
		number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

		# Loop through all the valid spaces. A sudoku board has 81 spaces
		for i in range(0, 81):
			row = i // 9
			col = i % 9
			# find next empty cell
			if board[row][col] == 0:
				# Shuffle the list with all the possibilities
				shuffle(number_list)

				# Loop through all the numbers in the list
				for number in number_list:
					# Check if the location of the number is valid
					if self.__location_valid(board, row, col, number):
						self.path.append((number, row, col))
						# Add the number to the board
						board[row][col] = number
						# Check if there are still emtpy spots in the board
						if not self.__find_empty_spot(board):
							# Finish the algorithm because the creation is valid
							return True
						else:
							if self.__generate_solution(board):
								# if the board is full
								return True
				break
		# This is the backtracking. This will reset the cell to 0
		board[row][col] = 0
		return False

	def __location_valid(self, board, row, col, number):
		"""
		Return false if the location of the given number is invalid with the help of helper functions
		:param board:
		:param row:
		:param col:
		:param number:
		:return:
		"""

		if self.__number_in_row(board, row, number):
			return False
		elif self.__number_in_column(board, col, number):
			return False
		elif self.__number_in_subboard(board, row, col, number):
			return False
		return True

	def __number_in_row(self, board, row, number):
		"""
		Returns true if the number is used in the given row
		:param board:
		:param row:
		:param number:
		:return:
		"""
		if number in board[row]:
			return True
		return False

	def __number_in_column(self, board, col, number):
		"""
		Returns true if the number is used in the given column
		:param board:
		:param col:
		:param number:
		:return:
		"""
		for i in range(9):
			if board[i][col] == number:
				return True
		return False

	def __number_in_subboard(self, board, row, col, number):
		"""
		Return true if the number is used in the given subboard
		:param board:
		:param row:
		:param col:
		:param number:
		:return:
		"""
		sub_row = (row // 3) * 3
		sub_col = (col // 3) * 3

		for i in range(sub_row, (sub_row + 3)):
			for j in range(sub_col, (sub_col + 3)):
				if board[i][j] == number:
					return True
		return False

	def __find_empty_spot(self, board):
		"""
		Return the next empty spot in the board
		:param board:
		:return:
		"""
		for i in range(9):
			for j in range(9):
				if board[i][j] == 0:
					return i, j
		return

	def get_non_empty_squares(self, board):
		"""
		Returns a shuffled list of non-empty squares in the puzzle
		:param board:
		:return:
		"""
		non_empty_squares = []
		for i in range(len(board)):
			for j in range(len(board)):
				if board[i][j] != 0:
					non_empty_squares.append((i, j))
		shuffle(non_empty_squares)
		return non_empty_squares

	def remove_numbers_from_board(self, remaining):
		"""
		This function removes numbers until the remaining numbers requirement is achieved.
		:param remaining:
		:return:
		"""
		non_empty_squares = self.get_non_empty_squares(self.board)
		non_empty_squares_count = len(non_empty_squares)

		while non_empty_squares_count != remaining:
			row, col = non_empty_squares.pop()
			non_empty_squares_count -= 1

			self.board[row][col] = 0
		return

	def print_board(self):
		"""
		This function is for testing/development purposes.
		:return:
		"""
		for row in self.board:
			print(row)
