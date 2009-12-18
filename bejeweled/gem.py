#!/usr/bin/python

import pygame, sys, random

class Gem:
	column = 0
	row = 0
	def __init__(self, image, gem_rect):
		self.gem = image
		self.rect = gem_rect
	def set_location(board_col, board_row):
		column = board_col
		row = board_row
	def blit():
		screen.blit(self.gem, self.gem_rect)
