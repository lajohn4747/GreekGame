import pygame, sys
from Person import *
from Building import *
from Scene import *
from pygame.locals import *


# Lots of comments so that it easier to understand, although comments in python does affect overall performance but we
# just need this to work 


# Colors to use in this module
BLACK = (0,0,0)	
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Frame rate of this game
FPS = 60
fpsClock = pygame.time.Clock()


# The main game loop
def main():

	# Setup stuff such as getting the surface and starting the engine
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((600, 600))
	pygame.display.set_caption('Hero of Greece') # Title
	DISPLAYSURF.fill(WHITE)
	people = pygame.sprite.Group()

	# Create a scene objects
	targetTalk = None

	first = Person(50, 50, (0,0))
	second = Person(50, 50, (300,300))
	building = Building(80,80,(0,520))
	second.dialogueChoice(["Will you help me?"])
	second.dialogueChoice(["Help", "Do not Help"])
	second.dialogueChoice(["Thanks man", "You suck"])

	people.add(first, second, building)
	people2 = pygame.sprite.Group()
	people2.add(second, building)
	talk = False
	img = pygame.image.load('background.png')
	scene1  = Scene(DISPLAYSURF,people2,first)

	# Importing cat images just a test snippet
	"""
	catImg = pygame.image.load('cat.png')
	cat2 = pygame.image.load('cat.png')
	cx = 100
	cy = 100
	catx = 10
	caty = 200
	"""

	scene1.run()

	'''	
	while True:
	'''

def collisions(hero, allSprites):
	for sprite in allSprites:
		if hero != sprite:
			if pygame.sprite.collide_rect(hero, sprite):
				return sprite

	return None

def wallCollide(hero, surface):
	return  hero.rect.left < 0 or hero.rect.right > surface.get_width() or hero.rect.top < 0 or hero.rect.bottom > surface.get_height()


if __name__ == "__main__":
	main()