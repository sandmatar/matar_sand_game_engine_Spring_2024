# This file was created by: Sandryan Matar
# My first source control edit
#Sources:
#ChatGPT
# New map, new enemies, kill enemies
# jump verb

#BETA GOALS:
 #First goal; more obstacles against the player (Random spawning)
 #Second goal; more maps

#Final goal: Jumpscare



# import necessary modules
import pygame as pg
import sys 
from settings import * 
from sprites import *
from random import randint
from os import path
from math import floor
import images
import pygame.display

LEVEL1 = "map.txt"
LEVEL2 = "mapp.txt"

#Coded in assistance with ChatGPT
#Jumpscare image used from Adobe Stock
#Creates a scary image upon opening game
pg.display
class Jumpscare():
    def __init__(self, screen_width, screen_height):
        self.jumpscares = pg.image.load(path.join(img_folder, 'jumpscare1.jpg')).convert_alpha()
        # Scale jumpscare image to match screen resolution
        self.jumpscares = pg.transform.scale(self.jumpscares, (1024, 768))

    def trigger_jumpscare(self, screen):
        screen.blit(self.jumpscares, (0, 0))  # Blit the jumpscare onto the screen
        pg.display.flip()
        pg.time.wait(2000)  # Display jumpscares for 2 seconds

# Initialize Pygame 
pg.init()

# Set up the display
screen_width = 1024
screen_height = 768
screen = pg.display.set_mode((screen_width, screen_height))

# Make an instance of Jumpscare
jumpscare = Jumpscare(screen_width, screen_height)


# Game loop
running = True

jumpscare = Jumpscare(screen, screen_height)


jumpscare.trigger_jumpscare(screen)

pg.display.flip()
    # Update display
pg.display.update()

class Cooldown():
    # sets all properties to zero when instantiated...
     def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
        # ticking ensures the timer is counting...
    # must use ticking to count up or down
     def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
    # resets event time to zero - cooldown reset
     def countdown(self, x):
         x = x - self.delta
         if x != None:
             return x
     def event_reset(self):
         self.event_time = floor((pg.time.get_ticks())/1000)
    # sets current time
     def timer(self):
         self.current_time = floor((pg.time.get_ticks())/1000)



# Creating the game class
class Game:
    # game screen and run
    def __init__(self):
        self.player = None  
        self.enemy_spawn_timer = 0
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) 
        self.load_data()
        #load saved game data etc
    # Defining the run method
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.img_folder = path.join(self.game_folder, 'images')
        self.player_img = pg.image.load(path.join(self.img_folder, 'dobby.png')).convert_alpha()
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        self.map_data = []
        with open(path.join(self.game_folder, 'map.txt'), 'rt') as f:
           for line in f:
              self.map_data.append(line)
     
    
    # new map after coinbag full
    def change_level(self, lvl):
        for s in self.all_sprites:
               s.kill()
        self.moneybag = 0
        self.map_data = []
        with open(path.join(self.game_folder, 'mapp.txt'), 'rt') as f:
              for line in f:
                print(line)
                self.map_data.append(line)
       
        for row, tiles in enumerate(self.map_data):
            print(self.map_data)
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'E':
                    Emerald(self, col, row)    
                        
   



    def new(self):
        # init all varables, setup groups, instantiate classes
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
       # self.power_ups = pg.sprite.Group()
        #self.foods = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.supers = pg.sprite.Group()
        self.emeralds = pg.sprite.Group()
        self.weapons = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
       # self.player = Player(self, 10, 10)
        #for x in range(10, 20):
          #  Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
           print(self.map_data)
           #print(row)
           #print(tiles)
           for col, tile in enumerate(tiles):
              #print(col)
              #print(tiles)
              if tile == '1':
                 Wall(self, col, row)
              if tile == 'P':
                 self.player = Player(self, col, row)
              if tile == 'C':
                  Coin(self, col, row)
              if tile == 'E':
                  Emerald(self, col, row)
              # tile == 'U':
                   # PowerUp(self, col, row)
             # if tile == 'F':
                    #Food(self, col, row)
              if tile == 'M':
                    Mob(self, col, row)
              if tile == 'S':
                    Super(self, col, row)
              if tile == 'R':
                    new_enemy = Super(self, col, row)
                    new_enemy.spawn(self.screen.get_width(), self.screen.get_height())
   # run game
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    # close game window
    def quit(self):
        pg.quit()
        sys.exit()
# import all sprites while playing
#change map
    def update(self):
        self.all_sprites.update()
        if self.player.moneybag > 15:
            self.change_level('mapp.txt')
        self.enemy_spawn_timer += self.dt
        if self.enemy_spawn_timer == (5-10):
            self.spawn_enemies()
            self.enemy_spawn_timer == (5-10)
        
#randomly spawn enemies/coded in assistance with friend and Mr. Cozort
    def spawn_enemies(self):
        for _ in range(12):
            col = random.randint(0, len(self.map_data[0]) - 1)  # Random column
            row = random.randint(0, len(self.map_data) - 1)     # Random row
            if self.map_data[row][col] == '.':
                Super(self, col, row, self.screen.get_width(), self.screen.get_height())
# draw game map
    def draw_grid(self):
        for x in range(0,WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0,WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
        
# shows currency
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)        
        pg.display.flip()
       

    # The input method
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
             self.quit()
            #if event.type == pg.KEYDOWN:
             # if event.key == pg.K_LEFT:
              #  self.player.move(dx=-1)
             # if event.key == pg.K_RIGHT:
             #   self.player.move(dx=1)
             # if event.key == pg.K_DOWN:
             #   self.player.move(dy=1)
             # if event.key == pg.K_UP:
             #   self.player.move(dy=-1)
#shows currency 
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)

    
    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
#g.show_start_screen()
while True:
    g.new()
    g.run()
    #g.show_go_screen()
g.run()