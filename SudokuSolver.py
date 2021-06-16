
class SudokuSolver(object):
	def __init__(self, grid):
		self.grid = grid

	def test_sudoku(self):
		pass

	def solve(self):
		pass

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