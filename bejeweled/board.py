#!/usr/bin/env python

import pygame, random
from gem import Gem

class GameBoard:
	gems = []
	def __init__(self, rows, columns, height):
		pygame.init()
		self.size = height, height
		#print self.size
		self.set_board()
		#print self.size
		#print self.height, self.width
	def set_board(self):
		# Inits the board, fills it with color!
		self.board = pygame.Surface(self.size)
		self.board.fill((123,123,123))
		rect = self.size
		print rect
		self.set_gems()
	def set_gems(self):
		# Load the gem images
		gem_0 = pygame.image.load("gem0.png")
		gem_1 = pygame.image.load("gem1.png")
		gem_2 = pygame.image.load("gem2.png")
		gem_3 = pygame.image.load("gem3.png")
		gem_list = [gem_0, gem_1, gem_2, gem_3]
		# Get the rectangle of the gems
		rect = gem_0.get_rect()
		i = 0
		for row in range(0,self.size[0]/25):
			for column in range(0,self.size[1]/25):
				# Appends a newly generated Gem to the list of gems
				self.gems.append(Gem(gem_list[random.randint(0,3)], rect))
				# Blits the new Gem to the screen.
				self.board.blit(self.gems[i].gem, self.gems[i].rect)
				# Shifts the rectangle set by one width.
				rect.left += 50
				i += 1
			# Resets the Gem rectangle to the left, moves down a line.
			rect.left = 0
			rect.top += 50
