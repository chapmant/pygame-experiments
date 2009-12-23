#!/usr/bin/python

import pygame, sys
from board import GameBoard

class Game:
	black = (100,100,100)
	board = GameBoard(10,10)
	def __init__(self):
		pygame.init()
		size = width, height = 800, 600
		self.screen = pygame.display.set_mode(size)
		self.game_main()
		#self.board = GameBoard(10, 10)
		self.screen.blit(self.board.board, self.board.board.get_rect())
	def game_main(self):
		print "Test"
		print self.board.board.get_rect()
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					print "Mouse clicked."
			self.screen.fill(self.black)
			self.screen.blit(self.board.board, self.board.board.get_rect())
			pygame.display.flip()

def main():
	game = Game()

if __name__ == "__main__":
	main()
