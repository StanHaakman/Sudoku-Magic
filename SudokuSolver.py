class SudokuSolver(object):
	def __init__(self, grid):
		self.grid = grid
		self.solve()

	def solve(self):
		"""Solve puzzle with Recursive Backtracking"""
		empty_spot = self.find_unsettled_spot()
		if not empty_spot:
			return True
		else:
			row, col = empty_spot

		#  Loop through all the available numbers
		for number in range(1, 10):
			# If the number has no conflicts in its row, column or subgrid
			if self.no_conflicts(row, col, number):
				# Then overwrite the 0 with the new number
				self.grid[row][col] = number

				if self.solve():
					return True

				# This is where backtracking happens
				# Reset the latest position back to 0 and try with new number value
				self.grid[row][col] = 0

		return False

	def no_conflicts(self, row, col, number):
		# 1st
		# check if n already existed in vertical (y) axis
		# if exists, return False (not possible)
		for i in range(9):
			if self.grid[row][i] == number:
				return False

		# 2nd
		# check horizontal (x) axis
		for i in range(9):
			if self.grid[i][col] == number:
				return False

		# 3rd
		# check the 3x3 local grid
		x0 = (col // 3) * 3
		y0 = (row // 3) * 3
		for i in range(3):
			for j in range(3):
				if self.grid[y0 + i][x0 + j] == number:
					return False

		# return true if pass all 3 checks.
		return True

	def find_unsettled_spot(self):
		"""return the next empty square coordinates in the grid"""
		for i in range(9):
			for j in range(9):
				if self.grid[i][j] == 0:
					return i, j
		return
