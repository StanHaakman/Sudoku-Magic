import timeit
import unittest

from codeDomain.SudokuBoard import SudokuBoard
from codeDomain.SudokuSolver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
	def test_solve(self):
		unfinished_grid = [
			[0, 8, 7, 0, 2, 9, 0, 1, 3],
			[2, 5, 3, 6, 0, 0, 7, 8, 9],
			[1, 9, 6, 0, 3, 0, 5, 0, 4],
			[7, 6, 2, 0, 5, 0, 8, 9, 1],
			[3, 4, 0, 8, 1, 7, 2, 0, 5],
			[8, 0, 5, 2, 9, 6, 0, 4, 7],
			[5, 0, 0, 9, 0, 3, 0, 7, 8],
			[9, 3, 8, 0, 0, 2, 0, 5, 6],
			[6, 7, 0, 4, 8, 0, 9, 3, 2]
		]

		finished_grid = [
			[4, 8, 7, 5, 2, 9, 6, 1, 3],
			[2, 5, 3, 6, 4, 1, 7, 8, 9],
			[1, 9, 6, 7, 3, 8, 5, 2, 4],
			[7, 6, 2, 3, 5, 4, 8, 9, 1],
			[3, 4, 9, 8, 1, 7, 2, 6, 5],
			[8, 1, 5, 2, 9, 6, 3, 4, 7],
			[5, 2, 4, 9, 6, 3, 1, 7, 8],
			[9, 3, 8, 1, 7, 2, 4, 5, 6],
			[6, 7, 1, 4, 8, 5, 9, 3, 2]
		]

		testSolver = SudokuSolver(unfinished_grid)
		testSolver.solve()

		self.assertListEqual(testSolver.grid, finished_grid)

	def test_unsettled(self):
		grid = [
			[4, 8, 7, 5, 2, 9, 6, 1, 3],
			[2, 5, 3, 6, 4, 1, 7, 8, 9],
			[1, 9, 6, 7, 3, 8, 5, 2, 4],
			[7, 6, 2, 3, 5, 4, 8, 9, 1],
			[3, 4, 9, 8, 1, 7, 2, 6, 5],
			[8, 1, 5, 2, 9, 6, 3, 4, 7],
			[5, 2, 4, 9, 6, 3, 1, 7, 8],
			[9, 3, 8, 1, 7, 2, 4, 0, 6],
			[6, 7, 1, 4, 8, 5, 9, 3, 2]
		]

		testSolver = SudokuSolver(grid).find_unsettled_spot()
		self.assertEqual((7, 7), testSolver, "There is an empty spot at row 8 column 8")

		grid = [
			[4, 8, 7, 5, 2, 9, 6, 1, 3],
			[2, 5, 3, 6, 4, 1, 7, 8, 9],
			[1, 9, 6, 7, 3, 8, 5, 2, 4],
			[7, 6, 2, 3, 5, 4, 8, 9, 1],
			[3, 4, 9, 8, 1, 7, 2, 6, 5],
			[8, 1, 5, 2, 9, 6, 3, 4, 7],
			[5, 2, 4, 9, 6, 3, 1, 7, 8],
			[9, 3, 8, 1, 7, 2, 4, 5, 6],
			[6, 7, 1, 4, 8, 5, 9, 3, 2]
		]

		testSolver = SudokuSolver(grid).find_unsettled_spot()
		self.assertIsNone(testSolver)

	def test_no_conflict(self):
		grid = [
			[0, 8, 7, 5, 2, 9, 6, 1, 3],
			[2, 5, 3, 6, 4, 1, 7, 8, 9],
			[1, 9, 6, 7, 3, 8, 5, 2, 4],
			[7, 6, 2, 3, 5, 4, 8, 9, 1],
			[3, 4, 9, 8, 1, 7, 2, 6, 5],
			[8, 1, 5, 2, 9, 6, 3, 4, 7],
			[5, 2, 4, 9, 6, 3, 1, 7, 8],
			[9, 3, 8, 1, 7, 2, 4, 5, 6],
			[6, 7, 1, 4, 8, 5, 9, 3, 2]
		]

		testSolver = SudokuSolver(grid)

		self.assertFalse(testSolver.no_conflicts(0, 0, 1))
		self.assertTrue(testSolver.no_conflicts(0, 0, 4))

	def test_speed(self):
		total_test = 100

		total_duration = timeit.Timer(lambda: SudokuSolver(SudokuBoard(17).board).solve()).timeit(number = total_test)

		single = total_duration / total_test

		print("The total number of times a new puzzle has been created and solved.")
		print(f"Total			: {total_test}")
		print(f"Total duration  : {total_duration}")
		print(f"Single duration : {single}")
