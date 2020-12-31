import typing

class Board():

	def __init__(self, rows: int, cols: int, name: str = "")-> None:
		self.rows = rows
		self.cols = cols
		self.board  = [["* " for col in range(cols)] for row in range(rows)]
		self.scanning_board  = [["* " for col in range(cols)] for row in range(rows)]
		print(f"{name}'s Placement Board")
		self.format(self.board)

	@staticmethod
	def format(matrix:list)-> None:
		print("  ", end = "")
		for i in range(len(matrix[0])):
			print(f"{i} ",end = "")
		print()
		for row in range(len(matrix)):
			print(str(row)+ " ", end="")
			for i,col in enumerate(range(len(matrix[row]))):
				print(str(matrix[row][col]), end = "")
			print()

	def edit(self, row:int, col:int , char:str) -> None:
		self.board[row][col] = char + " "

	def edit_scanning(self, row:int, col:int, char:str) -> None:
		self.scanning_board[row][col] = char + " "

	def is_valid(self, row:int, col:int, orientation:str = 'n', size:int = 0)-> int:
		if row > self.rows-1 or col > self.cols-1 or row < 0 or col < 0:
			return 0
		try: 
			for i in range(size):
				if orientation == 'h':
					if self.board[row][col+i] != "* " or col+i > self.cols-1:
						return 1
				if orientation == 'v':
					if self.board[row+i][col] != "* " or row+i > self.rows-1:
						return 1
			return 2
		except:
			return -1
	def is_intersecting(self, row:int, col:int, size:int)->list:
		inter_ships= []
		i = 0
		while i<size:
			if self.board[row][col+i] != "* " and self.board[row][col+i].strip() not in inter_ships:
				inter_ships.append(self.board[row][col+i].strip())
			elif self.board[row+i][col] != "* " and self.board[row+i][col].strip() not in inter_ships:
				inter_ships.append(self.board[row+i][col].strip())
			i += 1
		return sorted(inter_ships)

	def display_scanning(self)-> None:
		matrix = self.scanning_board
		print("  ", end = "")
		for i in range(len(matrix[0])):
			print(f"{i} ",end = "")
		print()
		for row in range(len(matrix)):
			print(str(row)+ " ",end="")
			for i,col in enumerate(range(len(matrix[row]))):
				print(str(matrix[row][col]), end = "")
			print()
		print()

