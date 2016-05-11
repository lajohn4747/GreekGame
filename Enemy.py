import pygame
import math
from Hero import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Enemy(pygame.sprite.Sprite):
	
	def __init__(self, pos, health):
		self.width = 50
		self.height = 50
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(BLACK)
		self.health = health
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.topleft = pos

	def setPosition(self, pos):
		self.rect.topleft = pos

	def changeHealth(self, healthChange):
		self.health -= healthChange
		if self.health < 0 :
			return True
		return False
	def chasePlayer(self, player):
		# find normalized direction vector (dx, dy) between enemy and player
		dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
		dist = math.hypot(dx, dy)
		dx, dy = dx / dist, dy / dist
		# move along this normalized vector towards the player at current speed
		self.rect.x += dx * self.speed
		self.rect.y += dy * self.speed
