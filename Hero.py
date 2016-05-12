import pygame, sys
from Person import *

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Weapon(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pos = (0,0)
		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([8, 50])
		self.sideImage = pygame.Surface([50,8])
		self.topImage = pygame.Surface([8,50])
		self.image.fill(RED)
		self.health = 10

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
	def __init__(self,width,height,pos):
		self.words = []
		self.dialogueNumber = 0
		self.combine = {}
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.image.load('hero_front.png').convert_alpha()

		self.imagesL = [pygame.image.load('hero_left.png'), pygame.image.load('hero_left_L.png'), pygame.image.load('hero_left_R.png')]
		self.imagesR = [pygame.image.load('hero_right.png'), pygame.image.load('hero_right_L.png'), pygame.image.load('hero_right_R.png')]
		self.imagesU = [pygame.image.load('hero_up.png'), pygame.image.load('hero_up_L.png'), pygame.image.load('hero_up_R.png')]
		self.imagesD = [pygame.image.load('hero_down.png'), pygame.image.load('hero_down_L.png'), pygame.image.load('hero_down_R.png')]
		self.imageLeft = 0
		self.imageRight = 0
		self.imageDown = 0
		self.imageUp = 0
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		self.athensPoints = 0
		self.spartaPoints = 0
		self.delphiPoints = 0
		self.health = 3
	
	direction = 1
	weaponSide = pygame.Surface([50,8])
	weaponSide.fill(RED)
	weapon = Weapon()

	seenScene = {}
	def resetImage(self, direction):
		if direction == "left":
			self.imageRight = 0
			self.imageDown = 0
			self.imageUp = 0
		elif direction == "right":
			self.imageLeft = 0
			self.imageDown = 0
			self.imageUp = 0
		elif direction == "down":
			self.imageRight = 0
			self.imageLeft = 0
			self.imageUp = 0
		elif direction == "up":
			self.imageRight = 0
			self.imageDown = 0
			self.imageLeft = 0

	def moveImage(self, direction):
		self.resetImage(direction)
		if direction == "left":
			self.imageLeft += 1
			if self.imageLeft > 2:
				self.imageLeft = 0
			self.image = self.imagesL[self.imageLeft]
		elif direction == "right":
			self.imageRight += 1
			if self.imageRight > 2:
				self.imageRight = 0
			self.image = self.imagesR[self.imageRight]
		elif direction == "down":
			self.imageDown += 1
			if self.imageDown > 2:
				self.imageDown = 0
			self.image = self.imagesD[self.imageDown]
		elif direction == "up":
			self.imageUp += 1
			if self.imageUp > 2:
				self.imageUp = 0
			self.image = self.imagesU[self.imageUp]

	def checkScene(self, scene):
		seenScene[scene] = True
	def setSurface(self, surface):
		self.surface = surface

	def askDecision(self, surface, textSurface, choices, current):
		pass

	def getTextBox(self, surface):
		pass

	def increasePoints(self, city, number):
		if city == "sparta":
			self.spartaPoints += number
			if self.spartaPoints > 3:
				return "Spartan3"
			else:
				return None
		elif city == "athens":
			self.athensPoints += number
			if self.athensPoints >= 3:
				return "Athens3"
			else:
				return None
		elif city == "delphi":
			self.delphiPoints += number

	def getAction(self):
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

