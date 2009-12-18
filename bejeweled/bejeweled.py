#!/usr/bin/python

import sys, pygame
from pygame.locals import *
pygame.init();

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

gem = pygame.image.load("gem.png")
gemrect = gem.get_rect()
gemrect2 = gem.get_rect()
gemrect2.left = gemrect2.left + 50 

print gemrect

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)
	screen.blit(gem, gemrect)
	screen.blit(gem, gemrect2)
	pygame.display.flip()
