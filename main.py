# This file was created by: Sandryan Matar
# My first source control edit

# import necessary modules
import pygame as pg 
import sys 
from settings import * 
from sprites import *
from random import randint
from os import path





# Creating the game class
class Game:
    # game screen and run
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) 
        self.load_data()
        #load saved game data etc
    # Defining the run method
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
           for line in f:
              self.map_data.append(line)
    def new(self):
        # init all varables, setup groups, instantiate classes
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
       # self.power_ups = pg.sprite.Group()
        #self.foods = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.coins = pg.sprite.Group()
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
             # if tile == 'U':
                   # PowerUp(self, col, row)
             # if tile == 'F':
                    #Food(self, col, row)
              if tile == 'M':
                    Mob(self, col, row)
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
    def update(self):
        self.all_sprites.update()
# draw game map
    def draw_grid(self):
        for x in range(0,WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0,WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
        
        
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
        pg.display.flip()
        #self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
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