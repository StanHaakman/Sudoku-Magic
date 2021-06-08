import tkinter as tk

from SudokuBoard import SudokuBoard

gameboard = SudokuBoard(root = tk.Tk())
gameboard.create_empty_grid()
gameboard.run_application()

