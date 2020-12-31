# inherit from player
from Player import Player
from AI_Ship import AI_Ship
from abc import ABC, abstractmethod


class AIPlayer(Player):
	def __init__(self, index: int, arguments: list, AI_type: str) -> None:
		self.name = self.get_name_from_player(AI_type, index)
		super().__init__(self.name, index, arguments)
		self.ships = [AI_Ship(self.name, self.board,arguments[i],arguments[i+1]) for i in range(2,len(arguments)-1,2)]


	@staticmethod
	def get_name_from_player(AI_type:str, index :int)-> str:
		return (f"{AI_type} {index}")

	@abstractmethod
	def make_move(self, other: "Player") -> None:
		pass


