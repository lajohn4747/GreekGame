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
        		starting = CutScene(self.scenes[0], [(self.sprites["guy"],"moveUp",self.hero.rect.top), \
        			(self.sprites["guy"],"moveRight", self.hero.rect.left), (self.sprites["guy"],"talk"," Out of the way--out of the way, please! I need to hide.\
        		  Grey-eyed Athena have mercy, I must leave before the guards catch up! Let me pass! "), (self.hero, "question", "What do you say", ["Slow down. Tell me what happened", "I don't think so! What did you do?"],\
        		  ["beginning2-1", "beginning2-2"])])
        		starting.runScene()
        	elif trigger == "beginning2-1":
        		react = Dialogue("Young man: They won’t listen to you, xenoi (foreigner), so I will tell you. I was starving so I stole some food from a slave.\
        		 They saw me, and I should have been quicker, so...I must hide until the merchant’s temper blows over.  It is in our custom for soldiers-in-training \
        		 to steal so they can eat, xenoi. The elder commanders say it makes us more wily. You must understand.")
        		react.runText(self.surface)
        		decisionAfter = CutScene(self.scenes[0], [(self.hero, "question", "Decision", ["Well as Spartan tradition says - DIE! (kill the thief)", \
        			"Custom? No you will face justice. (restrain the thief)", "Fine, I have not seen you here (let the thief pass)"], \
        			["beginning3-1","beginning3-2","beginning3-3"])])
        		decisionAfter.runScene()
        	elif trigger == "beginning2-2":
        		react  = Dialogue("Young man: Please, xenoi (foreigner), I’ll talk! I was starving so I stole some food from a merchant. They saw me, and I should have been quicker,\
        		 so...I must hide until the merchant’s temper blows over. It is in our custom for soldiers-in-training to steal so they can eat, xenoi. \
        		 The elder commanders say it makes us more wily. You must understand.")
        		react.runText(self.surface)
        		decisionAfter = CutScene(self.scenes[0], [(self.hero, "question", "Decision", ["Well as Spartan tradition says - DIE! (kill the thief)", \
        			"Custom? No you will face justice. (restrain the thief)", "Fine, I have not seen you here (let the thief pass)"], \
        			["beginning3-1","beginning3-2","beginning3-3"])])
        		decisionAfter.runScene()
        	elif trigger == "beginning3-1":
        		starting = CutScene(self.scenes[0], [(self.sprites["guy"],"murder", 4), (self.sprites["guy"],"talk"," No please! Gyaaa----"), (self.hero, "leave", "guy")])
        		starting.runScene()
        		#self.scenes[0].addEnemy(self.sprites["soldier1"], "soldier1")
        		#self.scenes[0].addSprite(self.sprites["soldier2"], "soldier2")
        	elif trigger == "beginning3-2":
        		self.scenes[0].addSprite(self.sprites["soldier1"], "soldier1")
        		self.scenes[0].addSprite(self.sprites["soldier2"], "soldier2")
        		starting = CutScene(self.scenes[0], [(self.sprites["soldier1"], "moveUpTogether", self.sprites["guy"].rect.y - 25, [self.sprites["soldier2"]]),\
        		 (self.sprites["soldier1"], "moveRightTogether", self.sprites["guy"].rect.x + 10, [self.sprites["soldier2"]]),\
        		 (self.sprites["guy"], "talk", "Oh no!"), (self.sprites["guy"], "talk", "Boy you have failed, now come back to Sparta to face failure,\
        			 xenoi, let go of this boy and stay out of our affairs"), (self.sprites["soldier1"], "moveLeftTogether", 0, [self.sprites["soldier2"], self.sprites["guy"]]), \
        			 (self.sprites["guy"], "leave", "guy"), (self.sprites["soldier1"], "leave", "soldier1"), (self.sprites["soldier2"], "leave", "soldier2")])
        		starting.runScene()
        	elif trigger == "beginning3-3":
        		starting = CutScene(self.scenes[0], [(self.sprites["guy"],"moveDown",400), (self.sprites["guy"],"moveRight", 600), \
        		 (self.sprites["guy"], "leave", "guy")])
        		starting.runScene()
        		self.scenes[0].addSprite(self.sprites["soldier1"], "soldier1")
        		self.scenes[0].addSprite(self.sprites["soldier2"], "soldier2")
        		nextCutScene = CutScene(self.scenes[0], [(self.sprites["soldier1"], "moveUpTogether",\
        			self.hero.rect.y - 25, [self.sprites["soldier2"]]), (self.sprites["soldier1"], "moveRightTogether", self.hero.rect.x - 25, [self.sprites["soldier2"]])])
        		nextCutScene.runScene()
        		self.sprites["soldier1"].addDialogue(Dialogue("Hahaha I see the excellent young boy, got away"))
        		self.sprites["soldier2"].addDialogue(Dialogue("Hahaha I know you assisted my boy, and as a Spartan I thank you"))
        		self.sprites["soldier1"].getTextBox(self.surface)

        	elif trigger == "Spartan7":
        		pass
        	elif trigger == "Spartan3":
        		pass
        	elif trigger == "Spartan0":
        		pass
        	elif trigger == "Spartan-3":
        		pass
        	elif trigger == "Spartan-7":
        		pass
        	elif trigger == "Athens7":
        		pass
        	elif trigger == "Athens3":
        		pass
        	elif trigger == "Athens0":
        		pass
        	elif trigger == "Athens-3":
        		pass
        	elif trigger == "Athens-7":
        		pass
        	elif trigger == "Delphi7":
        		pass
        	elif trigger == "Delphi3":
        		pass
        	elif trigger == "Delphi0":
        		pass
        	elif trigger == "Delphi-3":
        		pass
        	elif trigger == "Delphi-7":
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


	second = Person(50, 50, (0,400))
	soldier1 = Person(50, 50, (0,400))
	soldier2 = Person(50, 50, (0,470))
	third = Enemy((400,200), 5)


	'''
	Useless NPC's just giving information abobut the city, they have five different responses based on you likability
	'''
	# Spartan People
	spartanW1 = Person(30, 30, (0, 245))
	spartanW1.addDialogue(Dialogue("Spartans are a people of honor, maybe you should understand that before entering this city"))
	spartanW1.addDialogue(Dialogue("You are a scum without honor, how dare you show your face here"))
	spartanW1.addDialogue(Dialogue("Hello fine warrior, I cannot believe that you are not a native spartan"))
	allSprites["spartanW1"] = spartanW1

	spartanM1 = Person(30, 30, (200, 500))
	spartanM1.addDialogue(Dialogue("Hmmm if only were you a more suitable fighter, Sparta would honor you as a hero."))
	spartanM1.addDialogue(Dialogue("You consider yourself a hero? More a coward than anything."))
	spartanM1.addDialogue(Dialogue("I speak for the rest of Sparta and I say that you are truly a hero!"))
	allSprites["spartanM1"] = spartanM1

	scene10People = {}
	scene10People['spartanW1'] = spartanW1
	scene10People['spartanM1'] = spartanM1


	building = Building(80,80,(0,520))
	second.addDialogue(Dialogue("Will you help me?"))
	second.addDialogue(Question("Will you help?", ["Help", "Do not Help"], ["guyThanks", "guyHates"]), True)
	allSprites["guy"] = second
	allSprites["enemy1"] = third
	allSprites["Hero"] = first
	allSprites["soldier1"] = soldier1
	allSprites["soldier2"] = soldier2


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
	scene10= Scene(DISPLAYSURF, scene10People, first, background = pygame.image.load('sparta_city.png').convert(), transition_points = {2:[0,100,325,399], 3:[325,399,500,600], 4:[500,600,250,324]})
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
