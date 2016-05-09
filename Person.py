import pygame, sys
from pygame.locals import *


# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

from Dialogue import *

'''
	The Person class is a sprite and should be the parent of the Enemy class. A regular person is usually just an object that
	is able to interact with the hero only through conversation. 
'''
class Person(pygame.sprite.Sprite):
	# This represents a person in our game

	myfont = pygame.font.Font(None, 22)

	'''
	Initialize a person with their position and width and height to scale according to screen size
	'''
	def __init__(self,width,height,pos):
		self.words = []
		self.dialogueNumber = 0
		self.combine = {}
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(BLUE)

		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.topleft = pos

	# Function to give this person a dialogue script
	def addDialogue(self, dialogue, combine = False):
		if combine:
			self.combine[len(self.words) - 1] = True
			self.words.append(dialogue)
		else:
			self.words.append(dialogue)

	def goToLastDialogue(self):
		self.dialogueNumber = len(self.words) - 1
	# Setting the position of a person in the case they move to a different location
	def setPosition(self, pos):
		self.rect.topleft = pos

	'''
	The way getTextBox works is that there should be a 2d array for dialogue, after pressing SPACE it would then go on to the next piece of 
	dialogue. If there are choices call askDecision and then change choicePath. ChoicePath then determines what the character should say.
	'''
	def getTextBox(self, surface):
		trigger = None
		textToReturn = self.words[self.dialogueNumber]
		if isinstance(textToReturn, Dialogue):
			textToReturn.runText(surface)
		else:
			trigger = textToReturn.runQuestion(surface)

		keepRunning = self.dialogueNumber
		while keepRunning in self.combine:
			keepRunning += 1
			textToReturn = self.words[keepRunning]
			if isinstance(textToReturn, Dialogue):
				textToReturn.runText(surface)
			else:
				trigger = textToReturn.runQuestion(surface)

		return trigger

