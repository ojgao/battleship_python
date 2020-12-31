import typing
from Player import Player
from HumanPlayer import HumanPlayer
from CheatingAI import CheatingAI
from SearchDestroyAI import SearchDestroyAI
from RandomAI import RandomAI

class Game():
	def __init__(self, arguments:list)-> None:
		self.players = []
		for i in range(2):
			AI_t = self.get_AI_type(i+1)
			if AI_t == 'Human':
				self.players.append(HumanPlayer(self.players, i+1, arguments))
			elif AI_t == 'CheatingAi':
				self.players.append(CheatingAI(i+1, arguments, "Cheating Ai"))
			elif AI_t == 'SearchDestroyAi':
				self.players.append(SearchDestroyAI(i+1, arguments, "Search Destroy AI"))
			elif AI_t == 'RandomAi':
				self.players.append(RandomAI(i+1, arguments, "Random Ai"))
		self.turn = 0 

	@property
	def current_player(self) -> "Player":
		return self.players[self.turn]

	def get_AI_type(self, index : int) -> str:
		types = ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi']
		possible_type = [['human'], ['cheatingai'], ['searchdestroyai'], ['randomai']]
		for AI in possible_type:
			for char in range(len(AI[0])):
				AI.append(AI[0][0:char+1])
		AI_type = input(f"Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player {index}'s type: ")
		AI_type = AI_type.lower()
		AI_type = AI_type.strip()
		while True:
			if(AI_type not in possible_type[0]): 
				if (AI_type not in possible_type[1]): 
					if (AI_type not in possible_type[2]): 
						if (AI_type not in possible_type[3]):
							print(f"{AI_type} is not one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi']")
							AI_type = input(f"Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player {index}'s type: ")
						else:
							return types[3]
					else: 
						return types[2]
				else:
					return types[1]
			else:
				return types[0]

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
