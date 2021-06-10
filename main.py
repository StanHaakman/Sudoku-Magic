import tkinter as tk
import argparse

from SudokuBoard import SudokuBoard

BOARDS = ['debug', 'n00b', 'l33t', 'error']  # Available sudoku boards
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

gameboard = SudokuBoard(root = tk.Tk())

gameboard.print_board()

