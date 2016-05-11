import pygame, sys


BLACK = (0,0,0)	
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

'''
The entire reason for this class is to give a immovable object thus making the scene appear to be more different
'''

class Building(pygame.sprite.Sprite):
	def __init__(self, width, height, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([width, height],pygame.SRCALPHA, 32)
		self.image = self.image.convert_alpha()
		#self.image.fill(RED)
		#image = pygame.Surface([640,480], pygame.SRCALPHA, 32)
                #image = image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = pos

	def getTextBox(self, surface):
		pass
