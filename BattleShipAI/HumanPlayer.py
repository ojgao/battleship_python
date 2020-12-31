from Player import Player
from typing import Iterable
from Human_Ship import Human_Ship

class HumanPlayer(Player):
	def __init__(self, other_players: Iterable["Player"], index: int, arguments: list) -> None:
		self.name = self.get_name_from_player(other_players, index)
		super().__init__(self.name, index, arguments)
		self.ships = [Human_Ship(self.name, self.board,arguments[i],arguments[i+1]) for i in range(2,len(arguments)-1,2)]


	@staticmethod
	def get_name_from_player(other_players: Iterable["Player"], index: int ) -> str:
		already_used_names = set([player.name for player in other_players])
		name = input("Player {} please enter your name: ".format(index))
		while name in already_used_names:
			print(f"Someone is already using {name} for their name.\nPlease choose another name.")
			name = input("Player {} please enter your name: ".format(index))
		return name


	def make_move(self, other: "Player") -> None:
		shot = input(f"{self.name}, enter the location you want to fire at in the form row, column: ")
		try:
			x,y = shot.split(',')
			try: 
				x = int(x)
				try:	
					y = int(y)
					if not self.board.is_valid(x,y):
						print(f"{x}, {y} is not in bounds of our {self.board.rows} X {self.board.cols} board.")
						self.make_move(other)
					elif self.board.scanning_board[x][y] == "X " or self.board.scanning_board[x][y] == "O ":
						print(f"You have already fired at {x}, {y}.")
						self.make_move(other)
					else:
						for i in range(len(self.ships)):
							if other.ships[i].is_hit(x,y) == 1:
								self.board.edit_scanning(x,y,"X")
								other.board.edit(x,y,"X")
								if other.ships[i].is_sunk_horizontal() or other.ships[i].is_sunk_veritcal():
									other.ships[i].status = "sunk"
							elif other.ships[i].is_hit(x,y) == -1: 
								continue
							elif other.ships[i].is_hit(x,y) == 0:
								self.board.edit_scanning(x,y,"O")
								other.board.edit(x,y,"O")
						if other.board.board[x][y] == "O ":
							print("Miss")
				except ValueError:
					print(f"Column should be an integer. {y} is NOT an integer.")
					self.make_move(other)
				except:
					for i in range(len(self.ships)):
						self.board.edit_scanning(x,y,"X")
						other.board.edit(x,y,"X")
						if other.ships[i].is_sunk_horizontal() or other.ships[i].is_sunk_veritcal():
							other.ships[i].status = "sunk"
			except ValueError:
				print(f"Row should be an integer. {x} is NOT an integer.")
				self.make_move(other)
			except:
				if other.ships[i].is_sunk_horizontal() or other.ships[i].is_sunk_veritcal():
					other.ships[i].status = "sunk"
		except ValueError: 
			print(f"{shot} is not a valid location.")
			print("Enter the firing location in the form row, column")
			self.make_move(other)
		except:
			if other.ships[i].is_sunk_horizontal() or other.ships[i].is_sunk_veritcal():
				other.ships[i].status = "sunk"
			

