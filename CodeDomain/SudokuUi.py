import math
from copy import deepcopy
from tkinter import Canvas, Frame, Button, BOTH, TOP, BOTTOM, Label

from CodeDomain.SudokuSolver import SudokuSolver

MARGIN = 30  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuUI(Frame):
	def __init__(self, parent, game):
		self.game = game
		self.parent = parent
		Frame.__init__(self, parent)

		self.row, self.col = 0, 0

		self.__startUI()

	def __startUI(self):
		"""
		Start the UI with the help op helper functions.
		:return:
		"""
		self.parent.title("Magic Sudoku")
		self.pack(fill = BOTH, expand = 2)
		self.canvas = Canvas(self, width = WIDTH, height = HEIGHT)
		self.canvas.pack(fill = BOTH, side = TOP)

		self.__draw_buttons()
		self.__draw_grid()
		self.__draw_board()

		self.canvas.bind("<Button-1>", self.__cell_clicked)
		self.canvas.bind("<Key>", self.__key_pressed)

	def __draw_buttons(self):
		"""
		This function creates and draws all the buttons of the UI.
		:return:
		"""
		clear_button = Button(self, text = "Verwijder eigen cijfers", command = self.__clear_answers)
		clear_button.pack(fill = BOTH, side = BOTTOM)

		solve_button = Button(self, text = "Solve It!", command = self.__solve)
		solve_button.pack(fill = BOTH, side = BOTTOM)

		new_game_frame = Frame(self)

		new_game_text = Label(new_game_frame, text = "Start nieuw spel:")
		new_game_text.grid(row=0)

		easy_game_button = Button(new_game_frame, text = "Makkelijk", command = lambda: self.__new_game(40))
		easy_game_button.grid(row=1, column=0)

		medium_game_button = Button(new_game_frame, text = "Gemiddeld", command = lambda: self.__new_game(34))
		medium_game_button.grid(row=1, column=1)

		hard_game_button = Button(new_game_frame, text = "Moeilijk", command = lambda: self.__new_game(26))
		hard_game_button.grid(row=1, column=2)

		insane_game_button = Button(new_game_frame, text = "Onmogelijk", command = lambda: self.__new_game(17))
		insane_game_button.grid(row=1, column=3)

		new_game_frame.pack(fill=BOTH, side=BOTTOM)

	def __draw_grid(self):
		"""
		This function creates the lines that makes up the grid.
		:return:
		"""
		for i in range(10):
			color = "black" if i % 3 == 0 else "gray"

			x0 = MARGIN + i * SIDE
			y0 = MARGIN
			x1 = MARGIN + i * SIDE
			y1 = HEIGHT - MARGIN
			self.canvas.create_line(x0, y0, x1, y1, fill = color)

			x0 = MARGIN
			y0 = MARGIN + i * SIDE
			x1 = WIDTH - MARGIN
			y1 = MARGIN + i * SIDE
			self.canvas.create_line(x0, y0, x1, y1, fill = color)

	def __draw_board(self):
		"""
		This function deletes all the numbers from the canvas.
		Then it fills them with the numbers.
		If the number is not present in the original give that number a different color.
		:return:
		"""
		self.canvas.delete("numbers")

		for i in range(9):
			for j in range(9):
				answer = self.game.puzzle[i][j]
				if answer != 0:
					x = MARGIN + j * SIDE + SIDE / 2
					y = MARGIN + i * SIDE + SIDE / 2

					self.original = self.game.start_puzzle[i][j]
					color = "black" if answer == self.original else "sea green"
					self.canvas.create_text(x, y, text = answer, tags = "numbers", fill = color, font=("Purisa", 20))

	def __clear_answers(self):
		"""
		Clear all the filled in numbers and if the victory screen is present delete that to.
		Then rebuild the board.
		:return:
		"""
		self.game.start()
		self.canvas.delete("victory")
		self.__draw_board()

	def __cell_clicked(self, event):
		"""
		When a cell is clicked determan which it was and call the function self.__draw_cursor.
		:param event:
		:return:
		"""
		if self.game.game_over:
			return

		x, y = event.x, event.y
		if MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN:
			self.canvas.focus_set()

			# get row and col numbers from x,y coordinates
			row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

			row, col = math.floor(row), math.floor(col)

			# if cell was selected already - deselect it
			if (row, col) == (self.row, self.col):
				self.row, self.col = -1, -1
			elif self.game.start_puzzle[row][col] == 0:
				self.row, self.col = row, col

		self.__draw_cursor()

	def __draw_cursor(self):
		"""
		Draw a red line around of the clicked cell.
		:return:
		"""
		self.canvas.delete("cursor")

		if self.row >= 0 and self.col >= 0:
			x0 = MARGIN + self.col * SIDE + 1
			y0 = MARGIN + self.row * SIDE + 1
			x1 = MARGIN + (self.col + 1) * SIDE - 1
			y1 = MARGIN + (self.row + 1) * SIDE - 1
			self.canvas.create_rectangle(
				x0, y0, x1, y1,
				outline = "red", tags = "cursor"
			)

	def __key_pressed(self, event):
		"""
		Function which is called when a key gets pressed.
		First check if its valid number and then, if the number pressed is allowed in that cell, place the number in the cell.
		Then redraw the board and cursor and check if the game has been won.
		If that's the case draw victory screen.
		:param event:
		:return:
		"""
		if self.game.game_over:
			return
		if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
			column = [self.game.puzzle[i][self.col] for i in range(9)]

			x0 = (self.col // 3) * 3
			y0 = (self.row // 3) * 3

			subgrid = []

			for i in range(3):
				for j in range(3):
					subgrid.append(self.game.puzzle[y0 + i][x0 + j])

			if int(event.char) not in self.game.puzzle[self.row] and int(event.char) not in column and int(event.char) not in subgrid:
				self.game.puzzle[self.row][self.col] = int(event.char)
				self.col, self.row = -1, -1
				self.__draw_board()
				self.__draw_cursor()
				if self.game.check_win():
					self.__draw_victory()

	def __draw_victory(self):
		"""
		Draw the victory screen.
		:return:
		"""
		x0 = y0 = MARGIN + SIDE * 2
		x1 = y1 = MARGIN + SIDE * 7
		self.canvas.create_oval(
			x0, y0, x1, y1,
			tags = "victory", fill = "dark orange", outline = "orange"
		)

		x = y = MARGIN + 4 * SIDE + SIDE / 2
		self.canvas.create_text(
			x, y,
			text = "You win!", tags = "winner",
			fill = "white", font = ("Arial", 32)
		)

	def __new_game(self, remaining):
		"""
		This function calls the new_game function on the SudokuGame class.
		Then starts a new game and if necessary deletes the victory screen and redraws the board.
		:param remaining:
		:return:
		"""
		self.game.new_game(remaining)
		self.game.start()
		self.canvas.delete("victory")
		self.__draw_board()

	def __solve(self):
		"""
		This function creates a new SudokuSolver class.
		Then gives the instance the grid to solve.
		When the algorithm is finished fill in the solved grid.
		:return:
		"""
		self.solver = SudokuSolver(deepcopy(self.game.start_puzzle))
		self.game.puzzle = self.solver.grid
		self.canvas.delete("victory")
		self.__draw_board()
		self.__draw_victory()
