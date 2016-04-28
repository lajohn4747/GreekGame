import pygame, sys
from Person import *

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Weapon(pygame.sprite.Sprite):
	pos = (0,0)
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([8, 50])
		self.sideImage = pygame.Surface([50,8])
		self.topImage = pygame.Surface([8,50])
		self.image.fill(RED)

		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.topleft = self.pos

	def setPositionVertical(self, pos, direction):
		self.image = self.topImage
		self.rect = self.image.get_rect()
		if direction == 1:
			pos[1] -= 50
		self.rect.topleft = tuple(pos)

	def setPositionHorizontal(self, pos, direction):
		self.image = self.sideImage
		self.rect = self.sideImage.get_rect()
		if direction == 4:
			pos[0] -= 50
			pos[1] -= 8
		self.rect.topleft = tuple(pos)



class Hero(Person):
	likeAthena = 0
	direction = 1
	#weapon = pygame.Surface([8,50])
	weaponSide = pygame.Surface([50,8])
	weaponSide.fill(RED)
	#weapon.fill(RED)
	weapon = Weapon()

	def setSurface(self, surface):
		self.surface = surface
	def askDecision(self, surface, textSurface, choices, current):
		pass
	def getTextBox(self, surface):
		pass
	def increaseAthena(self,number):
		self.likeAthena += 1

	def getAction(self):
		#keys = pygame.key.get_pressed()
		#if keys[pygame.K_LSHIFT]:
		if(self.direction == 1):
			self.weapon.setPositionVertical([self.rect.x, self.rect.top], self.direction)
			self.surface.blit(self.weapon.image, self.weapon.rect)
		elif(self.direction == 2):
			self.weapon.setPositionHorizontal([self.rect.right, self.rect.y], self.direction)
			self.surface.blit(self.weapon.image, self.weapon.rect)
		elif(self.direction == 3):
			self.weapon.setPositionVertical([self.rect.x, self.rect.bottom], self.direction)
			self.surface.blit(self.weapon.image, self.weapon.rect)
		elif(self.direction == 4):
			self.weapon.setPositionHorizontal([self.rect.left, self.rect.bottom], self.direction)
			self.surface.blit(self.weapon.image, self.weapon.rect)
		else:
			return None

		return self.weapon

