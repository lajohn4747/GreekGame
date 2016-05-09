import pygame, sys
from pygame.locals import *

from Scene import *

FPS = 60
fpsClock = pygame.time.Clock()

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
		self.enemies = scene.enemies
		self.transition_points = scene.transition_points

		self.scene = scene
		self.instructions = actions

	def runScene(self):
		for i in self.instructions:
			spriteToMove = i[0]
			action = i[1]
			if action == "moveLeft":
				while spriteToMove.rect.left > i[2]:
					spriteToMove.rect.left -= 5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					#fpsClock.tick(FPS)
			elif action == "moveRight":
				while spriteToMove.rect.right < i[2]:
					spriteToMove.rect.right += 5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					#fpsClock.tick(FPS)
			elif action == "moveDown":
				while spriteToMove.rect.bottom < i[2]:
					spriteToMove.rect.bottom += 5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					#fpsClock.tick(FPS)
			elif action == "moveUp":
				while spriteToMove.rect.top > i[2]:
					spriteToMove.rect.top -=5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					#fpsClock.tick(FPS)
			elif action == "talk":
				talking = Dialogue(i[2])
				talking.runText(self.mainSurface)


