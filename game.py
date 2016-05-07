import pygame, sys
from Person import *
from Hero import *
from Building import *
from Enemy import *
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

class Game:
	def __init__(self, scenes):
		self.scenes = scenes
		for i in self.scenes:
			i.identifyGame(self)
	def modifyScene(self, sceneNumber, modifyCommand):
		scene = self.scenes[sceneNumber]
		scene.remove(modifyCommand)


# The main game loop
def main():

	# Setup stuff such as getting the surface and starting the engine
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((600, 600))
	pygame.display.set_caption('Hero of Greece') # Title
	DISPLAYSURF.fill(WHITE)
	people = pygame.sprite.Group()
	people2 = []

	first = Hero(50, 50, (0,0))
	first.setSurface(DISPLAYSURF)
	second = Person(50, 50, (300,300))
	third = Enemy((400,200), 5)

	building = Building(80,80,(0,520))
	second.dialogueChoice(["Will you help me?"])
	second.dialogueChoice(["Help", "Do not Help"])
	second.dialogueChoice(["Thanks man", "You suck"])
	second.setTrigger((1,0),(1,0))

	people.add(third)
	#people.append(third)
	people2.append(second)
	people2.append(building)
	talk = False
	img = pygame.image.load('background.png').convert()
	#scene1  = Scene(DISPLAYSURF, people2, first)
	#scene2 = Scene(DISPLAYSURF, people2, first, people)
	{1:[250,350,0,50], 2:[0,50,250,350], 3:[250,350,550,600], 4:[550,600,250,350]}
	scene1 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('midpoint.png').convert(), transition_points = {1:[250,350,0,50], 2:[0,50,250,350], 3:[250,350,550,600], 4:[550,600,250,350]})
	scene2 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('athens_for_now.png').convert(), transition_points = {2:[0,50,250,350], 3:[250,350,550,600], 4:[550,600,250,350]})
	scene3 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('fran_copy_paste.png').convert(), transition_points = {2:[0,50,250,350], 3:[250,350,550,600]})
	scene4 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('leftLroad.png').convert(), transition_points = {1:[250,350,0,50], 2:[0,50,250,350]})
	scene5 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[250,350,0,50], 2:[0,50,250,350], 4:[550,600,250,350]})
	scene6 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('T-road.png').convert(), transition_points = {1:[250,350,0,50], 2:[0,50,250,350], 4:[550,600,250,350]})
	scene7 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('horizontalroad.png').convert(), transition_points = {1:[250,350,0,50], 2:[0,50,250,350], 4:[550,600,250,350]})
	scene8 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[250,350,0,50], 4:[550,600,250,350]})
	scene9 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('sparta_helotfarm.png').convert(), transition_points = {3:[250,350,550,600], 4:[550,600,250,350]})
	scene10= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('sparta_for_now.png').convert(), transition_points = {2:[0,50,250,350], 3:[250,350,550,600], 4:[550,600,250,350]})
	scene11= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('delphi_for_now.png').convert(), transition_points = {1:[250,350,0,50], 3:[250,350,550,600]})
	scene12= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('finalmonster_room_withopening.png').convert(), transition_points = {3:[250,350,550,600]})

	scenes_list = [scene1, scene2, scene3, scene4, scene5, scene6, scene7, scene8, scene9, scene10, scene11, scene12]

	theGame = Game(scenes_list)

	current_scene = scenes_list[0]
	current_scene_num = 1
	while True:
		print(current_scene_num)
		state_of_current_scene = current_scene.run()
		if state_of_current_scene > 0:
			new_scene_num = getNextScene(current_scene_num, state_of_current_scene)
			current_scene_num = new_scene_num
			current_scene = scenes_list[new_scene_num-1]
		# nextScene = scene1.run()
		# if nextScene == -1:
		# 	scene2.remove(0)
		# 	nextScene = scene1.run()
		# if nextScene == 1:
		# 	scene2.run()


if __name__ == "__main__":
	main()