from RandomAI import RandomAI

class SearchDestroyAI(RandomAI):
	def __init__(self, index: int, arguments: list, AI_type: str) -> None:
		super().__init__(index, arguments, AI_type)
		self.mode = "random"
		self.past = []
		self.hit_location = []
		self.next_shots = []

	def make_move(self, other: "Player") -> None:
		if self.mode == "destroy": 
			self.destroy(self.hit_location) 
			if len(self.next_shots) != 0:
				hit = (super().shoot_your_shot(other,self.next_shots[0][0],self.next_shots[0][1]) == 0)
				self.Possible_Moves.remove(self.next_shots[0])
				if (hit): 
					self.past.append(self.hit_location)
					self.hit_location = self.next_shots[0] 
					self.destroy(self.hit_location)
					self.next_shots.pop(0)
				else:
					self.next_shots.pop(0)
			if len(self.next_shots) == 0:
				self.mode = "random"
		elif self.mode == "random": 
			current_location = super().make_move(other) 
			self.mode = "destroy" 
			if current_location == 1:
				self.mode = "random" 
			else:
				self.hit_location = current_location
				self.past.append(current_location)


	
	def destroy(self,location:list)-> list:
		starting_row = location[0]
		starting_col = location[1]
		possible_targets = [[starting_row,starting_col-1],[starting_row-1, starting_col],[starting_row,starting_col+1],[starting_row+1, starting_col]]
		for i in possible_targets:
			if i not in self.next_shots:
				if i not in self.past:
					if 0 <= i[0] <= self.board.rows-1 and 0 <= i[1] <= self.board.cols-1:
						if self.board.scanning_board[i[0]][i[1]] != "X ":
							if self.board.scanning_board[i[0]][i[1]] != "O ":
								self.next_shots.append(i)






