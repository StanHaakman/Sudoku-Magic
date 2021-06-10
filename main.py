from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
import argparse

from SudokuGame import SudokuGame
from SudokuUi import SudokuUI

BOARDS = ['debug', 'n00b', 'l33t', 'error']  # Available sudoku boards
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


if __name__ == '__main__':
	game = SudokuGame()
	game.start()

	root = Tk()
	SudokuUI(root, game)
	root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
	root.mainloop()
