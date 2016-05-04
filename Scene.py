# Mandatory imports for this game
import pygame
from Person import *
from Building import *
from Enemy import *
# Color values
WHITE = (255, 255, 255)
FPS = 60
fpsClock = pygame.time.Clock()

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
	talkingTo = None
	level = None

	# Scenes are initialized with the main pygame surface, sprites in the scene and a background drop for the room
	def __init__(self, mainSurface, spriteGroup ,hero, enemyList = None, background = None):
		self.spriteGroup = spriteGroup[:]
		self.hero = hero
		self.background = background
		self.mainSurface = mainSurface
		self.enemies = enemyList

	def identifyGame(self,l):
		self.level = l
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
		self.hero.setPosition((300,0))
		#talk = False
		talk = False

		while True:
			self.drawBackground()
			self.mainSurface.blit(self.hero.image, self.hero.rect)
			talk, change = self.checkMovement(talk)
			if change > 0:
				return change
			#self.spriteGroup.update()
			#self.spriteGroup.draw(self.mainSurface)
			self.drawAll()
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYUP:
					if event.key == K_SPACE and talk and self.talkingTo:
						reaction = self.talkingTo.getTextBox(self.mainSurface)
						self.getReaction(reaction)
						#self.talkingTo = None
					elif event.key == K_LSHIFT:
						weapon = self.hero.getAction()
						if weapon:
							self.hitCollision(weapon)

			pygame.display.update()
			fpsClock.tick(FPS)

	def getReaction(self, reaction):
		if reaction:
			if isinstance(reaction, tuple):
				self.hero.increaseAthena(reaction[0])
				self.level.modifyScene(1,0)

			

	# This is just a function to control movement of the hero in the scene
	def checkMovement(self, t):
		keys = pygame.key.get_pressed()
		talkingTo = None
		change = 0
		talk = t

		
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_UP] :
			self.hero.rect.y -= 5
			self.hero.direction = 1
			talk = False
			if self.wallCollide() or self.walkCollision():
				self.hero.rect.y += 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.y += 5
				self.talkingTo = talkingTo

		elif keys[pygame.K_DOWN]:
			self.hero.rect.y += 5
			self.hero.direction = 3
			talk = False
			if self.wallCollide() or self.walkCollision():
				self.hero.rect.y -= 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.y -= 5
				self.talkingTo = talkingTo

		elif keys[pygame.K_RIGHT]:
			self.hero.rect.x += 5
			self.hero.direction = 2
			talk = False
			if self.wallCollide() or self.walkCollision():
				self.hero.rect.x -= 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.x -= 5
				self.talkingTo = talkingTo

		elif keys[pygame.K_LEFT]:
			self.hero.rect.x -= 5
			self.hero.direction = 4
			talk = False
			if self.wallCollide() or self.walkCollision():
				self.hero.rect.x += 5
			talkingTo = self.talkCollisions()
			if talkingTo:
				talk = True
				self.hero.rect.x += 5
				self.talkingTo = talkingTo

		#print(self.hero.rect.bottom, self.hero.rect.x)
		change = self.transistion()

		return talk, change

	def drawAll(self):
		for i in self.spriteGroup:
			i.update()
			self.mainSurface.blit(i.image,i.rect)
		if self.enemies:
			self.enemies.draw(self.mainSurface)

	def transistion(self):
		if self.hero.rect.bottom > 550 and self.hero.rect.x > 290 and self.hero.rect.x < 310:
			print("Transition Occurs")
			return 1
		return 0

	def hitCollision(self, weapon):
		if self.enemies:
			for enemy in self.enemies:
				if(pygame.sprite.collide_rect(weapon, enemy)):
					dead = enemy.changeHealth(2)
					print(enemy.health)
					if dead:
						enemy.kill()

	def walkCollision(self):
		if self.enemies:
			for enemy in self.enemies:
				if pygame.sprite.collide_rect(self.hero, enemy):
					return True
		return False

	def talkCollisions(self):
		for sprite in self.spriteGroup:
			if pygame.sprite.collide_rect(self.hero, sprite):
				return sprite
		return None

	def wallCollide(self):
		return  self.hero.rect.left < 0 or self.hero.rect.right > self.mainSurface.get_width() or self.hero.rect.top < 0 or self.hero.rect.bottom > self.mainSurface.get_height()

	def remove(self,sprite):
		del self.spriteGroup[sprite]
