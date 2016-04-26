import pygame

class Scene:

	# May be possible to have multiple sprites
	def __init__(self, mainSurface):
		self.spriteGroups = pygame.sprite.Group()
