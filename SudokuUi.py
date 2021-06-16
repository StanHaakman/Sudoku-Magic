import math
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 30  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuUI(Frame):
	def __init__(self, parent, game):
		self.game = game
		self.parent = parent
		self.parent.geometry('1000x1000')
		Frame.__init__(self, parent)

		self.row, self.col = 0, 0

		self.__startUI()

	def __startUI(self):
		self.parent.title("Magic Sudoku")
		self.pack(fill = BOTH, expand = 2)
		self.canvas = Canvas(self, width = WIDTH, height = HEIGHT)
		self.canvas.pack(fill = BOTH, side = TOP)

		clear_button = Button(self, text = "Verwijder eigen cijfers", command = self.__clear_answers)
		clear_button.pack(fill = BOTH, side = BOTTOM)

		new_game_button = Button(self, text = "Start nieuw spel", command = self.__new_game)
		new_game_button.pack(fill = BOTH, side = BOTTOM)

		self.__draw_grid()
		self.__draw_board()

		self.canvas.bind("<Button-1>", self.__cell_clicked)
		self.canvas.bind("<Key>", self.__key_pressed)

	def __draw_grid(self):
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
		self.game.start()
		self.canvas.delete("victory")
		self.__draw_board()

	def __cell_clicked(self, event):
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
		if self.game.game_over:
			return
		if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
			column = [self.game.puzzle[i][self.col] for i in range(9)]
			if int(event.char) not in self.game.puzzle[self.row] and int(event.char) not in column:
				self.game.puzzle[self.row][self.col] = int(event.char)
				self.col, self.row = -1, -1
				self.__draw_board()
				self.__draw_cursor()
				if self.game.check_win():
					self.__draw_victory()

	def __draw_victory(self):
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

	def __new_game(self):
		self.game.new_game()
		self.game.start()
		self.canvas.delete("victory")
		self.__draw_board()
