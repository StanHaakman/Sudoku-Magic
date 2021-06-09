from random import shuffle
from tkinter import *
import numpy as np

from SudokuError import SudokuError

BOARDS = ['debug', 'n00b', 'l33t', 'error']  # Available sudoku boards
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuBoard(object):
	def __init__(self, root):
		self.root = root
		self.root.geometry(str(WIDTH) + "x" + str(HEIGHT))
		self.root.title('Sudoku Board')
		self.__create_board()

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

		# iterate over each line
		# for line in board_file:
		# 	line = line.strip()
		#
		# 	# raise error if line is longer or shorter than 9 characters
		# 	if len(line) != 9:
		# 		board = np.array([])
		# 		raise SudokuError(
		# 			"Each line in the sudoku puzzle must be 9 chars long."
		# 		)
		#
		# 	# create a list for the line
		# 	print(board)
		# 	np.append(board, [])
		# 	print(board)
		#
		# 	# then iterate over each character
		# 	for c in line:
		# 		# Raise an error if the character is not an integer
		# 		if not c.isdigit():
		# 			raise SudokuError(
		# 				"Valid characters for a sudoku puzzle must be in 0-9"
		# 			)
		# 		# Add to the latest list for the line
		# 		board[-1].append(int(c))

		# Raise an error if there are not 9 lines
		if len(self.board) != 9:
			raise SudokuError("Each sudoku puzzle must be 9 lines long")

		# Return the constructed board
		return self.board

	def __generate_solution(self):
		"""generates a full solution with backtracking"""
		grid = self.board
		number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in range(0, 81):
			row = i // 9
			col = i % 9
			# find next empty cell
			if grid[row][col] == 0:
				shuffle(number_list)
				for number in number_list:
					if self.valid_location(grid, row, col, number):
						self.path.append((number, row, col))
						grid[row][col] = number
						if not self.find_empty_square(grid):
							return True
						else:
							if self.generate_solution(grid):
								# if the grid is full
								return True
				break
		grid[row][col] = 0
		return False

	def create_empty_grid(self):
		"""
		Own function
		:return:
		"""
		new_frame = Frame(self.root, width = self.root.winfo_screenwidth())
		total = 0

		# Loop through grid in three rows
		for row_index in range(3):
			# Loop through row in three columns
			for column_index in range(3):
				# Loop through column for 9 slots
				for grid_index in range(9):
					# Print row column and grid index for visualization of grid
					print(row_index, column_index, grid_index)
					total += 1
					print(total)

		new_frame.pack()

	def number_in_row(self, grid, row, number):
		"""
		Returns true if the number is used in the given row
		:param grid:
		:param col:
		:param number:
		:return:
		"""
		if number in grid[row]:
			return True
		return False

	def number_in_column(self, grid, col, number):
		"""
		Returns true if the number is used in the given column
		:param grid:
		:param col:
		:param number:
		:return:
		"""
		for i in range(9):
			if grid[i][col] == number:
				return True
		return False

	def number_in_subgrid(self, grid, row, col, number):
		"""
		Return true if the number is used in the given subgrid
		:param grid:
		:param row:
		:param col:
		:param number:
		:return:
		"""
		sub_row = (row // 3) * 3
		sub_col = (col // 3) * 3

		for i in range(sub_row, (sub_row + 3)):
			for j in range(sub_col, (sub_col + 3)):
				if grid[i][j] == number:
					return True
		return False

	def valid_location(self, grid, row, col, number):
		"""
		Return false if the location of the given number is invalid
		:param grid:
		:param row:
		:param col:
		:param number:
		:return:
		"""

		if self.number_in_row(grid, row, number):
			return False
		elif self.number_in_column(grid, col, number):
			return False
		elif self.number_in_subgrid(grid, row, col, number):
			return False
		return True

	def run_application(self):
		"""
		Own function
		:return:
		"""
		self.root.mainloop()

