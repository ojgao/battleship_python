import typing
import Player
from abc import ABC, abstractmethod

class Ship():
	def __init__(self, player: "Player", board: "Board", name: str, size: str)-> None:
		self.player = player
		self.board = board
		self.name = name
		self.size = int(size)
		self.location = self.place_ships()
		self.status = "alive"
		
		
	@abstractmethod
	def place_ships(self) -> list:
		pass

	def is_hit(self,x:int,y:int) -> int:
		if self.board.board[x][y] != "* ":
			if self.board.board[x][y] == f"{self.name[0]} ":
				print(f"You hit {self.player}'s {self.name}!")
				return 1
			return -1
		else:
			return 0

	def is_sunk_horizontal(self) -> bool:
		for i in range(self.size):
			try:
				if self.board.board[self.location[0]][self.location[1]+i] != "X ":
					return False
			except:
				return False
		print(f"You destroyed {self.player}'s {self.name}")
		return True 
	
	def is_sunk_veritcal(self) -> bool:
		for i in range(self.size):
			try:
				if self.board.board[self.location[0]+i][self.location[1]] != "X ":
					return False
			except:
				return False
		print(f"You destroyed {self.player}'s {self.name}")
		return True 




	