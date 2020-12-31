# inherit from AI player
from AIPlayer import AIPlayer

class CheatingAI(AIPlayer):
	def __init__(self, index: int, arguments: list, AI_type: str) -> None:
		super().__init__(index, arguments, AI_type)

	def make_move(self, other: "Player") -> int:
		for i in range(len(other.board.board)):
			for j in range(len(other.board.board[i])):
				for ship in range(len(self.ships)):
					if other.ships[ship].is_hit(i,j) == 1:
						self.board.edit_scanning(i,j,"X")
						other.board.edit(i,j,"X")
						if other.ships[ship].orientation == "horizontal" and other.ships[ship].is_sunk_horizontal(): 
							other.ships[ship].status = "sunk"
						elif other.ships[ship].orientation == "vertical" and other.ships[ship].is_sunk_veritcal():
							other.ships[ship].status = "sunk"
						return (0)
					elif other.ships[ship].is_hit(i,j) == -1: 
						continue
					elif other.ships[ship].is_hit(i,j) == 0:
						continue


