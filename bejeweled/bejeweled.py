#!/usr/bin/python

import sys, pygame, random
from  gem import Gem
from pygame.locals import *

def print_screen(gems, gemrects):
	screen.fill(black)
	for x in range(10):
		for y in range(10):
			temp_gem = Gem(gems[random.randint(0,3)], gemrect)
			gem_list.append(temp_gem)
			screen.blit(gem_list[len(gem_list)-1].gem, gem_list[len(gem_list)-1].rect)
			gemrect.left = gemrect.left + (50)
		gemrect.top = gemrect.top + (50)
		gemrect.left = 0

def move_right(mouse_pos):
	column = mouse_pos[0] / 50
	row = mouse_pos[1] / 50


pygame.init()
size = width, height = 800, 520
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

gem0 = pygame.image.load("gem0.png").convert()
gem1 = pygame.image.load("gem1.png").convert()
gem2 = pygame.image.load("gem2.png").convert()
gem3 = pygame.image.load("gem3.png").convert()

gem_list = [gem0, gem1, gem2, gem3]

gemrect = gem0.get_rect()
print_screen(gem_list, gemrect)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			move_right(pygame.mouse.get_pos())

#	screen.blit(gem, gemrect)
#	screen.blit(gem, gemrect2)
	pygame.display.flip()
