import pygame, sys
from pygame.locals import *

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Question:
	myfont = pygame.font.Font(None, 22)

	def __init__(self, text, choices, triggers):
		self.text = text
		self.choices = choices
		self.triggers = triggers

	def runQuestion(self, surface, currentLocation):
		textSurface = pygame.Surface((surface.get_width(), 200))
		arrowX = 90
		chosen = 0
		while True:
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == K_DOWN:
						if(arrowX < 30 * len(self.choices) + 90):
							arrowX += 30
							chosen += 1
					elif event.key == K_UP:
						if(arrowX > 90):
							arrowX -= 30
							chosen -= 1
					elif event.key == K_SPACE:
						return self.triggers[chosen]

			textSurface.fill(WHITE)
			pygame.draw.rect(textSurface, ((RED)), (0, 0, textSurface.get_width(), textSurface.get_height()), 2)
			pygame.draw.rect(textSurface, ((RED)), (80, arrowX, 15, 15), 2)
			textSurface.blit(self.myfont.render(self.text, True, (RED)), (100, 30))
			for i in range(len(self.choices)):
				textSurface.blit(self.myfont.render(self.choices[i], True, (RED)), (100, 90+30*i))

			if currentLocation < 300:
				surface.blit(textSurface, (0,400))
			else:
				surface.blit(textSurface, (0,0))
			pygame.display.update()
