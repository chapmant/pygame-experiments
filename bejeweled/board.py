#!/usr/bin/python

import pygame
from gem import Gem

class GameBoard:
	def __init__(self, rows, columns):
		height = rows * 25
		width = columns * 25
		self.size = height, width
		self.set_board()
	def set_board(self):
		self.board = pygame.Surface(self.size)
		self.board.fill((255,255,255))
