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
		board = np.zeros((9, 9))

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
		for line in board_file:
			line = line.strip()

			# raise error if line is longer or shorter than 9 characters
			if len(line) != 9:
				board = np.array([])
				raise SudokuError(
					"Each line in the sudoku puzzle must be 9 chars long."
				)

			# create a list for the line
			print(board)
			np.append(board, [])
			print(board)

			# then iterate over each character
			for c in line:
				# Raise an error if the character is not an integer
				if not c.isdigit():
					raise SudokuError(
						"Valid characters for a sudoku puzzle must be in 0-9"
					)
				# Add to the latest list for the line
				board[-1].append(int(c))

		# Raise an error if there are not 9 lines
		if len(board) != 9:
			raise SudokuError("Each sudoku puzzle must be 9 lines long")

		# Return the constructed board
		return board

	def __generate_solution(self, empty_grid):
		pass

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

	def fill_grid(self):
		"""
		Own function
		:return:
		"""
		pass

	def run_application(self):
		"""
		Own function
		:return:
		"""
		self.root.mainloop()
