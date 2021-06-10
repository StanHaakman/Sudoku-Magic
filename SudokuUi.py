from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

from main import WIDTH, HEIGHT


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
		pass

	def __draw_board(self):
		pass

	def __clear_answers(self):
		pass

	def __cell_clicked(self):
		pass

	def __key_pressed(self):
		pass

