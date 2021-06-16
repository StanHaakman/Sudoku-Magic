class SudokuSolver(object):
	def __init__(self, grid):
		self.grid = grid

		self.solve()

	def test_sudoku(self):
		pass

	def possible(self, y, x, n):
		# n is the number we want to fill in
		# 1st
		# check if n already existed in vertical (y) axis
		# if exists, return False (not possible)
		for i in range(9):
			if self.grid[y][i] == n:
				return False

		# 2nd
		# check horizontal (x) axis
		for i in range(9):
			if self.grid[i][x] == n:
				return False

		# 3rd
		# check the 3x3 local grid
		x0 = (x // 3) * 3
		y0 = (y // 3) * 3
		for i in range(3):
			for j in range(3):
				if self.grid[y0 + i][x0 + j] == n:
					return False

		# return true if pass all 3 checks.
		return True

	def solve(self):
		"""Solve puzzle with Recursive Backtracking"""
		empty_spots = self.find_unsettled_spot()
		if not empty_spots:
			return True
		else:
			row, col = empty_spots

		for i in range(1, 10):
			if self.possible(row, col, i):
				self.grid[row][col] = i

				if self.solve():
					return True

				self.grid[row][col] = 0

		return False

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
