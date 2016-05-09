import pygame, sys
from Person import *
from Hero import *
from Building import *
from Enemy import *
from Scene import *
from pygame.locals import *
from Dialogue import *
from Question import *


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
        def __init__(self, scenes, people, surface):
                self.scenes = scenes
                for i in self.scenes:
                        i.identifyGame(self)
                self.sprites = people
                self.surface = surface
        def reaction(self, trigger):
        	if trigger == "guyThanks":
        		self.sprites["guy"].addDialogue(Dialogue("Thanks"))
        		self.sprites["guy"].goToLastDialogue()
        		self.sprites["guy"].getTextBox(self.surface)
        	elif trigger == "guyHates":
        		react = Dialogue("You know that you suck")
        		react.runText(self.surface)


# The main game loop
def main():

	# Setup stuff such as getting the surface and starting the engine
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((600, 600))
	pygame.display.set_caption('Hero of Greece') # Title
	DISPLAYSURF.fill(WHITE)
	people = pygame.sprite.Group()
	people2 = {}
	allSprites  = {}


	first = Hero(50, 50, (0,0))
	first.setSurface(DISPLAYSURF)
	second = Person(50, 50, (300,300))
	third = Enemy((400,200), 5)

	building = Building(80,80,(0,520))
	second.addDialogue(Dialogue("Will you help me?"))
	second.addDialogue(Question("Will you help", ["Help", "Do not Help"], ["guyThanks", "guyHates"]), True)
	#second.dialogueChoice(["Thanks man", "You suck"])
	#second.setTrigger((1,0),(1,0))
	allSprites["guy"] = second
	allSprites["enemy1"] = third


	people.add(third)
	#people.append(third)
	people2["guy"] = second
	people2["building"] = building
	talk = False
	img = pygame.image.load('background.png').convert()
	#scene1  = Scene(DISPLAYSURF, people2, first)
	#scene2 = Scene(DISPLAYSURF, people2, first, people)																			
	scene1 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('midpoint.png').convert(), transition_points = {1:[250,324,0,100], 2:[0,100,250,324], 3:[325,399,500,600], 4:[500,600,325,399]})
	scene2 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('athens_city.png').convert(), transition_points = {2:[0,100,325,399], 3:[325,399,500,600], 4:[500,600,250,324]})
	scene3 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('fran_copy_paste.png').convert(), transition_points = {2:[0,100,250,324], 3:[325,399,500,600]})
	scene4 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('leftLroad.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,250,324]})
	scene5 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,325,399], 4:[500,600,250,324]})
	scene6 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('T-road.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,250,324], 4:[500,600,325,399]})
	scene7 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('horizontalroad.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,325,399], 4:[500,600,250,324]})
	scene8 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[325,399,0,100], 4:[500,600,325,399]})
	scene9 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('sparta_helotfarm.png').convert(), transition_points = {3:[325,399,500,600], 4:[500,600,325,399]})
	scene10= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('sparta_city.png').convert(), transition_points = {2:[0,100,325,399], 3:[325,399,500,600], 4:[500,600,250,324]})
	scene11= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('delphi_city.png').convert(), transition_points = {1:[325,399,0,100], 3:[250,324,500,600]})
	scene12= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('finalmonster_room_withopening.png').convert(), transition_points = {3:[325,399,500,600]})

	scenes_list = [scene1, scene2, scene3, scene4, scene5, scene6, scene7, scene8, scene9, scene10, scene11, scene12]

	theGame = Game(scenes_list, allSprites, DISPLAYSURF)

	current_scene = scenes_list[0]
	current_scene_num = 1
	while True:
		print(current_scene_num)
		state_of_current_scene = current_scene.run()
		if state_of_current_scene > 0:
			new_scene_num = getNextScene(current_scene_num, state_of_current_scene)
			current_scene_num = new_scene_num
			current_scene = scenes_list[new_scene_num-1]


if __name__ == "__main__":
        main()
