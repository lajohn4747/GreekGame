import pygame, sys
from Person import *
from Hero import *
from Building import *
from Enemy import *
from Scene import *
from pygame.locals import *
from Dialogue import *
from Question import *
from CutScene import *


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
        def __init__(self, scenes, people, surface, hero):
                self.scenes = scenes
                for i in self.scenes:
                        i.identifyGame(self)
                self.sprites = people
                self.surface = surface
                self.hero = hero
        def reaction(self, trigger):
        	if trigger == "guyThanks":
        		self.sprites["guy"].addDialogue(Dialogue("Thanks"))
        		self.sprites["guy"].goToLastDialogue()
        		self.sprites["guy"].getTextBox(self.surface)
        	elif trigger == "guyHates":
        		react = Dialogue("You know that you suck")
        		react.runText(self.surface)
        	elif trigger == "beginning":
        		starting = CutScene(self.scenes[0], [(self.sprites["guy"],"moveUp",self.hero.rect.top), (self.sprites["guy"],"moveLeft", self.hero.rect.right), (self.sprites["guy"],"talk"," Out of the way--out of the way, please! I need to hide.\
        		  Grey-eyed Athena have mercy, I must leave before the guards catch up! Let me pass! "), (self.hero, "question", "What do you say", ["Slow down. Tell me what happened", "I don't think so! What did you do?"],\
        		  ["NiceAthena", "NoChange"])])
        		starting.runScene()
        	elif trigger == "beginning2-1":
        		pass
        	elif trigger == "beginning2-2":
        		pass


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


	# Adding buildings 
	scene1TopLeftBlock = Building(200,200,(0,0))

	first = Hero(50, 50, (300,300))
	first.setSurface(DISPLAYSURF)
	second = Person(50, 50, (550,400))
	third = Enemy((400,200), 5)

	building = Building(80,80,(0,520))
	second.addDialogue(Dialogue("Will you help me?"))
	second.addDialogue(Question("Will you help", ["Help", "Do not Help"], ["guyThanks", "guyHates"]), True)
	allSprites["guy"] = second
	allSprites["enemy1"] = third
	allSprites["Hero"] = first


	people.add(third)
	#people.append(third)
	people2["guy"] = second
	people2["building"] = building
	talk = False
	img = pygame.image.load('background.png').convert()
	#scene1  = Scene(DISPLAYSURF, people2, first)
	#scene2 = Scene(DISPLAYSURF, people2, first, people)																			
	scene1 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('midpoint.png').convert(), transition_points = {1:[250,324,0,0], 2:[0,0,350,400], 3:[290,350,550,600], 4:[500,600,325,399]}, entranceTrigger = "beginning")
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

	theGame = Game(scenes_list, allSprites, DISPLAYSURF, first)

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
