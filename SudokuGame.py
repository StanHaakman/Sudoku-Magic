from SudokuBoard import SudokuBoard


class SudokuGame(object):
	def __init__(self):
		"""
		When you create a SudokuGame instance. Use the SudokuBoard class to create a new random and valid sudoku board.
		"""
		self.start_puzzle = SudokuBoard().board

	def start(self):
		"""
		This puzzle fills in the game puzzle based on the given start_puzzle.
		This is separated for further use of the starting puzzle.
		:return:
		"""
		self.game_over = False
		self.puzzle = []

		for i in range(9):
			self.puzzle.append([])
			for j in range(9):
				self.puzzle[i].append(self.start_puzzle[i][j])

	def check_win(self):
		"""
		This puzzle checks if the player has won. This is done with helper functions.
		:return:
		"""
		for row in range(9):
			if not self.__check_row(row):
				return False
		for column in range(9):
			if not self.__check_column(column):
				return False
		for row in range(3):
			for column in range(3):
				if not self.__check_square(row, column):
					return False

		self.game_over = True
		return True

	def __check_block(self, block):
		"""
		This returns true if the set of numbers contains 1-9 and is valid for the sudoku solution.
		:param block:
		:return:
		"""
		return set(block) == set(range(1, 10))

	def __check_row(self, row):
		"""
		This function checks if the row is valid.
		:param row:
		:return:
		"""
		return self.__check_block(self.puzzle[row])

	def __check_column(self, column):
		"""
		This function checks if the column is valid.
		:param column:
		:return:
		"""
		return self.__check_block([self.puzzle[row][column] for row in range(9)])

	def __check_square(self, row, column):
		"""
		This function checks if the square is valid.
		:param row:
		:param column:
		:return:
		"""
		return self.__check_block(
			[
				self.puzzle[r][c]
				for r in range(row * 3, (row + 1) * 3)
				for c in range(column * 3, (column + 1) * 3)
			]
		)

	def new_game(self, remaining):
		"""
		This function creates a new board and fills in the start_puzzle.
		The param remaining stands for the amount of numbers should be left on the board.
		:param remaining:
		:return:
		"""
		self.start_puzzle = SudokuBoard(remaining).board
