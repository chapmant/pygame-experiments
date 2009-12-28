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

		# For each row in the map...
		for row in range(0, max_rows):
			# reset the board to empty...
			self.gems.append([])
			# then for each column in the map...
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
		#print event.pos
		#print event.button
		
		# Get the x and y positions from the button click
		y = event.pos[0]
		x = event.pos[1]
		location = [x, y]
		
		# Sets the (0,0) coord to be the upper left
		# corner of the game board
		location[0] -= self.size[0] / 18
		location[1] -= self.size[1] / 18
		#print location

		# If the location is in the bounds of the board...
		if location[0] < self.size[0] and location[1] < self.size[1] and location[0] > 0 and location[1] > 0:
			#print "in bounds!"
			
			# Compute the row and column of the click
			location[0] = int(location[0] / 50)
			location[1] = int(location[1] / 50)

			# Copy the clicked gem into a temp variable
			temp_gem_1 = self.gems[location[0]][location[1]]

			# If there is a gem to the right ...
			if location[1] < len(self.gems[location[0]])-1:

				# Copy the gem to the right to another temp var
				temp_gem_2 = self.gems[location[0]][location[1]+1]

				# Switch the two gems in the list
				self.gems[location[0]][location[1]] = self.gems[location[0]][location[1]+1]
				self.gems[location[0]][location[1]].rect = temp_gem_1.rect
				self.gems[location[0]][location[1]+1] = temp_gem_1
				self.gems[location[0]][location[1]+1].rect = temp_gem_2.rect

		# Clear the board for blitting
		self.board.fill((123,123,123))

		# Get the default rectangle for the gems
		rect = self.gems[0][0].rect
		rect.left = 0
		rect.top = 0

		# For each gem in the board...
		for row in range(0, len(self.gems)):
			for column in range(0, len(self.gems[0])):
				#print self.gems[row][column]
				#print row
				#print column
				#print rect, rect.left, rect.top, rect.bottom, rect.right, self.gems[row][column].rect
				#self.gems[row][column].rect = rect

				# Blit the gem to the board
				self.board.blit(self.gems[row][column].gem, self.gems[row][column].rect)

				# Shift the rectangle (change this to a var instead of magic number later)
				rect.left += 50
	
			# Reset the left edge.
			rect.left = 0

			# Push the row down by one.
			rect.top += 50
