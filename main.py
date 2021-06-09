import tkinter as tk

import numpy as np

from SudokuBoard import SudokuBoard

gameboard = SudokuBoard(root = tk.Tk())

# gameboard.create_empty_grid()
gameboard.run_application()

