# Mandatory imports for this game
import pygame
from Person import *
from Building import *
from Enemy import *
from CutScene import *
# Color values
BLACK = (0,0,0) 
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Font
basicFont = pygame.font.SysFont(None, 24)
largeFont = pygame.font.SysFont(None, 36)
#images
heartImg = pygame.image.load("heart.png")

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
        
        # Scenes are initialized with the main pygame surface, sprites in the scene and a background drop for the room
        def __init__(self, mainSurface, spriteGroup ,hero, enemyList = None, background = None, transition_points = None, entranceTrigger = None):
                self.entrancePointsX = []
                self.entrancePointsY = []
                self.talkingTo = None
                self.level = None
                self.spriteGroup = spriteGroup.copy()
                self.hero = hero
                self.background = background
                self.mainSurface = mainSurface
                self.enemies = enemyList
                self.transition_points = transition_points
                self.pause = False
                        #dictionary of lists of transition points {1:[left_x, right_x, top_y, bottom_y]}
                        #where the key in the dictioary is which side the hero transitioned on:
                        #1 = top of screen, 2 = left of screen, 3 = bottom of screen, 4 = right of screen
                self.sceneTrigger = entranceTrigger

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
        def addSprite(self, newPerson, name):
                if name not in self.spriteGroup:
                        self.spriteGroup[name] = newPerson

        #def addEnemy(self, newEnemy, enemy):

        def paused(self):
                if self.pause:
                        #self.mainSurface.fill(WHITE)
                        pygame.draw.rect(self.mainSurface, BLACK, (100,100,400,300),0)
                        #Title
                        meterLabel = largeFont.render('Hero Meter', True, WHITE)
                        self.mainSurface.blit(meterLabel, (235,150))
                        #Athens's bar
                        pygame.draw.rect(self.mainSurface, BLUE, (230,200,(self.hero.athensPoints +10) * 10,25), 0)
                        pygame.draw.rect(self.mainSurface, BLUE, (230,200,200,25), 5)
                        athensLabel = basicFont.render('Athens', True, BLUE)
                        self.mainSurface.blit(athensLabel, (160,205))
                        #Sparta's bar
                        pygame.draw.rect(self.mainSurface, RED, (230,240,(self.hero.spartaPoints +10) * 10,25), 0)
                        pygame.draw.rect(self.mainSurface, RED, (230,240,200,25), 5)
                        spartaLabel = basicFont.render('Sparta', True, RED)
                        self.mainSurface.blit(spartaLabel, (160,245))
                        #Delphi's bar
                        pygame.draw.rect(self.mainSurface, GREEN, (230,280,(self.hero.delphiPoints +10) * 10,25), 0)
                        pygame.draw.rect(self.mainSurface, GREEN, (230,280,200,25), 5)
                        delphiLabel = basicFont.render('Delphi', True, GREEN)
                        self.mainSurface.blit(delphiLabel, (160,285))
                        
        def unpaused(self):
                self.pause = False
                print("pause no more")

        def setTrigger(self, trigger):
                self.sceneTrigger = trigger
        # This is the function that runs the current scene
        def run(self, hero_coords):
                self.hero.setPosition(hero_coords)
                #talk = False
                talk = False

                while True:
                        if not self.pause:
                                self.drawBackground()
                                self.mainSurface.blit(self.hero.image, self.hero.rect)
                                #health
                                if(self.hero.health == 3):
                                        self.mainSurface.blit(heartImg,(535,0))
                                        self.mainSurface.blit(heartImg,(555,0))
                                        self.mainSurface.blit(heartImg,(575,0))
                                elif self.hero.health == 2:
                                        self.mainSurface.blit(heartImg,(555,0))
                                        self.mainSurface.blit(heartImg,(575,0))
                                elif self.hero.health == 1:
                                        self.mainSurface.blit(heartImg,(575,0))
                                talk, change = self.checkMovement(talk)
                                if change[0] > 0:
                                        return change
                                self.drawAll()

                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                elif event.type == KEYUP:
                                        if event.key == pygame.K_p:
                                                if not self.pause:
                                                        self.pause = True
                                                        print("pause is now True")
                                                        self.paused()
                                                else:
                                                        self.unpaused()
                                        if event.key == K_SPACE and talk and self.talkingTo:
                                                trigger = self.talkingTo.getTextBox(self.mainSurface)
                                                if trigger:
                                                        self.level.reaction(trigger)
                                                        self.talkingTo.talkReaction = None
                                                trigger = None
                                        elif event.key == K_LSHIFT:
                                                weapon = self.hero.getAction()
                                                if weapon:
                                                        self.hitCollision(weapon)

                        pygame.display.update()

                        if self.sceneTrigger:
                                self.level.reaction(self.sceneTrigger)
                                self.sceneTrigger = None
                        
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
                        self.hero.moveImage("up")
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
                        self.hero.moveImage("down")
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
                        self.hero.moveImage("right")
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
                        self.hero.moveImage("left")
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
                        self.spriteGroup[i].update()
                        self.mainSurface.blit(self.spriteGroup[i].image,self.spriteGroup[i].rect)
                if self.enemies:
                        self.enemies.draw(self.mainSurface)

        def transistion(self):
                if self.transition_points == None:
                        if self.hero.rect.bottom > 550 and self.hero.rect.x > 290 and self.hero.rect.x < 310:
                                print("Transition Occurs")
                                return (1, (self.hero.rect.x, self.hero.rect.y))
                        return (0, None)
                else:
                        for transition_point_key in self.transition_points:
                                transition_point_list = self.transition_points[transition_point_key]
                                #[left_x, right_x, top_y, bottom_y]
                                left_x = transition_point_list[0] - 5
                                right_x = transition_point_list[1]
                                top_y = transition_point_list[2] - 5
                                bottom_y = transition_point_list[3] + 5
                                if self.hero.rect.x >= left_x and self.hero.rect.x <= right_x and self.hero.rect.y >= top_y and self.hero.rect.y <= bottom_y:
                                        #print("Transition Occurs", transition_point_key)
                                        #print(self.hero.rect.x, self.hero.rect.y)
                                        return (transition_point_key, (self.hero.rect.x, self.hero.rect.y))
                        return (0, None)

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
                        if pygame.sprite.collide_rect(self.hero, self.spriteGroup[sprite]):
                                return self.spriteGroup[sprite]
                return None

        def wallCollide(self):
                return  self.hero.rect.left < 0 or self.hero.rect.right > self.mainSurface.get_width() or self.hero.rect.top < 0 or self.hero.rect.bottom > self.mainSurface.get_height()


        def remove(self,sprite):
                del self.spriteGroup[sprite]


