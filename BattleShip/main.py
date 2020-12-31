import sys
from Game import Game

if __name__ == '__main__':
	content = []
	with open(sys.argv[1]) as file:
		line = file.readline()
		while line != "":
			content += line.split()
			line = file.readline()
	game = Game(content)
	game.play()