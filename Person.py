import pygame, sys
from pygame.locals import *


# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

# This represents a person
class Person(pygame.sprite.Sprite):
	# This represents a person in our game

	myfont = pygame.font.Font(None, 22)
	words = []
	eventTrigger = 0
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

	def dialogueChoice(self, text):
		self.words.append(text)


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

	def getTextBox(self, surface):
		currentText = 0
		choicePath = 0
		textbox = pygame.Surface((surface.get_width(), 200))
		while True:

			textbox.fill(WHITE)

			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == K_SPACE:
						currentText += 1
						if currentText > len(self.words)-1:
							return
						makeChoice = len(self.words[currentText])
						if makeChoice > 1:
							choicePath = self.askDecision(surface, textbox, makeChoice, currentText)
							currentText += 1

			pygame.draw.rect(textbox, (BLACK), (0, 0, textbox.get_width(), textbox.get_height()), 2)
			textbox.blit(self.myfont.render(self.words[currentText][choicePath], True, (RED)), (150, 50))

			surface.blit(textbox, (0,400))


			pygame.display.update()
