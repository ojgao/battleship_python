import typing
import Player 
from Ship import Ship

class Human_Ship(Ship):
	def __init__(self, player: "Player", board: "Board", name: str, size: str)-> None:
		super().__init__(player, board, name, size)

	def place_ships(self) -> list:
		h = "horizontal"
		horizontal_calls = [h[0:i+1] for i in range(len(h))]
		v = "vertical"
		vertical_calls = [v[0:i+1] for i in range(len(v))]
		orientation = input(f"{self.player} enter horizontal or vertical for the orientation of {self.name} which is {self.size} long: ")
		orientation = orientation.lower()
		orientation = orientation.strip()
		if orientation not in horizontal_calls and orientation not in vertical_calls:
			print(f"{orientation} does not represent an Orientation")
			return self.place_ships()
		else: 
			start = input(f"{self.player}, enter the starting position for your {self.name} ship ,which is {self.size} long, in the form row, column: ")
			try:
				x,y = start.split(',')
				try: 
					x = int(x)
					try:	
						y = int(y)
						if orientation in horizontal_calls:
							self.orientation = "horizontal"
							if self.board.is_valid(x,y) == 0:
								print(f"Cannot place {self.name} horizontally at {x}, {y} because it would be out of bounds.")
								return self.place_ships()
							elif self.board.is_valid(x,y,'h',self.size) == -1:
								print(f"Cannot place {self.name} horizontally at {x}, {y} because it would end up out of bounds.")
								return self.place_ships()
							elif self.board.is_valid(x,y,'h',self.size) == 1:
								print(f"Cannot place {self.name} horizontally at {x}, {y} because it would overlap with {self.board.is_intersecting(x,y,self.size)}")
								return self.place_ships()
							else:
								for i in range(self.size):
									self.board.edit(x,y+i,self.name[0])
								print(f"{self.player}'s Placement Board")
								self.board.format(self.board.board)
								return [x,y]
						elif orientation in vertical_calls:
							self.orientation = "vertical"
							if self.board.is_valid(x,y) == 0 :
								print(f"Cannot place {self.name} vertically at {x}, {y} because it would be out of bounds.")
								return self.place_ships()
							elif self.board.is_valid(x,y,'v',self.size) == -1:
								print(f"Cannot place {self.name} vertically at {x}, {y} because it would end up out of bounds.")
								return self.place_ships()
							elif self.board.is_valid(x,y,'v',self.size) == 1:
								print(f"Cannot place {self.name} vertically at {x}, {y} because it would overlap with {self.board.is_intersecting(x,y,self.size)}")
								return self.place_ships()
							else:
								for i in range(self.size):
									self.board.edit(x+i,y,self.name[0])
								print(f"{self.player}'s Placement Board")
								self.board.format(self.board.board)
								return [x,y]

					except ValueError:
						print(f"{y} is not a valid value for column.")
						print(f"It should be an integer between 0 and {self.board.cols-1}")
						return self.place_ships()
					except:
						return [x,y]
				except ValueError:
					print(f"{x} is not a valid value for row.")
					print(f"It should be an integer between 0 and {self.board.rows-1}")
					return self.place_ships()
				except:
					return [x,y]
				
			except ValueError: 
				print(f"{start} is not in the form x,y")
				return self.place_ships()
			except:
				return [x,y]




	