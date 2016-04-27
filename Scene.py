# Mandatory imports for this game
import pygame
from Person import *
from Building import *

# Color values
WHITE = (255, 255, 255)

'''
	The scene is the second highest (as of now highest) clas of the game. In this class, the hero is dropped in 
	and the needed sprites around the hero are initialized. The hero would be in this scene and interact with sprites
	that are within the same scene. When we leave a scene, we cross the entrance point and then we should return out and move
	into the new scene.
'''

class Scene:

	'''
	Transition positions such that if we enter by surpassing the Y or X values, then we must move on to a different scene into 
	the level
	''' 
	entrancePointsX = []
	entrancePointsY = []

	# Scenes are initialized with the main pygame surface, sprites in the scene and a background drop for the room
	def __init__(self, mainSurface, spriteGroup, hero, background = None):
		self.spriteGroup = spriteGroup
		self.hero = hero
		self.background = background
		self.mainSurface = mainSurface

	# initialize the background and resize according to window size
	def drawBackground(self):
		if self.background:
			bg = pygame.transform.scale(self.background, (self.mainSurface.get_width(), self.mainSurface.get_height()))
			self.mainSurface.blit(bg, (0,0))
		else:
			self.mainSurface.fill(WHITE)

	# set the entry points for this scene
	def setEntryPoint(point):
		entrancePoints.append(point)

	# This is the function that runs the current scene
	def run(self):
		self.hero.setPosition((0,0))
		#talk = False

		while True:
			self.drawBackground()
			self.mainSurface.blit(self.hero.image, self.hero.rect)

			talk,talkingTo = self.checkMovement()
			
			self.spriteGroup.update()
			self.spriteGroup.draw(self.mainSurface)

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYUP:
					if event.key == K_SPACE and talk:
						talkingTo.getTextBox(self.mainSurface)

			pygame.display.update()

	# This is just a function to control movement of the hero in the scene
	
	def checkMovement(self):
		keys = pygame.key.get_pressed()
		talkingTo = None
		talk = False
		
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_UP] :
			self.hero.rect.y -= 5
			talk = False
			if self.wallCollide():
				self.hero.rect.y += 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.y += 5
		elif keys[pygame.K_DOWN]:
			self.hero.rect.y += 5
			talk = False
			if self.wallCollide():
				self.hero.rect.y -= 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.y -= 5
		elif keys[pygame.K_RIGHT]:
			self.hero.rect.x += 5
			talk = False
			if self.wallCollide():
				self.hero.rect.x -= 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.x -= 5
		elif keys[pygame.K_LEFT]:
			self.hero.rect.x -= 5
			talk = False
			if self.wallCollide():
				self.hero.rect.x+= 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.x += 5

		return talk, talkingTo
		

	def talkCollisions(self):
		for sprite in self.spriteGroup:
			if pygame.sprite.collide_rect(self.hero, sprite):
				return sprite
		return None

	def wallCollide(self):
		return  self.hero.rect.left < 0 or self.hero.rect.right > self.mainSurface.get_width() or self.hero.rect.top < 0 or self.hero.rect.bottom > self.mainSurface.get_height()

