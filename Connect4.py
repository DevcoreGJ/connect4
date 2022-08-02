BOARD_COLS = 7
BOARD_ROWS = 6

class Board():
	def _init_(self):
		self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
		self.turns = 0
		self.last_move = [-1, -1] #row, col

	def print_board(self):
		#number the columns
		print("\n")
		for c in range (BOARD_COLS):
			print(f" ({c + 1}) ", end="")
			print("\n")

			# print the slots of the board game
			for r in range (BOARD_ROWS):
			print('|', end="")
				for c in range(BOARD_COLS)
				print(f" {self.board[r][c]} |", end="") # prints the entire board
				print("\n")
