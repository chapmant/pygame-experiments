#!/usr/bin/env python

import pygame, sys
from board import GameBoard

class Game:
	# Arbitrary color added for science
	black = (100,100,100)

	# Two numbers determine the size of the board
	# [ width, height ] 
	game_rect = [ 700, 500]

	# Sets up a global GameBoard instance
	board = GameBoard(10,10, .9 * game_rect[1])

	def __init__(self):
		pygame.init()

		# Sets the video mode, calls the main function.
		self.screen = pygame.display.set_mode(self.game_rect)
		self.game_main()

	def game_main(self):
		# Sets the rectangle for the game board's location based off of the screen size
		board_rect = [.05 * self.game_rect[1], .05 * self.game_rect[1], .05 * self.game_rect[1], .05 * self.game_rect[1]]

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					print "Mouse clicked."

			# Clears the screen, blits the board and refreshes the screen.
			self.screen.fill(self.black)
			self.board.board.convert()
			self.screen.blit(self.board.board, board_rect)
			pygame.display.flip()

def main():
	game = Game()

if __name__ == "__main__":
	main()
