import pygame, sys
from pygame.locals import *

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Dialogue:
	myfont = pygame.font.Font(None, 22)


	def __init__(self, words):
		self.textboxes = []
		self.wordArray = words.split()
		stringBox = ""
		for i in self.wordArray:
			if len(stringBox) < 50:
				stringBox += i + " "
			else:
				self.textboxes.append(stringBox)
				stringBox = i + " "
		self.textboxes.append(stringBox)
		while (len(self.textboxes) % 3 != 0):
			self.textboxes.append("")


	def runText(self, surface, currentY):
		textbox = pygame.Surface((surface.get_width(), 200))
		currentWords = 0
		while True:
			textbox.fill(WHITE)
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == K_SPACE:
						currentWords += 3
						if currentWords >= len(self.textboxes):
							return

			pygame.draw.rect(textbox, (BLACK), (0, 0, textbox.get_width(), textbox.get_height()), 2)
			
			textbox.blit(self.myfont.render(self.textboxes[currentWords], True, (BLACK)), (80, 50))
			textbox.blit(self.myfont.render(self.textboxes[currentWords + 1], True, (BLACK)), (80, 100))
			textbox.blit(self.myfont.render(self.textboxes[currentWords + 2], True, (BLACK)), (80, 150))

			if currentY < 300:
				surface.blit(textbox, (0,400))
			else:
				surface.blit(textbox, (0,0))
			pygame.display.update()