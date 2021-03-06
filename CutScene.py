import pygame, sys
from pygame.locals import *

from Scene import *
from Question import *
FPS = 60
fpsClock = pygame.time.Clock()

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


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
					spriteToMove.moveImage("left")
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "moveRight":
				while spriteToMove.rect.right < i[2]:
					spriteToMove.rect.right += 5
					spriteToMove.moveImage("right")
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "moveDown":
				while spriteToMove.rect.bottom < i[2]:
					spriteToMove.rect.bottom += 5
					spriteToMove.moveImage("down")
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "moveUp":
				while spriteToMove.rect.top > i[2]:
					spriteToMove.rect.top -=5
					spriteToMove.moveImage("up")
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "moveLeftTogether":
				while spriteToMove.rect.left > i[2]:
					for j in i[3]:
						j.rect.left -= 5
						j.moveImage("left")
					spriteToMove.moveImage("left")
					spriteToMove.rect.left -= 5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "moveRightTogether":
				while spriteToMove.rect.right < i[2]:
					for j in i[3]:
						j.rect.right += 5
						j.moveImage("right")
					spriteToMove.moveImage("right")
					spriteToMove.rect.right += 5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "moveDownTogether":
				while spriteToMove.rect.bottom < i[2]:
					for j in i[3]:
						j.rect.bottom += 5
						j.moveImage("down")
					spriteToMove.moveImage("down")
					spriteToMove.rect.bottom += 5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "moveUpTogether":
				while spriteToMove.rect.top > i[2]:
					for j in i[3]:
						j.rect.top -= 5
						j.moveImage("up")
					spriteToMove.moveImage("up")
					spriteToMove.rect.top -=5
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
					fpsClock.tick(FPS)
			elif action == "turn":
					spriteToMove.moveImage(i[2])
					self.scene.drawBackground()
					self.mainSurface.blit(self.hero.image, self.hero.rect)
					self.scene.drawAll()
					pygame.display.update()
			elif action == "talk":
				talking = Dialogue(i[2])
				talking.runText(self.mainSurface, spriteToMove.rect.y)
			elif action == "question":
				question = Question(i[2],i[3],i[4])
				trigger = question.runQuestion(self.mainSurface, spriteToMove.rect.y)
				self.level.reaction(trigger)
			elif action == "leave":
				self.scene.remove(i[2])
				self.scene.drawBackground()
				self.mainSurface.blit(self.hero.image, self.hero.rect)
				self.scene.drawAll()
				pygame.display.update()
				fpsClock.tick(FPS)
			elif action == "murder":
				if i[2] == 1:
					weapon = pygame.image.load("swordUp.png")
					self.mainSurface.blit(weapon, (self.hero.rect.left, self.hero.rect.top - 50))
					pygame.display.update()
				elif i[2] == 2:
					weapon = pygame.image.load("swordRight.png")
					self.mainSurface.blit(weapon, (self.hero.rect.right, self.hero.rect.top))
					pygame.display.update()
				elif i[2] == 3:
					weapon = pygame.image.load("swordDown.png")
					self.mainSurface.blit(weapon, (self.hero.rect.right, self.hero.rect.bottom))
					pygame.display.update()
				elif i[2] == 4:
					weapon = pygame.image.load("swordLeft.png")
					self.mainSurface.blit(weapon, (self.hero.rect.left - 30, self.hero.rect.bottom - 8))
					pygame.display.update()
				pygame.time.wait(200)

