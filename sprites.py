# This file was created by: Sandryan Matar

# import modules
import pygame as pg
from pygame.sprite import Sprite
from settings import *
# create a player class

# create a wall class
# Create a player class with all the basic stats and functions

vec =pg.math.Vector2


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
        self.weapon_drawn = False
        self.weapon_dir = (0,0)
        self.weapon = Sword(self.game, self.rect.x, self.rect.y, 16, 16, (0,0))
        
        def get_mouse(self):
            if pg.mouse.get_pressed()[0]:
                if self.weapon_drawn == False:
                   self.weapon_drawn = True
                if abs(pg.mouse.get_pos()[0]-self.rect.x) > abs(pg.mouse.get_pos()[1]-self.rect.y):
                    if pg.mouse.get_pos()[0]-self.rect.x > 0:
                        print("swing to pos x")
                        self.weapon = Sword(self.game, self.rect.x+TILESIZE, self.rect.y, 16, 16, (1,0))
                    if pg.mouse.get_pos()[0]-self.rect.x < 0:
                        print("swing to neg x")
                        self.weapon = Sword(self.game, self.rect.x-16, self.rect.y, 16, 16, (1,0))
                else:
                    if pg.mouse.get_pos()[1]-self.rect.y > 0:
                        print("swing to pos y")
                    if pg.mouse.get_pos()[1]-self.rect.y < 0:
                        print("swing to neg y")
        if pg.mouse.get_pressed()[1]:
            print("middle click")
        if pg.mouse.get_pressed()[2]:
            print("right click")

    #def move(self, dx=0, dy=0):
        #self.x += dx
        #self.y += dy
   # movement/utilities
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
        if keys[pg.K_e]:
            print("trying to shoot...")
            self.poof()
    # bullet
    def poof(self):
        p = Bullet(self.game, self.rect.x, self.rect.y)
        print(p.rect.x)
        print(p.rect.y)

#collects objects
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
#collision
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
#collect coins
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
             
             self.moneybag += 1
            if str(hits[0].__class__.__name__) == "Emerald":
             
             self.moneybag += 3
             


    # def collect_coins(self, dir):
    #     if dir == 'x':
    #        hits = pg.sprite.spritecollide(self, self.game.coins, True)
    #        if hits:
    #            if self.vx > 0:
    #                self.x = hits[0].rect.top - self.rect.width
    #            if self.vx < 0:
    #                self.x = hits[0].rect.bottom 
    #            self.vx = 0
    #            self.rect.x = self.x

    #     if dir == 'y':
    #        hits = pg.sprite.spritecollide(self, self.game.coins, True)
    #        if hits:
    #             if self.vy > 0:
    #                 self.y = hits[0].rect.top - self.rect.width
    #             if self.vy < 0:
    #                 self.y = hits[0].rect.bottom 
    #             self.vy = 0
    #             self.rect.y = self.y


    # def collect_emeralds(self, dir):
    #     if dir == 'x':
    #        hits = pg.sprite.spritecollide(self, self.game.emeralds, True)
    #        if hits:
    #            if self.vx > 0:
    #                self.x = hits[0].rect.top - self.rect.width
    #            if self.vx < 0:
    #                self.x = hits[0].rect.bottom 
    #            self.vx = 0
    #            self.rect.x = self.x

    #     if dir == 'y':
    #        hits = pg.sprite.spritecollide(self, self.game.emeralds, True)
    #        if hits:
    #             if self.vy > 0:
    #                 self.y = hits[0].rect.top - self.rect.width
    #             if self.vy < 0:
    #                 self.y = hits[0].rect.bottom 
    #             self.vy = 0
    #             self.rect.y = self.y
    
#movement/collision
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
    


#new currency
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
#new currency
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
#enemy added
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
        
     #mob movement
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
    
  #Creates new mob
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
        self.hitpoints = 1
        

        
#new mob movement
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
          if self.hitpoints < 1:
             self.kill()



# bullets
class Bullet(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE/4, TILESIZE/4))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        print("BAM")
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
    def update(self):
        self.collide_with_group(self.game.coins, True)
        self.rect.y -= self.speed
        # pass
#weapon added
class Sword(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, dir):
        self.groups = game.all_sprites, game.weapons
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.rect.width = w
        self.rect.height = h
        self.pos = vec(x,y)
        self.dir = dir
        print("I created a sword")
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Mob":
                print("you hurt a mob!")
                hits[0].hitpoints -= 1
            if str(hits[0].__class__.__name__) == "Super":
                print("you hurt a super!")
                hits[0].hitpoints -= 3
    def track(self, obj):
        self.rect.x = obj.rect.x
        self.rect.y = obj.rect.y
        self.vx = obj.vx
        self.vy = obj.vy
    def update(self):
        if self.game.player.weapon_drawn == False:
            self.kill()
        self.track(self.game.player)
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.rect.y = self.y
        self.collide_with_group(self.game.mobs, False)

          #if self.hitpoints < 1:
          #  print("mob2 should be dead")
          #  self.kill()
         # self.sensor()
          #if self.chasing:
           # self.rot = (self.game.player.rect.center - self.pos).angle_to(vec(1, 0))
            # self.image = pg.transform.rotate(self.image, 45)
            # self.rect = self.image.get_rect()
           # self.rect.center = self.pos
           # self.acc = vec(self.speed, 0).rotate(-self.rot)
           # self.acc += self.vel * -1
           # self.vel += self.acc * self.game.dt
           # self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            # self.hit_rect.centerx = self.pos.x
           # collide_with_walls(self, self.game.walls, 'x')
            # self.hit_rect.centery = self.pos.y
           # collide_with_walls(self, self.game.walls, 'y')
            # self.hit_rect.centery = self.pos.y
           
            # self.rect.center = self.hit_rect.center
            # if self.health <= 0:
            #     self.kill()

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