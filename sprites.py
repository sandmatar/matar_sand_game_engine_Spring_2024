# This file was created by: Sandryan Matar

# import modules
import pygame as pg
from pygame.sprite import Sprite
from settings import *
# create a player class

# create a wall class
# Create a player class with all the basic stats and functions

class Player(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image = game.player_img
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y  = y * TILESIZE
        self.moneybag = 0
        self.speed = 300

    #def move(self, dx=0, dy=0):
        #self.x += dx
        #self.y += dy

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071


    def collide_with_obj(self, group, kill, desc):
        hits = pg.sprite.spritecollide(self, group, kill)
       # if hits and desc == "food":
            #print("I collided with food")
          #  self.image.fill(GREEN)
        #if #hits and desc == "powerup":
          #  print("I collided with powerup")
           # self.image.fill(GREEN)
        if hits and desc == "mob":
            print("I collided with mob")
            self.image.fill(GREEN)
            self.hitpoints -= 10
        if hits and desc == "super":
            print("I collided with super")
            self.image.fill(RED)
            self.hitpoints -= 10

    def collide_with_walls(self, dir):
        if dir == 'x':
           hits = pg.sprite.spritecollide(self, self.game.walls, False)
           if hits:
               if self.vx > 0:
                   self.x = hits[0].rect.left - self.rect.width
               if self.vx < 0:
                   self.x = hits[0].rect.right 
               self.vx = 0
               self.rect.x = self.x

        if dir == 'y':
           hits = pg.sprite.spritecollide(self, self.game.walls, False)
           if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.width
                if self.vy < 0:
                    self.y = hits[0].rect.bottom 
                self.vy = 0
                self.rect.y = self.y
        
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
             self
             coinbag = +1
            if str(hits[0].__class__.__name__) == "Emerald":
             self
             coinbag = +1
   


    def collect_coins(self, dir):
        if dir == 'x':
           hits = pg.sprite.spritecollide(self, self.game.coins, True)
           if hits:
               if self.vx > 0:
                   self.x = hits[0].rect.top - self.rect.width
               if self.vx < 0:
                   self.x = hits[0].rect.bottom 
               self.vx = 0
               self.rect.x = self.x

        if dir == 'y':
           hits = pg.sprite.spritecollide(self, self.game.coins, True)
           if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.width
                if self.vy < 0:
                    self.y = hits[0].rect.bottom 
                self.vy = 0
                self.rect.y = self.y


    def collect_emeralds(self, dir):
        if dir == 'x':
           hits = pg.sprite.spritecollide(self, self.game.emeralds, True)
           if hits:
               if self.vx > 0:
                   self.x = hits[0].rect.top - self.rect.width
               if self.vx < 0:
                   self.x = hits[0].rect.bottom 
               self.vx = 0
               self.rect.x = self.x

        if dir == 'y':
           hits = pg.sprite.spritecollide(self, self.game.emeralds, True)
           if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.width
                if self.vy < 0:
                    self.y = hits[0].rect.bottom 
                self.vy = 0
                self.rect.y = self.y
    

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        self.collide_with_group(self.game.coins, True)
        self.collide_with_group(self.game.emeralds, True)
        #self.collide_with_group(self.game.powerups, True)

        #coin_hits = pg.sprite.spritecollide(self.game.coins, True, kill)
        #if coin_hits:
          #   print("I got a coin")
          #   coinbag = + 1
        #self.collide_with_obj(self.game.power_ups, True, "powerup")
        #self.collide_with_obj(self.game.foods, True, "food")
        self.collide_with_obj(self.game.mobs, True, "mob")
        self.collide_with_obj(self.game.supers, True, "super")
        #self.collide_with
# create a wall class that blocks player movement
class Wall(Sprite):
     def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    



class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
class Emerald(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.emeralds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.rect.x = x
        self.rect.y = y 
        self.vx = ENEMY_SPEED
        self.vy = ENEMY_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        

    def collide_with_walls(self, dir):
        if dir == 'x':
           hits = pg.sprite.spritecollide(self, self.game.walls, False)
           if hits:
               if self.vx > 0:
                   self.x = hits[0].rect.left - self.rect.width
               if self.vx < 0:
                   self.x = hits[0].rect.right 
               self.vx = -self.vx
               self.rect.x = self.x

        if dir == 'y':
           hits = pg.sprite.spritecollide(self, self.game.walls, False)
           if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.width
                if self.vy < 0:
                    self.y = hits[0].rect.bottom 
                self.vy = -self.vy
                self.rect.y = self.y
    

class Super(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.supers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.rect.x = x
        self.rect.y = y 
        self.vx = ENEMY_SPEED
        self.vy = ENEMY_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 1.500
            self.vy *= 1.500
        

    def collide_with_walls(self, dir):
        if dir == 'x':
           hits = pg.sprite.spritecollide(self, self.game.walls, False)
           if hits:
               if self.vx > 0:
                   self.x = hits[0].rect.left - self.rect.width
               if self.vx < 0:
                   self.x = hits[0].rect.right 
               self.vx = -self.vx
               self.rect.x = self.x

        if dir == 'y':
           hits = pg.sprite.spritecollide(self, self.game.walls, False)
           if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.width
                if self.vy < 0:
                    self.y = hits[0].rect.bottom 
                self.vy = -self.vy
                self.rect.y = self.y
    
    def update(self):
          #self.rect.x = self.x * TILESIZE
          #self.rect.y = self.y * TILESIZE
          self.x += self.vx * self.game.dt
          self.y += self.vy * self.game.dt
          self.rect.x = self.x
          self.collide_with_walls('x')
          self.rect.y = self.y
          self.collide_with_walls('y')

#class PowerUp(Sprite):
    #def __init__(self, game, x, y):
      # add powerup groups later....
      #  self.groups = game.all_sprites, game.power_ups
       # Sprite.__init__(self, self.groups)
      #  self.game = game
      #  self.image = pg.Surface((TILESIZE, TILESIZE))
      #  self.image.fill(RED)
      #  self.rect = self.image.get_rect()
       # self.x = x
      #  self.y = y
     #   self.rect.x = x * TILESIZE
      #  self.rect.y = y * TILESIZE

# Food(Sprite):
   # def __init__(self, game, x, y):
        # add powerup groups later....
        #self.groups = game.all_sprites, game.foods
        #Sprite.__init__(self, self.groups)
        #self.game = game
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.image.fill(LIGHTGREY)
       # self.rect = self.image.get_rect()
       # self.x = x
       # self.y = y
       # self.rect.x = x * TILESIZE
      #  self.rect.y = y * TILESIZEclass Mob(Sprite):
   # def __init__(self, game, x, y):
     #c#lass Mob(Sprite):
     ##add powerup groups later....
     # self.groups = game.all_sprites, game.mobs
    # Sprite.__init__(self, self.groups)
    # self.game = game
    # self.image = pg.Surface((TILESIZE, TILESIZE))
     #self.image.fill(LIGHTGREY)
     #self.rect = self.image.get_rect()
     #self.x = x
    # self.y = y
    # self.rect.x = x * TILESIZE
     #self.rect.y = y * TILESIZE