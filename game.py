import pygame, sys
from Person import *
from pygame.locals import *

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
	first = Person(50, 50, (0,0))
	second = Person(50, 50, (300,300))
	second.dialogueChoice(["Will you help me?"])
	second.dialogueChoice(["Help", "Do not Help"])
	second.dialogueChoice(["Thanks man", "You suck"])
	people.add(first, second)

	# Importing cat images just a test snippet
	catImg = pygame.image.load('cat.png')
	cat2 = pygame.image.load('cat.png')
	cx = 100
	cy = 100
	catx = 10
	caty = 200

	talk = False

	while True:
		DISPLAYSURF.fill(WHITE)
		DISPLAYSURF.blit(catImg, (catx,caty))
		#This for loop checks for any events that occur

		# This is for the movement of our sprite
		keys = pygame.key.get_pressed()
	

		if keys[pygame.K_UP] :
			first.rect.y -= 5
			talk = False
			if pygame.sprite.collide_rect(first, second):
				talk = True
				first.rect.y += 5
		elif keys[pygame.K_DOWN]:
			first.rect.y += 5
			talk = False
			if pygame.sprite.collide_rect(first, second):
				first.rect.y -= 5
				talk = True
		elif keys[pygame.K_RIGHT]:
			first.rect.x += 5
			talk = False
			if pygame.sprite.collide_rect(first, second):
				first.rect.x -= 5
				talk = True
		elif keys[pygame.K_LEFT]:
			first.rect.x -= 5
			talk = False
			if pygame.sprite.collide_rect(first, second):
				first.rect.x += 5
				talk = True

		people.update()
		people.draw(DISPLAYSURF)

		# Event key look for
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYUP:
				if event.key == K_SPACE and talk:
					second.getTextBox(DISPLAYSURF)

		#Updates after events have been made
		pygame.display.update()
		fpsClock.tick(FPS)



if __name__ == "__main__":
	main()