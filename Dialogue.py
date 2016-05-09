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


	def runText(self, surface):
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
			
			textbox.blit(self.myfont.render(self.textboxes[currentWords], True, (RED)), (150, 50))
			textbox.blit(self.myfont.render(self.textboxes[currentWords + 1], True, (RED)), (150, 100))
			textbox.blit(self.myfont.render(self.textboxes[currentWords + 2], True, (RED)), (150, 150))


			surface.blit(textbox, (0,400))
			pygame.display.update()