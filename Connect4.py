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
			print(f" ({r + 1}) ", end="")
		print("\n")

		# print the slots of the board game
		for r in range (BOARD_ROWS):
			print('|', end="")
			for c in range(BOARD_COLS):
				print(f" {self.board[r][c]} |", end="") # prints the entire board
			print("\n")
				
		print(f"{'-' * 42}\n") #prints 30 - next to each other

def which_turn(self):
    players = ['X', 'O']
    return players[self.turns % 2]

def in_bounds(self, r, c):
	return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)
	
def turn(self, column):
    # search from the bottom up
    for r in range(BOARD+_ROWS-1, -1, -1):
      	if self.board[r][column] == ' ':
	        self.board[r][column] = self.which_turn()
	        self.last_move = [r, column]

	        self.turns += 1
	        return True
			
    return False

def check_winner(self):
   	last_row = self.last_move[0]
   	last_col = self.last_move[1]
   	last_letter = self.board[last_row][last_col]

   	# [r, c] direction, matching letter count locked bool
   	directions = [[[-1, 0], 0, True],
   				[[1, 0], 0, True],
  				[[0, -1], 0, True],
   				[[0, 1], 0, True],
   				[[-1, -1], 0, True]
				[[1, 1], 0, True]
   				[[-1, 1], 0, True]
   				[[1, -1], 0, True]

   	# Check outward for matches
   	for a in range(4):
   		for d in directions:
   			r = last_row + (d[0][0] * (a+1))
   			c = last_row + (d[0][1] * (a+1))

    
def play():
	game = Board()

	game_over = False
	while not game_over:
    	#continue playing
    	game.print_board()

    	#ask user for input but only accepting valid
    	valid_move = False
    	while not valid_move:
      		user_move = input(f"{game.which_turn()}'s turn - pick a column (1-{BOARD_COLS}): ")
      		try:
        		vaid_move = game.turn(int(user_move)-1)
      		except:
              print(f"Please choose a number between 1 and {BOARD_COLS}")
 
 		# End if winner is declared
		game_over = game.check_winner()

		# End if tie
		if not any (' ' in x for x in game.board):
			print("The game is a draw..")
			return

if __name__ == '__main__':
    play()