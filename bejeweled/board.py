#!/usr/bin/env python

import pygame, random
from gem import Gem

class GameBoard:
	gems = []
	def __init__(self, rows, columns, height):
		pygame.init()

		# Determines the (square) size of the board
		# based on the value passed in, calls the
		# board setup
		self.size = height, height
		self.set_board()

	def set_board(self):
		# Inits the board, fills it with color!
		self.board = pygame.Surface(self.size)
		self.board.fill((123,123,123))
		rect = self.size
		self.set_gems()

	def set_gems(self):
		# Load the gem images
	#	gem_0 = pygame.image.load("gem0.png")
	#	gem_1 = pygame.image.load("gem1.png")
	#	gem_2 = pygame.image.load("gem2.png")
	#	gem_3 = pygame.image.load("gem3.png")
	#	gem_list = [gem_0, gem_1, gem_2, gem_3]
		gem_list = [pygame.image.load("gem0.png"), 
				pygame.image.load("gem1.png"), 
				pygame.image.load("gem2.png"), 
				pygame.image.load("gem3.png")]

		# Get the rectangle of the gems
		rect = gem_list[0].get_rect()
		i = 0
		max_rows = int(self.size[0] / 50)
		max_columns = int(self.size[1] / 50)
		row_spacing = self.size[0] / max_columns
		column_spacing = self.size[1] / max_rows

		for row in range(0, max_rows):
			self.gems.append([])
			for column in range(0, max_columns):
				# Appends a newly generated Gem to the list of gems
				self.gems[row].append(Gem(gem_list[random.randint(0,3)], rect))

				# Blits the new Gem to the screen.
				self.board.blit(self.gems[row][column].gem, self.gems[row][column].rect)

				# Shifts the rectangle set by one width.
				rect.left += row_spacing
				i += 1

			# Resets the Gem rectangle to the left, moves down a line.
			rect.left = 0
			rect.top += column_spacing
