#!/usr/bin/env python

import pygame, sys
from board import GameBoard

class Game:
	black = (100,100,100)
	game_rect = [0, 0, 1000, 500]
	board = GameBoard(10,10, .9 * game_rect[3])
	def __init__(self):
		pygame.init()
		size = width, height = self.game_rect[2], self.game_rect[3]
		self.screen = pygame.display.set_mode(size)
		self.game_main()
		#self.board = GameBoard(10, 10)
		self.screen.blit(self.board.board, self.board.board.get_rect())
	def game_main(self):
		print "Test"
		print self.board.board.get_rect()
		#game_rect = self.screen.get_rect()
		board_rect = [.05 * self.game_rect[3], .05 * self.game_rect[3], .05 * self.game_rect[3], .05 * self.game_rect[3]]
		print board_rect
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					print "Mouse clicked."
			self.screen.fill(self.black)
			self.screen.blit(self.board.board, board_rect)
			pygame.display.flip()

def main():
	game = Game()

if __name__ == "__main__":
	main()
