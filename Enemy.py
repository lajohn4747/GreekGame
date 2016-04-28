import pygame 
from Hero import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Enemy(pygame.sprite.Sprite):
	width = 50
	height = 50
	def __init__(self, pos, health):
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