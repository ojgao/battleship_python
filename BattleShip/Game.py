import typing
from Player import Player

class Game():
	def __init__(self, arguments:list)-> None:
		self.players = []
		self.players.append(Player(self.players, 1, arguments))
		self.players.append(Player(self.players, 2, arguments))
		self.turn = 0 

	@property
	def current_player(self) -> "Player":
		return self.players[self.turn]

	def play(self)-> None:
		while not self.game_over():
			self.current()
			self.current_player.make_move(self.players[(self.turn+1)%2])
			self.current()
			self.change_player()
		self.change_player()
		self.is_winner()

	def game_over(self) -> bool :
		p1_lose = True
		p2_lose = True
		for i in self.current_player.ships:
			if i.status != "sunk":
				p1_lose = False
		for i in self.players[(self.turn+1)%2].ships:
			if i.status != "sunk":
				p2_lose = False
		return (p1_lose or p2_lose)

	def change_player(self) -> None:
		self.turn = (self.turn + 1) % 2

	def current(self) -> None:
		print(f"{self.current_player.name}'s Scanning Board")
		self.current_player.board.format(self.current_player.board.scanning_board)
		print(f"{self.current_player.name}'s Board")
		self.current_player.board.format(self.current_player.board.board)

	def is_winner(self) -> None:
		print(f"{self.players[self.turn].name} won the game!")