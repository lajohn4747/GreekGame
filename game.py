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
        	checkHero = None
        	if trigger == "startScene":
        		starting = CutScene(self.scenes[0], [(self.hero, "turn", "up"), (self.sprites["scaredM1"], "moveDownTogether", 370, [self.sprites["scaredW1"]]), (self.hero, "talk", "AHHHHH THE HYDRA HAS BEEN SEEN IN THE NORTH, RUNNN!!!!\
        			You better get out of here. Tell everyone you know with SPACEBAR. Use the DIRECTIONAL buttons to move far far away from here. If you get tired press P, to take a break and look how Greece sees you. So run, hopefully Greece can choose a hero to save us."),\
        		 (self.sprites["scaredM1"], "moveLeftTogether", 10, [self.sprites["scaredW1"]]), (self.sprites["scaredM1"], "leave", "scaredM1"), (self.sprites["scaredW1"], "leave", "scaredW1")])
        		starting.runScene()


        	elif trigger == "poorFarmer":
        		starting = CutScene(self.scenes[8], [(self.sprites["poorFarmer"],"moveDown",self.hero.rect.bottom),(self.sprites["poorFarmer"],"moveRight", self.hero.rect.left), (self.hero, "turn","left"), \
        			(self.sprites["poorFarmer"],"talk","You’re--you’re not a Spartan, right? You don’t look like you’re from around here! [The man seems very out of breath,\
        			 and unusually pale.] It’s autumn--it is the time for the young Spartan soldiers of the Krypteia to slaughter us like cattle! Please, I need help. We are slaves, and have no ability to resist. \
        			 The Spartans see them as their finest trainees, but they’re truly no better than thugs, happily terrorizing us Helots whenever they wish. They even declare war on us every year so they may justify killing all of the slaves they want!\
        			  The Krypteia even prefer killing the strongest and best of us--I have three sons on the cusp of manhood, I cannot let their blood stain Spartan hands!"), (self.hero, "question", "What do you say?",\
        			   ["I’m sorry, ask someone else. Hide in your home for now", "What a horrid practice! What can I do? "],["poorFarmer2-1", "poorFarmer2-2"])])
        		starting.runScene()
        	elif trigger == "poorFarmer2-1":
        		cut = CutScene(self.scenes[8], [(self.sprites["poorFarmer"], "talk", "Home?! That will be the first place they look! I should have known better than to ask a foreigner for help."),\
        			(self.sprites["poorFarmer"], "moveLeft", 20), (self.sprites["poorFarmer"], "leave", "poorFarmer")])
        		cut.runScene()
        		checkHero = self.hero.increasePoints("sparta", 1)
        		self.updateDialogue(checkHero)
        	elif trigger == "poorFarmer2-2":
        		cut = CutScene(self.scenes[8], [(self.sprites["poorFarmer"], "talk", "My only option is to move my family towards Menelaos--the district is safe, and the Krypteia will not follow us there. But the Spartans are everywhere, \
        			and I do not know how I can convince them that we are from Menelaos!")])
        		cut.runScene()
        		self.scenes[8].addSprite(self.sprites["soldier1"], "soldier1")
        		self.scenes[8].addSprite(self.sprites["soldier2"], "soldier2")
        		self.sprites["soldier1"].setPosition((0,490))
        		self.sprites["soldier2"].setPosition((0,525))
        		cut2 = CutScene(self.scenes[8], [(self.sprites["soldier1"], "moveRightTogether", self.hero.rect.left - 35, [self.sprites["soldier2"]]), (self.hero, "talk", "Soldier: It is dangerous for you to be here, foreigner. We expect much bloodshed\
        		 in this district once we are done with the slaves. We may escort you out, if you wish. This may deem it barbaric and rightfully so, but it has been our tradition for many generations. A soldier is not a true\
        		  soldier until he has killed, and our first targets have always been the Helots. It is the only way to keep them from attempting to revolt and destroy our city."), (self.hero, "talk", "Farmer: Please help me stranger"),\
        		(self.hero, "question", "What do you say", ["I do not care for your practice Spartans", "I see, I know Athenians wouldn't approve but these are your laws", "You are mistaken, this man is from Menelaos"], ["farmerFight", "poorFarmerDeath", "poorFarmerSaved"]) ])
        		cut2.runScene()
        	elif trigger == "poorFarmerDeath":
        		cut = CutScene(self.scenes[8], [(self.sprites["poorFarmer"], "talk", "Farmer: NOOOOO!!! Please help!!...."), (self.sprites["soldier1"], "moveLeftTogether", 15, [self.sprites["soldier2"], self.sprites["poorFarmer"]]),\
        			(self.sprites["soldier1"], "leave", "soldier1"), (self.sprites["soldier2"], "leave", "soldier2"), (self.sprites["poorFarmer"], "leave", "poorFarmer")])
        		cut.runScene()
        		checkHero = self.hero.increasePoints("sparta", 1)
        		self.updateDialogue(checkHero)
        	elif trigger == "poorFarmerSaved":
        		cut = CutScene(self.scenes[8], [(self.sprites["soldier1"], "talk", "Soldier1: He does not look like he is from Menelaos, but we do not have time to squabble with news of the Hydra. Slaves are riled up since the arrival of the beast. Only\
        			 a hero from Sparta can bring peace. Go home strangers if you know what is best."), (self.sprites["soldier2"], "moveLeftTogether", 10, [self.sprites["soldier1"]]),\
        		(self.sprites["soldier1"], "leave", "soldier1"), (self.sprites["soldier2"], "leave", "soldier2")]) 
        		cut2 = CutScene(self.scenes[8], [(self.sprites["poorFarmer"], "talk", "Thank you sir. Such a noble act you have done me. Here is a token of my appreciation. I think I will be safe for a while, I will wait for my family here"),\
        		(self.sprites["poorFarmer"], "moveLeft", 50)])
        		cut.runScene()
        		cut2.runScene()
        		checkHero = self.hero.increasePoints("delphi", 1)
        		self.updateDialogue(checkHero)

        	elif trigger == "NoApprentence":
        		self.sprites["oldManQuest"].addDialogue(Dialogue("I am sorry, my anger has strayed from the gods. I should let the people exact justice upon him. Maybe this is why the Hydra has attacked us"))
        		self.sprites["oldManQuest"].goToLastDialogue()
        		self.sprites["oldManQuest"].getTextBox(self.surface, self.hero.rect.y)
        		checkHero = self.hero.increasePoints("athens", 3)
        		self.updateDialogue(checkHero)
        		checkHero = self.hero.increasePoints("delphi", 2)
        		self.updateDialogue(checkHero)

        	elif trigger == "beginning":
        		moveHero = CutScene(self.scenes[3], [(self.hero, "moveRight", 325),(self.hero, "moveDown", 450)])
        		moveHero.runScene()
        		self.scenes[3].addSprite(self.sprites["guy"],"guy")
        		starting = CutScene(self.scenes[3], [(self.sprites["guy"],"moveUp",self.hero.rect.top),\
        			(self.sprites["guy"],"moveRight", self.hero.rect.left), (self.hero, "turn", "left"), (self.sprites["guy"],"talk"," Out of the way--out of the way, please! I need to hide.\
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
        		checkHero = self.hero.increasePoints("sparta", -2)
        		self.updateDialogue(checkHero)
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
        		checkHero =self.hero.increasePoints("sparta", -1)
        		self.updateDialogue(checkHero)
        		checkHero = self.hero.increasePoints("athens", 2)
        		self.updateDialogue(checkHero)
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
        		checkHero = self.hero.increasePoints("sparta", 2)
        		self.updateDialogue(checkHero)

        def updateDialogue(self, checkHero):
        	if checkHero:
        		if checkHero == "Athens3":
        			athenSprites = self.scenes[1].spriteGroup
        			for a in athenSprites:
        				athenSprites[a].dialogueNumber = 2



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

	#scene 2 buildings
	buildingA1 = Building(255, 100, (0,0))
	buildingA2 = Building(255, 75, (0,130))
	buildingA3 = Building(210, 45, (0,205))
	buildingA4 = Building(200, 75, (0,295))
	buildingA5 = Building(55, 130, (0,465))
	buildingA6 = Building(100, 130, (100,465))
	buildingA7 = Building(100, 45, (345,550))
	buildingA8 = Building(90, 100, (505,450))
	buildingA9 = Building(250, 55, (345,0))
	buildingA10 = Building(50, 300, (545,80))
	buildingA11 = Building(150, 130, (350,100))
	buildingA12 = Building(110, 140, (390,230))
	
        #people
	first = Hero(50, 50, (300,300))
	first.setSurface(DISPLAYSURF)
	second = Person(50, 50, (0,400))
	soldier1 = Person(30, 30, (0,400))
	soldier2 = Person(30, 30, (0,470))
	third = Enemy((400,200), 5, people2)


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
	scene1People["building1"] = building1
	scene1People["building2"] = building2
	scene1People["building3"] = building3
	scene1People["building4"] = building4
	scene1People["building5"] = building5
	scene1People["building6"] = building6
	scene1People["building7"] = building7
	scene1People["building8"] = building8
	scene1People["building9"] = building9

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
	poorFarmer = Person(30, 30, (150, 150))
	poorFarmer.addDialogue(Dialogue("Thank you, maybe you are the Greece needs in order to destroy the Hydra"))
	allSprites['poorFarmer'] = poorFarmer
	scene9People = {}
	scene9People['building91'] = building91
	scene9People['building92'] = building92
	scene9People['poorFarmer'] = poorFarmer
	
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

	#stuff for scene 2
	scene2People = {}
	scene2People['buildingA1'] = buildingA1
	scene2People['buildingA2'] = buildingA2
	scene2People['buildingA3'] = buildingA3
	scene2People['buildingA4'] = buildingA4
	scene2People['buildingA5'] = buildingA5
	scene2People['buildingA6'] = buildingA6
	scene2People['buildingA7'] = buildingA7
	scene2People['buildingA8'] = buildingA8
	scene2People['buildingA9'] = buildingA9
	scene2People['buildingA10'] = buildingA10
	scene2People['buildingA11'] = buildingA11
	scene2People['buildingA12'] = buildingA12

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
	#buildings for scene 2
	scene2People['buildingA1'] = buildingA1
	scene2People['buildingA2'] = buildingA2
	scene2People['buildingA3'] = buildingA3
	scene2People['buildingA4'] = buildingA4
	scene2People['buildingA5'] = buildingA5
	scene2People['buildingA6'] = buildingA6
	scene2People['buildingA7'] = buildingA7
	scene2People['buildingA8'] = buildingA8
	scene2People['buildingA9'] = buildingA9
	scene2People['buildingA10'] = buildingA10
	scene2People['buildingA11'] = buildingA11
	scene2People['buildingA12'] = buildingA12

	# Delphi People
	delphiW1 = Person(30, 30,(175, 445))
	delphiW1.addDialogue(Dialogue("There is a monster out there in the north, I wonder who can stop him"))
	delphiW1.addDialogue(Dialogue("I know you may be strong but I think you aren't fit to be a hero. Delphi will never vote for you"))
	delphiW1.addDialogue(Dialogue("Hurry save us hero"))
	allSprites["dephiW1"] = delphiW1

	oldManQuest = Person(30, 30,(480, 115))
	oldManQuest.addDialogue(Dialogue("I am a great philosopher and I have great deciples but one of them has went rogue and killed my son. Athenian law wants to stop him but I want to make sure he pays"))
	oldManQuest.addDialogue(Question("Will you exact my vengeance", ["Yes", "No"], ["LooseApprentence", "NoApprentence"]), True)
	allSprites["oldManQuest"] = oldManQuest

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
	scene11People["oldManQuest"] = oldManQuest
	#scene 11 buildings
	buildingD1 = Building(205, 85, (0,0))
	buildingD2 = Building(100, 95, (355,0))
	buildingD3 = Building(85, 95, (510,0))
	buildingD4 = Building(240, 75, (0,160))
	buildingD5 = Building(130, 105, (0,235))
	buildingD6 = Building(80, 75, (170,290))
	buildingD7 = Building(85, 200, (360,155))
	buildingD8 = Building(80, 200, (515,150))
	buildingD9 = Building(130, 125, (0,470))
	buildingD10 = Building(80, 125, (170,470))
	buildingD11 = Building(100, 125, (355,470))
	buildingD12 = Building(85, 105, (510,490))
	scene11People["buildingD1"] = buildingD1
	scene11People["buildingD2"] = buildingD2
	scene11People["buildingD3"] = buildingD3
	scene11People["buildingD4"] = buildingD4
	scene11People["buildingD5"] = buildingD5
	scene11People["buildingD6"] = buildingD6
	scene11People["buildingD7"] = buildingD7
	scene11People["buildingD8"] = buildingD8
	scene11People["buildingD9"] = buildingD9
	scene11People["buildingD10"] = buildingD10
	scene11People["buildingD11"] = buildingD11
	scene11People["buildingD12"] = buildingD12

	#Scene 7 enemies
	enemy = Enemy((300,300),2,people2)
	enemies = [enemy]


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
	people2["building1"] = building1
	people2["building2"] = building2
	people2["building3"] = building3
	people2["building4"] = building4
	people2["building5"] = building5
	people2["building6"] = building6
	people2["building7"] = building7
	people2["building8"] = building8
	people2["building9"] = building9


	#hero sprite is 25 pixels wide, 40 tall											
	scene1 = Scene(DISPLAYSURF, scene1People, first, background = pygame.image.load('midpoint.png').convert(), transition_points = {1:[250,350,0,0], 2:[0,0,365,465], 4:[575,600,365,465]}, entranceTrigger = "startScene")
	scene2 = Scene(DISPLAYSURF, scene2People, first, background = pygame.image.load('fran_athens_city.png').convert(), transition_points = {2:[0,0,365,465], 3:[250,350,560,600], 4:[575,600,365,465]})
	scene3 = Scene(DISPLAYSURF, {}, first, background = pygame.image.load('rightbottomL.png').convert(), transition_points = {2:[0,0,365,465], 3:[250,350,560,600]})
	scene4 = Scene(DISPLAYSURF, {}, first, background = pygame.image.load('leftLroad.png').convert(), transition_points = {1:[250,350,0,0], 2:[0,0,365,465]}, entranceTrigger = "beginning")
	scene5 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[250,350,0,0], 4:[575,600,365,465]})
	#scene6 doesn't exist anymore, but left it there so we don't have to rename everything
	scene6 = Scene(DISPLAYSURF, people2, first)
	scene7 = Scene(DISPLAYSURF, people2, first, enemies, background = pygame.image.load('leftLroad.png').convert(), transition_points = {1:[250,350,0,0], 2:[0,0,365,465]})
	scene8 = Scene(DISPLAYSURF, people2, first, background = pygame.image.load('rightLroad.png').convert(), transition_points = {1:[250,350,0,0], 4:[575,600,365,465]})
	scene9 = Scene(DISPLAYSURF, scene9People, first, background = pygame.image.load('fran_sparta_helotfarm.png').convert(), transition_points = {3:[250,350,560,600], 4:[575,600,487,584]}, entranceTrigger = "poorFarmer")
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
