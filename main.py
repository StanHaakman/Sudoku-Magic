from tkinter import Tk

from codeDomain.SudokuBoard import SudokuBoard
from codeDomain.SudokuGame import SudokuGame
from codeDomain.SudokuUi import SudokuUI

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


if __name__ == '__main__':
	game = SudokuGame()
	game.start()

	# Start tkinter object
	root = Tk()
	SudokuUI(root, game)
	root.geometry("%dx%d" % (WIDTH + MARGIN, HEIGHT + 150))
	root.mainloop()
