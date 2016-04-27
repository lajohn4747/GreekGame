import pygame, sys
from pygame.locals import *


# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

'''
	The Person class is a sprite and should be the parent of the Enemy class. A regular person is usually just an object that
	is able to interact with the hero only through conversation. 
'''
class Person(pygame.sprite.Sprite):
	# This represents a person in our game

	myfont = pygame.font.Font(None, 22)
	words = []
	eventTrigger = {}

	'''
	Initialize a person with their position and width and height to scale according to screen size
	'''
	def __init__(self,width,height,pos):
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
	def dialogueChoice(self, text):
		self.words.append(text)

	# Setting the position of a person in the case they move to a different location
	def setPosition(self, pos):
		self.rect.topleft = pos

	'''
	This is when choices could be made, it handles to choice indicator to show which choice the player is choosing
	It also determines the outcome of the answer
	'''
	def askDecision(self, surface, textSurface, choices, current):
		arrowX = 50
		chosen = 0
		while True:
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == K_DOWN:
						if(arrowX < 50 * choices):
							arrowX += 50
							chosen += 1
					elif event.key == K_UP:
						if(arrowX > 50):
							arrowX -= 50
							chosen -= 1
					elif event.key == K_SPACE:
						return chosen

			textSurface.fill(WHITE)
			pygame.draw.rect(textSurface, ((BLACK)), (0, 0, textSurface.get_width(), textSurface.get_height()), 2)
			pygame.draw.rect(textSurface, ((BLACK)), (110, arrowX, 20, 20), 2)
			for i in range(choices):
				textSurface.blit(self.myfont.render(self.words[current][i], True, (RED)), (150, 50+50*i))
			surface.blit(textSurface, (0,400))
			pygame.display.update()


	'''
	The way getTextBox works is that there should be a 2d array for dialogue, after pressing SPACE it would then go on to the next piece of 
	dialogue. If there are choices call askDecision and then change choicePath. ChoicePath then determines what the character should say.
	'''
	def getTextBox(self, surface):
		currentText = 0
		choicePath = 0
		textbox = pygame.Surface((surface.get_width(), 200))
		trigger = None

		while True:

			textbox.fill(WHITE)

			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == K_SPACE:
						currentText += 1
						if currentText > len(self.words)-1:
							return trigger
						makeChoice = len(self.words[currentText])
						if makeChoice > 1:
							choicePath = self.askDecision(surface, textbox, makeChoice, currentText)
							if(self.checkTrigger((currentText,choicePath))):
								trigger = self.activateTrigger((currentText,choicePath))
							currentText += 1

			pygame.draw.rect(textbox, (BLACK), (0, 0, textbox.get_width(), textbox.get_height()), 2)
			textbox.blit(self.myfont.render(self.words[currentText][choicePath], True, (RED)), (150, 50))

			surface.blit(textbox, (0,400))


			pygame.display.update()


	def activateTrigger(self, currentTextAndChoice):
		return self.eventTrigger[currentTextAndChoice]

	def setTrigger(self, currentTextAndChoice, newEvent):
		self.eventTrigger[currentTextAndChoice] = newEvent

	def checkTrigger(self, currentTextAndChoice):
		if currentTextAndChoice in self.eventTrigger:
			return True
		return False
