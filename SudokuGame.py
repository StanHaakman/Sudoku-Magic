from SudokuBoard import SudokuBoard


class SudokuGame(object):
	def __init__(self):
		self.start_puzzle = SudokuBoard().get_board()

	def start(self):
		self.game_over = False
		self.puzzle = []

		for i in range(9):
			self.puzzle.append([])
			for j in range(9):
				self.puzzle[i].append(self.start_puzzle[i][j])

	def check_win(self):
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

	def __check_row(self, row):
		pass

	def __check_column(self, column):
		pass

	def __check_square(self, row, column):
		pass
	
	
