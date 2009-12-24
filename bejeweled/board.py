#!/usr/bin/python

import pygame
from gem import Gem

class GameBoard:
	gems = []
	def __init__(self, rows, columns):
		pygame.init()
		self.height = rows * 50
		self.width = columns * 50
		self.size = self.height, self.width
		print self.size
		self.set_board()
		print self.size
		print self.height, self.width
	def set_board(self):
		self.board = pygame.Surface(self.size)
		self.board.fill((123,123,123))
		rect = self.size
		print rect
		self.set_gems()
	def set_gems(self):
		gem_0 = pygame.image.load("gem0.png")
		rect = gem_0.get_rect()
		i = 0
		for row in range(0,self.height/25):
			for column in range(0,self.width/25):
				self.gems.append(Gem(gem_0, rect))
				self.board.blit(self.gems[i].gem, self.gems[i].rect)
				rect.left += 50
				i += 1
			rect.left = 0
			rect.top += 50
