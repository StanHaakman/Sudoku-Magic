import tkinter as tk
from tkinter import *

BOARDS = ['debug', 'n00b', 'l33t', 'error']  # Available sudoku boards
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuBoard:
	def __init__(self, root):
		self.root = root
		self.root.geometry(str(WIDTH) + "x" + str(HEIGHT))
		self.root.title('Sudoku Board')

	def create_empty_grid(self):
		new_frame = Frame(self.root, width=self.root.winfo_screenwidth())
		total = 0


		for row_index in range(3):
			for column_index in range(3):
				for grid_index in range(9):
					print(row_index, column_index, grid_index)
					total += 1
					print(total)

		new_frame.pack()

	def fill_grid(self):
		pass

	def run_application(self):
		self.root.mainloop()


gameboard = SudokuBoard(root = tk.Tk(), geometry = '540x600')
gameboard.create_empty_grid()
gameboard.run_application()

