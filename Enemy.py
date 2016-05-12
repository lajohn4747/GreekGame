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
		#self.image = pygame.Surface([self.width, self.height])
		#self.image.fill(BLACK)
		#self.health = health
		self.image = pygame.image.load('enemy_down.png').convert_alpha()
		self.imagesL = [pygame.image.load('enemy_left.png'), pygame.image.load('enemy_left_L.png'), pygame.image.load('enemy_left_R.png')]
		self.imagesR = [pygame.image.load('enemy_right.png'), pygame.image.load('enemy_right_L.png'), pygame.image.load('enemy_right_R.png')]
		self.imagesU = [pygame.image.load('enemy_up.png'), pygame.image.load('enemy_up_L.png'), pygame.image.load('enemy_up_R.png')]
		self.imagesD = [pygame.image.load('enemy_down.png'), pygame.image.load('enemy_down_L.png'), pygame.image.load('enemy_down_R.png')]
		self.imageLeft = 0
		self.imageRight = 0
		self.imageDown = 0
		self.imageUp = 0
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.topleft = pos

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
		if self.health < 0 :
			return True
		return False
	
	def wallCollide(self):
		return  self.rect.left < 0 or self.rect.right > 600 or self.rect.top < 0 or self.rect.bottom > 600
	
	def chasePlayer(self, player):
		# find normalized direction vector (dx, dy) between enemy and player
		dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
		dist = math.hypot(dx, dy)
		dx, dy = dx / dist, dy / dist
		speed = 1
		
		if self.rect.x > player.rect.x:
		    self.rect.x -= speed
		elif self.rect.x < player.rect.x:
		    self.rect.x += speed
		# Movement along y direction
		if self.rect.y < player.rect.y:
		    self.rect.y += speed
		elif self.rect.y > player.rect.y:
		    self.rect.y -= speed
		#change image
		if math.fabs(dx) > math.fabs(dy) and dx > 0:
			self.moveImage("left")
			if self.wallCollide():
				self.rect.x -= 3
		elif math.fabs(dx) > math.fabs(dy) and dx <= 0:
			self.moveImage("right")
			if self.wallCollide():
				self.rect.x += 3
		if math.fabs(dy) > math.fabs(dx) and dy > 0:
			self.moveImage("up")
			if self.wallCollide():
				self.rect.y += 3
		elif math.fabs(dy) > math.fabs(dx) and dy <= 0:
			self.moveImage("down")
			if self.wallCollide():
				self.rect.y -= 3

