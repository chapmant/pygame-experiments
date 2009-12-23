#!/usr/bin/python

import pygame
from gem import Gem

class GameBoard:
	def __init__(self, rows, columns):
		pygame.init()
		self.height = rows * 25
		self.width = columns * 25
		self.size = self.height, self.width
		self.set_board()
		print self.size
		print self.height, self.width
	def set_board(self):
		self.board = pygame.Surface(self.size)
		self.board.fill((123,123,123))
		rect = self.size
		print rect
