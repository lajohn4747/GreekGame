import pygame, sys
from pygame.locals import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Question:
	myfont = pygame.font.Font(None, 22)

	def __init__(self, text, choices, triggers):
		self.text = text
		self.choices = choices
		self.triggers = triggers

	def runQuestion(self, surface):
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
			pygame.draw.rect(textSurface, ((BLACK)), (0, 0, textSurface.get_width(), textSurface.get_height()), 2)
			pygame.draw.rect(textSurface, ((BLACK)), (80, arrowX, 15, 15), 2)
			textSurface.blit(self.myfont.render(self.text, True, (BLACK)), (100, 30))
			for i in range(len(self.choices)):
				textSurface.blit(self.myfont.render(self.choices[i], True, (BLACK)), (100, 90+30*i))
			surface.blit(textSurface, (0,400))
			pygame.display.update()
