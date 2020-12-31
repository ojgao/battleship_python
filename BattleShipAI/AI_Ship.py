import typing
import Player
import random
from Ship import Ship

class AI_Ship(Ship):
	def __init__(self, player: "Player", board: "Board", name: str, size: str)-> None:
		super().__init__(player, board, name, size)

	def place_ships(self) -> list:
		orientation = random.choice(['horizontal','vertical'])
		self.orientation = orientation
		if orientation == 'horizontal':
			row = random.randint(0, self.board.rows - 1)
			col = random.randint(0, self.board.cols - self.size)
			if(self.board.is_valid(row,col,'h',self.size) == 1):
				return self.place_ships()
			else:
				for i in range(self.size):
					self.board.edit(row,col+i,self.name[0])
				print(f"{self.player}'s Placement Board")
				self.board.format(self.board.board)
				return [row,col]
		else:
			row = random.randint(0, self.board.rows - self.size)
			col = random.randint(0, self.board.cols - 1)
			if(self.board.is_valid(row,col,'v',self.size) == 1):
				return self.place_ships()
			else:
				for i in range(self.size):
					self.board.edit(row+i,col,self.name[0])
				print(f"{self.player}'s Placement Board")
				self.board.format(self.board.board)
				return [row,col]

