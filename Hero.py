import pygame, sys
from Person import *

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Hero(Person):
	likeAthena = 0


	def askDecision(self, surface, textSurface, choices, current):
		pass
	def getTextBox(self, surface):
		pass
	def increaseAthena(self,number):
		self.likeAthena += 1