class SudokuSolver(object):
	def __init__(self, grid):
		self.grid = grid

	def test_sudoku(self):
		pass

	def solve(self):
		"""Solve puzzle with Recursive Backtracking"""

		# todo: Change loop through all to loop through available spots
		# Loop through all the slots
		for i in range(0, 81):
			# Configure the row and column
			row = i // 9
			col = i % 9

			# On the next empty cell
			if self.grid[row][col] == 0:
				# Loop through the available numbers
				for number in range(1, 10):
					# Check if the number has no conflicts
					if not self.no_conflicts(self.grid, row, col, number):
						self.grid[row][col] = number
						if not self.find_unsettled_spot(self):
							break
						else:
							if self.solve:
								return True

	def no_conflicts(self, grid, row, col, number):
		"""returns True if the number has been used in that row"""
		if number in grid[row]:
			return True

		"""returns True if the number has been used in that column"""
		for i in range(9):
			if grid[i][col] == number:
				return True

		"""returns True if the number has been used in that subgrid/box"""
		sub_row = (row // 3) * 3
		sub_col = (col // 3) * 3
		for i in range(sub_row, (sub_row + 3)):
			for j in range(sub_col, (sub_col + 3)):
				if grid[i][j] == number:
					return True
		return False

	def find_unsettled_spot(self):
		"""return the next empty square coordinates in the grid"""
		for i in range(9):
			for j in range(9):
				if self.grid[i][j] == 0:
					return i, j
		return