def getNextScene(current_scene, border, last_hero_coords):
        #current_scene is the number of the current scene
        #border = 1 if the hero crossed the top border, 2 for left, 3 for bottom, 4 for right
        #returns number of next scene 1-12
        if current_scene==1:
                if border==1:
                        return (11, (last_hero_coords[0], 550))
                elif border==2:
                        return (10, (565, last_hero_coords[1]))
                elif border==3:
                        return "error in scene 1 transition"
                elif border==4:
                        return (2, (35, last_hero_coords[1]))
        elif current_scene==2:
                if border==1:
                        return "error in scene 2 transition"
                elif border==2:
                        return (1, (565, last_hero_coords[1]))
                elif border==3:
                        return (5, (last_hero_coords[0], 50))
                elif border==4:
                        return (3, (35, last_hero_coords[1]))
        elif current_scene==3:
                if border==1:
                        return "error in scene 3 transition"
                elif border==2:
                        return (2, (565, last_hero_coords[1]))
                elif border==3:
                        return (4, (last_hero_coords[0], 50))
                elif border==4:
                        return "error in scene 3 transition"
        elif current_scene==4:
                if border==1:
                        return (3, (last_hero_coords[0], 550))
                elif border==2:
                        return (5, (565, last_hero_coords[1]))
                elif border==3:
                        return "error in scene 4 transition"
                elif border==4:
                        return "error in scene 4 transition"
        elif current_scene==5:
                if border==1:
                        return (2, (last_hero_coords[0], 550))
                elif border==2:
                        return (6, (565, last_hero_coords[1]))
                elif border==3:
                        return "error in scene 5 transition"
                elif border==4:
                        return (4, (35, last_hero_coords[1]))
        elif current_scene==7:
                if border==1:
                        return (10, (last_hero_coords[0], 550))
                elif border==2:
                        return (8, (565, last_hero_coords[1]))
                elif border==3:
                        return "error in scene 7 transition"
                elif border==4:
                        return (6, (35, last_hero_coords[1]))
        elif current_scene==8:
                if border==1:
                        return (9, (last_hero_coords[0], 550))
                elif border==2:
                        return "error in scene 8 transition"
                elif border==3:
                        return "error in scene 8 transition"
                elif border==4:
                        return (7, (35, last_hero_coords[1]))
        elif current_scene==9:
                if border==1:
                        return "error in scene 9 transition"
                elif border==2:
                        return "error in scene 9 transition"
                elif border==3:
                        return (8, (last_hero_coords[0], 50))
                elif border==4:
                        return (10, (35, last_hero_coords[1]))
        elif current_scene==10:
                if border==1:
                        return "error in scene 10 transition"
                elif border==2:
                        return (9, (565, last_hero_coords[1]))
                elif border==3:
                        return (7, (last_hero_coords[0], 50))
                elif border==4:
                        return (1, (35, last_hero_coords[1]))
        elif current_scene==11:
                if border==1:
                        return (12, (last_hero_coords[0], 550))
                elif border==2:
                        return "error in scene 11 transition"
                elif border==3:
                        return (1, (last_hero_coords[0], 50))
                elif border==4:
                        return "error in scene 11 transition"
        elif current_scene==12:
                if border==1:
                        return "error in scene 12 transition"
                elif border==2:
                        return "error in scene 12 transition"
                elif border==3:
                        return (11, (last_hero_coords[0], 50))
                elif border==4:
                        return "error in scene 12 transition"
        return "error in scene transition"

