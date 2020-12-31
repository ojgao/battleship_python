# inherit from AI player
from AIPlayer import AIPlayer
import random


class RandomAI(AIPlayer):
	def __init__(self, index: int, arguments: list, AI_type: str) -> None:
		super().__init__(index, arguments, AI_type)
		self.Possible_Moves = []
		for i in range(len(self.board.board)):
			for j in range(len(self.board.board[i])):
				self.Possible_Moves.append([i,j])

	def make_move(self, other: "Player") -> int:
		starting = self.attack_location(other)
		if self.shoot_your_shot(other,starting[0],starting[1]) == 0:
			return starting
		return self.shoot_your_shot(other,starting[0],starting[1])

	def attack_location(self, other: "Player") -> list:
		start = random.choice(self.Possible_Moves)
		self.Possible_Moves.remove(start)
		return start

	def shoot_your_shot(self, other: "Player",row,col)->int:
		for i in range(len(self.ships)):
			if other.ships[i].is_hit(row,col) == 1:
				self.board.edit_scanning(row,col,"X")
				other.board.edit(row,col,"X")
				if other.ships[i].orientation == "horizontal" and other.ships[i].is_sunk_horizontal(): 
					other.ships[i].status = "sunk"
				elif other.ships[i].orientation == "vertical" and other.ships[i].is_sunk_veritcal():
					other.ships[i].status = "sunk"
				return 0
			elif other.ships[i].is_hit(row,col) == 0:
				self.board.edit_scanning(row,col,"O")
				other.board.edit(row,col,"O")
				print("Miss")
				return 1   
		return 1