from random import shuffle

from SudokuError import SudokuError


class SudokuBoard(object):
	def __init__(self, root):
		self.counter = 0
		self.path = []
		self.board = self.__create_board()

	def __create_board(self):
		# create an initial matrix, or a list of a list
		self.board = [[0 for i in range(9)] for j in range(9)]

		'''
		Create emtpy numpy array with zeros to be filled in
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

		# Raise an error if there are not 9 lines
		if len(self.board) != 9:
			raise SudokuError("Each sudoku puzzle must be 9 lines long")

		# Return the constructed board
		return self.board

	def __generate_solution(self, board):
		"""generates a full solution with backtracking"""
		number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in range(0, 81):
			row = i // 9
			col = i % 9
			# find next empty cell
			if board[row][col] == 0:
				shuffle(number_list)
				for number in number_list:
					if self.__valid_location(board, row, col, number):
						self.path.append((number, row, col))
						board[row][col] = number
						if not self.__find_empty_spot(board):
							return True
						else:
							if self.__generate_solution(board):
								# if the board is full
								return True
				break
		board[row][col] = 0
		return False

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

	def __valid_location(self, board, row, col, number):
		"""
		Return false if the location of the given number is invalid
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

	def print_board(self):
		for row in self.board:
			print(row)
