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
        	if trigger == "startScene":
        		starting = CutScene(self.scenes[0], [(self.sprites["scaredM1"], "moveDownTogether", 370, [self.sprites["scaredW1"]]), (self.hero, "talk", "AHHHHH THE HYDRA HAS BEEN SEEN IN THE NORTH, RUNNN!!!!\
        			You better get out of here. Use the DIRECTIONAL buttons to move far far away from here. Also if you meet new people try to tell about the Hydra with SPACEBAR"),\
        		 (self.sprites["scaredM1"], "moveLeftTogether", 10, [self.sprites["scaredW1"]]), (self.sprites["scaredM1"], "leave", "scaredM1"), (self.sprites["scaredW1"], "leave", "scaredW1")])
        		starting.runScene()
        	elif trigger == "beginning":
        		moveHero = CutScene(self.scenes[3], [(self.hero, "moveRight", 325),(self.hero, "moveDown", 450)])
        		moveHero.runScene()
        		self.scenes[3].addSprite(self.sprites["guy"],"guy")
        		starting = CutScene(self.scenes[3], [(self.sprites["guy"],"moveUp",self.hero.rect.top),\
        			(self.sprites["guy"],"moveRight", self.hero.rect.left), (self.sprites["guy"],"talk"," Out of the way--out of the way, please! I need to hide.\
        		  Grey-eyed Athena have mercy, I must leave before the guards catch up! Let me pass! "), (self.hero, "question", "What do you say", ["Slow down. Tell me what happened", "I don't think so! What did you do?"],\
        		  ["beginning2-1", "beginning2-2"])])
        		starting.runScene()
        	elif trigger == "beginning2-1":
        		react = CutScene(self.scenes[3], [(self.sprites["guy"], "talk", "Young man: They won’t listen to you, xenoi (foreigner), so I will tell you. I was starving so I stole some food from a slave.\
        		 They saw me, and I should have been quicker, so...I must hide until the merchant’s temper blows over.  It is in our custom for soldiers-in-training \
        		 to steal so they can eat, xenoi. The elder commanders say it makes us more wily. You must understand.")])
        		react.runScene()
        		decisionAfter = CutScene(self.scenes[3], [(self.hero, "question", "Decision", ["Well as Spartan tradition says - DIE! (kill the thief)", \
        			"Custom? No you will face justice. (restrain the thief)", "Fine, I have not seen you here (let the thief pass)"], \
        			["beginning3-1","beginning3-2","beginning3-3"])])
        		decisionAfter.runScene()
        	elif trigger == "beginning2-2":
        		react  = CutScene(self.scenes[3], [(self.sprites["guy"], "talk", "Young man: Please, xenoi (foreigner), I’ll talk! I was starving so I stole some food from a merchant. They saw me, and I should have been quicker,\
        		 so...I must hide until the merchant’s temper blows over. It is in our custom for soldiers-in-training to steal so they can eat, xenoi. \
        		 The elder commanders say it makes us more wily. You must understand.")])
        		react.runScene()
        		decisionAfter = CutScene(self.scenes[3], [(self.hero, "question", "Decision", ["Well as Spartan tradition says - DIE! (kill the thief)", \
        			"Custom? No you will face justice. (restrain the thief)", "Fine, I have not seen you here (let the thief pass)"], \
        			["beginning3-1","beginning3-2","beginning3-3"])])
        		decisionAfter.runScene()
        	elif trigger == "beginning3-1":
        		starting = CutScene(self.scenes[3], [(self.sprites["guy"],"murder", 4), (self.sprites["guy"],"talk"," No please! Gyaaa----"), (self.hero, "leave", "guy")])
        		starting.runScene()
        		#self.scenes[0].addEnemy(self.sprites["soldier1"], "soldier1")
        		#self.scenes[0].addSprite(self.sprites["soldier2"], "soldier2")
        	elif trigger == "beginning3-2":
        		self.scenes[3].addSprite(self.sprites["soldier1"], "soldier1")
        		self.scenes[3].addSprite(self.sprites["soldier2"], "soldier2")
        		starting = CutScene(self.scenes[3], [(self.sprites["soldier1"], "moveUpTogether", self.sprites["guy"].rect.y - 25, [self.sprites["soldier2"]]),\
        		 (self.sprites["soldier1"], "moveRightTogether", self.sprites["guy"].rect.x + 10, [self.sprites["soldier2"]]),\
        		 (self.sprites["guy"], "talk", "Oh no!"), (self.sprites["guy"], "talk", "Boy you have failed, now come back to Sparta to face failure,\
        			 xenoi, let go of this boy and stay out of our affairs"), (self.sprites["soldier1"], "moveLeftTogether", 0, [self.sprites["soldier2"], self.sprites["guy"]]), \
        			 (self.sprites["guy"], "leave", "guy"), (self.sprites["soldier1"], "leave", "soldier1"), (self.sprites["soldier2"], "leave", "soldier2")])
        		starting.runScene()
        	elif trigger == "beginning3-3":
        		starting = CutScene(self.scenes[3], [(self.sprites["guy"],"moveDown",400), (self.sprites["guy"],"moveRight", 600), \
        		 (self.sprites["guy"], "leave", "guy")])
        		starting.runScene()
        		self.scenes[3].addSprite(self.sprites["soldier1"], "soldier1")
        		self.scenes[3].addSprite(self.sprites["soldier2"], "soldier2")
        		nextCutScene = CutScene(self.scenes[3], [(self.sprites["soldier1"], "moveUpTogether",\
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


	#scene one - eight buildings
	building1 = Building(210,50, (0,0))
	building2 = Building(150, 100, (0,50))
	building3 = Building(100, 140,(0,150))
	building4 = Building(155, 50, (0,545))
	building5 = Building(155,50,(445,545))
	building6 = Building(150,190,(445,0))
	building7 = Building(50, 50, (547,260))
	building8 = Building(50, 50, (400,90))
	building9 = Building(50,40, (400,0))

        #scene 9 buildings
	building91 = Building(405,360,(0,100))
	building92 = Building(100, 360, (495,100))

	#scene 10 buildings
	buildingS1 = Building(100, 130, (0,70))
	buildingS2 = Building(100,200,(150,0))
	buildingS3 = Building(205,80,(350,0))
	buildingS4 = Building(250,230,(0,255))
	buildingS5 = Building(105,120,(360,130))
	buildingS6 = Building(105,40,(360,315))
	buildingS7 = Building(85,80,(480,470))
	buildingS8 = Building(65,105,(530,250))
        #people
	first = Hero(50, 50, (300,300))
	first.setSurface(DISPLAYSURF)

	second = Person(50, 50, (0,400))
	soldier1 = Person(50, 50, (0,400))
	soldier2 = Person(50, 50, (0,470))
	third = Enemy((400,200), 5)


	'''
	Important NPC's
	'''
	# The starting NPC's
	scaredW1 = Person(30, 30, (280,0))
	scaredM1 = Person(30, 30, (320,0))
	allSprites["scaredW1"] = scaredW1
	allSprites["scaredM1"] = scaredM1
	scene1People = {}
	scene1People["scaredW1"] = scaredW1
	scene1People["scaredM1"] = scaredM1

	Guide = Person(40, 40, (300,0))
	allSprites["Guide"] = Guide
	'''
	Useless NPC's just giving information about the city, they have five different responses based on you likability
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

        #stuff for scene 9
	scene9People = {}
	scene9People['building91'] = building91
	scene9People['building92'] = building92
	
        #stuff for scene 10
	scene10People = {}
	scene10People['spartanW1'] = spartanW1
	scene10People['spartanM1'] = spartanM1
	scene10People['buildingS1'] = buildingS1
	scene10People['buildingS2'] = buildingS2
	scene10People['buildingS3'] = buildingS3
	scene10People['buildingS4'] = buildingS4
	scene10People['buildingS5'] = buildingS5
	scene10People['buildingS6'] = buildingS6
	scene10People['buildingS7'] = buildingS7
	scene10People['buildingS8'] = buildingS8

	# Athens People
	athensW1 = Person(30, 30, (250, 250))
	athensW1.addDialogue(Dialogue("The blessed Athena believes justice should be settled by the people"))
	athensW1.addDialogue(Dialogue("You are a lawless monster, how dare you tarnish this city with your presence"))
	athensW1.addDialogue(Dialogue("You are truly the suymbol of justics, Athena blesses you"))
	allSprites["athensW1"] = athensW1

	athensM1 = Person(30, 30, (300, 400))
	athensM1.addDialogue(Dialogue("Killing people may satisfy one's vengeance but it does not cleanse the soul"))
	athensM1.addDialogue(Dialogue("Your anger consumes you. You must learn to control yourself before you fight the darkness"))
	athensM1.addDialogue(Dialogue("Your reputation precedes you, I believe you are the true hero of Athens. Do not lose sight of justice"))
	allSprites["athensM1"] = athensM1

	scene2People = {}
	scene2People["athensW1"] = athensW1
	scene2People["athensM1"] = athensM1

	# Delphi People
	delphiW1 = Person(30, 30,(175, 445))
	delphiW1.addDialogue(Dialogue("There is a monster out there in the north, I wonder who can stop him"))
	delphiW1.addDialogue(Dialogue("I know you may be strong but I think you aren't fit to be a hero. Delphi will never vote for you"))
	delphiW1.addDialogue(Dialogue("Hurry save us hero"))
	allSprites["dephiW1"] = delphiW1

	delphiM1 = Person(30, 30,(215, 135))
	delphiM1.addDialogue(Dialogue("Many have left due to the attacks of the monsters, the cities are trying to determine who they should send. \
		Perhaps it would be ideal if all cities liked a single person but they are so divided"))
	delphiM1.addDialogue(Dialogue("I don't know what to say about Sparta and Athens but I know for sure that Delphi will never choose you as their hero with all your blasphehemy."))
	delphiM1.addDialogue(Dialogue("I hope you were able to get Sparta and Athens to choose you, because the city of Delphi adores you and your holy blade"))
	allSprites["dephiM1"] = delphiM1

	scene11People = {}
	scene11People["delphiW1"] = delphiW1
	scene11People["delphiM1"] = delphiM1
	scene11People["Guide"] = Guide



	# Add buildings for all the cities
	building = Building(80,80,(0,520))

	second.addDialogue(Dialogue("Will you help me?"))
	second.addDialogue(Question("Will you help?", ["Help", "Do not Help"], ["guyThanks", "guyHates"]), True)
	allSprites["guy"] = second
	allSprites["enemy1"] = third
	allSprites["Hero"] = first
	allSprites["soldier1"] = soldier1
	allSprites["soldier2"] = soldier2


	people.add(third)
	people2["guy"] = second
	people2["building1"] = building1
	people2["building2"] = building2
	people2["building3"] = building3
	people2["building4"] = building4
	people2["building5"] = building5
	people2["building6"] = building6
	people2["building7"] = building7
	people2["building8"] = building8
	people2["building9"] = building9

	"""																		
	scene1 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('midpoint.png').convert(), transition_points = {1:[250,324,0,0], 2:[0,0,350,400], 3:[290,350,550,600], 4:[500,600,325,399]}, entranceTrigger = "beginning")
	scene2 = Scene(DISPLAYSURF, scene2People, first, background = pygame.image.load('athens_city.png').convert(), transition_points = {2:[0,100,325,399], 3:[325,399,500,600], 4:[500,600,250,324]})
	scene3 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('fran_copy_paste.png').convert(), transition_points = {2:[0,100,250,324], 3:[325,399,500,600]})
	scene4 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('leftLroad.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,250,324]})
	scene5 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,325,399], 4:[500,600,250,324]})
	scene6 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('T-road.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,250,324], 4:[500,600,325,399]})
	scene7 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('horizontalroad.png').convert(), transition_points = {1:[325,399,0,100], 2:[0,100,325,399], 4:[500,600,250,324]})
	scene8 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[325,399,0,100], 4:[500,600,325,399]})
	scene9 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('sparta_helotfarm.png').convert(), transition_points = {3:[325,399,500,600], 4:[500,600,325,399]})
	scene10= Scene(DISPLAYSURF, scene10People, first, background = pygame.image.load('sparta_city.png').convert(), transition_points = {2:[0,100,325,399], 3:[325,399,500,600], 4:[500,600,250,324]})
	scene11= Scene(DISPLAYSURF, scene11People, first, background = pygame.image.load('delphi_city.png').convert(), transition_points = {1:[325,399,0,100], 3:[250,324,500,600]})
	scene12= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('finalmonster_room_withopening.png').convert(), transition_points = {3:[325,399,500,600]})
	"""

	#hero sprite is 25 pixels wide, 40 tall											
	scene1 = Scene(DISPLAYSURF, scene1People, first, background = pygame.image.load('midpoint.png').convert(), transition_points = {1:[250,350,0,0], 2:[0,0,365,465], 3:[250,350,560,600], 4:[575,600,365,465]}, entranceTrigger = "startScene")
	scene2 = Scene(DISPLAYSURF, {}, first, background = pygame.image.load('fran_athens_city.png').convert(), transition_points = {2:[0,0,365,465], 3:[250,350,560,600], 4:[575,600,365,465]})
	scene3 = Scene(DISPLAYSURF, {}, first, background = pygame.image.load('rightbottomL.png').convert(), transition_points = {2:[0,0,365,465], 3:[250,350,560,600]})
	scene4 = Scene(DISPLAYSURF, {}, first, background = pygame.image.load('leftLroad.png').convert(), transition_points = {1:[250,350,0,0], 2:[0,0,365,465]}, entranceTrigger = "beginning")
	scene5 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[250,350,0,0], 4:[575,600,365,465]})
	#scene6 doesn't exist anymore, but left it there so we don't have to rename everything
	scene6 = Scene(DISPLAYSURF, people2, first)
	scene7 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('leftLroad.png').convert(), transition_points = {1:[250,350,0,0], 2:[0,0,365,465]})
	scene8 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[250,350,0,0], 4:[575,600,365,465]})
	scene9 = Scene(DISPLAYSURF, scene9People, first, background = pygame.image.load('fran_sparta_helotfarm.png').convert(), transition_points = {3:[250,350,560,600], 4:[575,600,487,584]})
	scene10= Scene(DISPLAYSURF, scene10People, first, background = pygame.image.load('fran_sparta_city.png').convert(), transition_points = {2:[0,0,487,584], 3:[250,350,560,600], 4:[575,600,365,465]})
	scene11= Scene(DISPLAYSURF, scene11People, first, background = pygame.image.load('fran_delphi_city.png').convert(), transition_points = {1:[250,350,0,0], 3:[250,350,560,600]})
	scene12= Scene(DISPLAYSURF, people2, first, background = pygame.image.load('finalmonster_room_withopening.png').convert(), transition_points = {3:[250,350,560,600]})

	scenes_list = [scene1, scene2, scene3, scene4, scene5, scene6, scene7, scene8, scene9, scene10, scene11, scene12]

	theGame = Game(scenes_list, allSprites, DISPLAYSURF, first)

	current_scene = scenes_list[0]
	current_scene_num = 1
	current_hero_coords = (300,400)

	while True:
		#print(current_scene_num)
		state_of_current_scene, last_hero_coords = current_scene.run(current_hero_coords)
		if state_of_current_scene > 0:
			new_scene_num, current_hero_coords = getNextScene(current_scene_num, state_of_current_scene, last_hero_coords)
			current_scene_num = new_scene_num
			current_scene = scenes_list[new_scene_num-1]


if __name__ == "__main__":
        main()
