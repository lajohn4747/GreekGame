import pygame, sys
from pygame.locals import *

from Scene import *

class CutScene:
	def __init__(self, scene, actions):
		self.entrancePointsX = scene.entrancePointsX
		self.entrancePointsY = scene.entrancePointsY
		self.talkingTo = scene.talkingTo
		self.level = scene.level
		self.spriteGroup = scene.spriteGroup
		self.hero = scene.hero
		self.background = scene.background
		self.mainSurface = scene.mainSurface
		self.enemies = scene.enemyList
		self.transition_points = scene.transition_points

		self.instructions = actions


	def runScene(self):
		pass
