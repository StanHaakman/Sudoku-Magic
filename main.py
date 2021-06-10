from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
import argparse

from SudokuBoard import SudokuBoard

BOARDS = ['debug', 'n00b', 'l33t', 'error']  # Available sudoku boards

gameboard = SudokuBoard()

gameboard.print_board()

