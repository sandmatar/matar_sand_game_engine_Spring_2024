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
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y  = y * TILESIZE

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


  #  def collide_with_obj(self, group, kill, desc):
    #    hits = pg.sprite.spritecollide(self, group, kill)
        #if hits and desc == "coin"

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

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
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
    



class Coin (Sprite):
  def __init__(self, game, x, y):
      self.groups = game.all_sprites
      Sprite.__init__(self, self.groups)
      self.game = game
      self.image = pg.Surface((TILESIZE, TILESIZE))
      self.image.fill(YELLOW)
      self.rect = self.image.get_rect()
      self.vx, self.vy = 0, 0
      self.rect.x = x * TILESIZE
      self.rect.y = y * TILESIZE
      self.image.fill(GREEN)