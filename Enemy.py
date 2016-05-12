import pygame
import math
from Hero import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Enemy(pygame.sprite.Sprite):
	
	def __init__(self, pos, health, spriteGroup, L,R ,U, D, speed = 2):
		self.width = 50
		self.height = 50
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		#self.image = pygame.Surface([self.width, self.height])
		#self.image.fill(BLACK)
		self.health = health
		self.spriteGroup = spriteGroup
		self.imagesL = L
		self.imagesR = R
		self.imagesU = U
		self.imagesD = D
		self.image = self.imagesD[0]
		self.imageLeft = 0
		self.imageRight = 0
		self.imageDown = 0
		self.imageUp = 0
		self.speed = speed
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.topleft = pos

	def changeImage(self,U,R,D,L):
		self.imagesL = L
		self.imagesR = R
		self.imagesU = U
		self.imagesD = D

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
			
	def setPosition(self, pos):
		self.rect.topleft = pos

	def changeHealth(self, healthChange):
		self.health -= healthChange
		if self.health <= 0 :
			return True
		return False
	
	def wallCollide(self):
		return  self.rect.left < 0 or self.rect.right > 600 or self.rect.top < 0 or self.rect.bottom > 600

	def objectCollisions(self):
                for sprite in self.spriteGroup:
                        if pygame.sprite.collide_rect(self, self.spriteGroup[sprite]):
                                return True
                return None

	def pushBack(self, direction):
		if direction == 1:
			self.rect.y -= 40
		elif direction == 2:
			self.rect.x += 40
		elif direction == 4:
			self.rect.x -= 40
		elif direction == 3:
			self.rect.y += 40


	def chasePlayer(self, player):
		# find normalized direction vector (dx, dy) between enemy and player
		dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
		dist = math.hypot(dx, dy) + 0.01
		
		if self.rect.x > player.rect.x:
		    self.rect.x -= self.speed
		elif self.rect.x < player.rect.x:
		    self.rect.x += self.speed
		# Movement along y direction
		if self.rect.y < player.rect.y:
		    self.rect.y += self.speed
		elif self.rect.y > player.rect.y:
		    self.rect.y -= self.speed
		#change image
		if math.fabs(dx) > math.fabs(dy) and dx > 0:
			self.moveImage("left")
			if self.wallCollide() or self.objectCollisions() or dist < 20 :
				self.rect.x += 40
		elif math.fabs(dx) > math.fabs(dy) and dx <= 0:
			self.moveImage("right")
			if self.wallCollide() or self.objectCollisions() or dist < 20:
				self.rect.x -= 40
		if math.fabs(dy) > math.fabs(dx) and dy > 0:
			self.moveImage("up")
			if self.wallCollide() or self.objectCollisions() or dist < 20:
				self.rect.y += 40
		elif math.fabs(dy) > math.fabs(dx) and dy <= 0:
			self.moveImage("down")
			if self.wallCollide() or self.objectCollisions() or dist < 20:
				self.rect.y -= 40

		if dist < 20:
                        player.health -= 1

