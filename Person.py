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
	def __init__(self,pos, L , R , U , D ):
		self.words = []
		self.dialogueNumber = 0
		self.combine = {}
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.

		self.imagesL = L
		self.imagesR = R
		self.imagesU = U
		self.imagesD = D
		self.imageLeft = 0
		self.imageRight = 0
		self.imageDown = 0
		self.imageUp = 0
		self.image = self.imagesD[0]
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		self.talkReaction = None

	def giveTalkTrigger(self, triggerWord):
		self.talkReaction = triggerWord

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

	def turn(self, direction):
		if direction == "left":
			self.image = self.imagesL[0]
		elif direction == "right":
			self.image = self.imagesR[0]
		elif direction == "up":
			self.image = self.imagesU[0]
		elif direction == "down":
			self.image = self.imagesD[0]

	# Function to give this person a dialogue script
	def addDialogue(self, dialogue, combine = False):
		if combine:
			self.combine[len(self.words) - 1] = True
			self.words.append(dialogue)
		else:
			self.words.append(dialogue)

	def goToLastDialogue(self):
		self.dialogueNumber = len(self.words) - 1
	def clearDialogueQuest(self, text):
		self.dialogueNumber = 0
		del self.words[:]
		self.combine.clear()
		for i in range(2):
			self.words.append(Dialogue(text))
	# Setting the position of a person in the case they move to a different location
	def setPosition(self, pos):
		self.rect.topleft = pos

	def getPosition(self):
		return self.rect

	'''
	The way getTextBox works is that there should be a 2d array for dialogue, after pressing SPACE it would then go on to the next piece of 
	dialogue. If there are choices call askDecision and then change choicePath. ChoicePath then determines what the character should say.
	'''
	def getTextBox(self, surface, activate = False):
		trigger = None
		if len(self.words) > 0:
			textToReturn = self.words[self.dialogueNumber]
		else:
			return 
		if isinstance(textToReturn, Dialogue):
			textToReturn.runText(surface, self.rect.y)
		else:
			trigger = textToReturn.runQuestion(surface, self.rect.y)

		keepRunning = self.dialogueNumber
		while keepRunning in self.combine:
			keepRunning += 1
			textToReturn = self.words[keepRunning]
			if isinstance(textToReturn, Dialogue):
				textToReturn.runText(surface, self.rect.y)
			else:
				trigger = textToReturn.runQuestion(surface, self.rect.y)
		if activate:
			return self.talkReaction
		return trigger

