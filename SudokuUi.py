from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuUI(Frame):
	def __init__(self, parent, game):
		self.game = game
		self.parent = parent
		Frame.__init__(self, parent)

		self.row, self.col = 0,0

		self.__startUI()

	def __startUI(self):
		self.parent.title("Magic Sudoku")
		self.pack(fill=BOTH, expand=1)
		self.canvas = Canvas(self, width = WIDTH, height = HEIGHT)
		self.canvas.pack(fill=BOTH, side=TOP)

		clear_button = Button(self, text="Verwijder eigen cijfers", command=self.__clear_answers())
		clear_button.pack(fill=BOTH, side=BOTTOM)

		self.__draw_grid()
		self.__draw_board()

		self.canvas.bind("<Button-1>", self.__cell_clicked())
		self.canvas.bind("<Key>", self.__key_pressed())

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
		self.canvas.delete("Numbers")

		for i in range(9):
			for j in range(9):
				answer = self.game.puzzle[i][j]
				if answer != 0:
					x = MARGIN + j * SIDE + SIDE / 2
					y = MARGIN + i * SIDE + SIDE / 2

					original = self.game.start_puzzle[i][j]
					color = "black" if answer == original else "sea green"
					self.canvas.create_text(x, y, text=answer, tags="numbers", fill=color)

	def __clear_answers(self):
		pass

	def __cell_clicked(self):
		pass

	def __key_pressed(self):
		pass

