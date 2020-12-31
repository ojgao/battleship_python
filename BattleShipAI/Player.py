from Board import Board 
from Ship import Ship 
from typing import Iterable
from abc import ABC, abstractmethod

class Player():
	def __init__(self, name: str, index: int, arguments: list) -> None:
		self.board = Board(int(arguments[0]),int(arguments[1]), name)

	@staticmethod
	@abstractmethod
	def get_name_from_player(self)->None:
		pass

	@abstractmethod
	def make_move(self, other: "Player") -> None:
		pass
			

