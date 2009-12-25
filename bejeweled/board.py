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

			# Resets the Gem rectangle to the left, moves down a line.
			rect.left = 0
			rect.top += column_spacing

	def switch_gems(self, event):
		print event.pos
		print event.button
		y = event.pos[0]
		x = event.pos[1]
		location = [x, y]
		location[0] -= self.size[0] / 18
		location[1] -= self.size[1] / 18
		print location
		if location[0] < self.size[0] and location[1] < self.size[1] and location[0] > 0 and location[1] > 0:
			print "in bounds!"
			location[0] = int(location[0] / 50)
			location[1] = int(location[1] / 50)
			temp_gem_1 = self.gems[location[0]][location[1]]
			if location[0] < len(self.gems[location[0]]):
				temp_gem_2 = self.gems[location[0]][location[1]+1]
				self.gems[location[0]][location[1]] = self.gems[location[0]][location[1]+1]
				self.gems[location[0]][location[1]].rect = temp_gem_1.rect
				self.gems[location[0]][location[1]+1] = temp_gem_1
				self.gems[location[0]][location[1]+1].rect = temp_gem_2.rect
		self.board.fill((123,123,123))
		rect = self.gems[0][0].rect
		rect.left = 0
		rect.top = 0
		for row in range(0, len(self.gems)):
			for column in range(0, len(self.gems[0])):
				#print self.gems[row][column]
				#print row
				#print column
				print rect, rect.left, rect.top, rect.bottom, rect.right, self.gems[row][column].rect
				#self.gems[row][column].rect = rect
				self.board.blit(self.gems[row][column].gem, self.gems[row][column].rect)
				rect.left += 50
			rect.left = 0
			rect.top += 50
