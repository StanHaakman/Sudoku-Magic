import tkinter as tk

from SudokuCode import SudokuBoard

gameboard = SudokuBoard(root = tk.Tk())
gameboard.create_empty_grid()
gameboard.run_application()

