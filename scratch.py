# loop through a list

import pygame as pg

clock = pg.time.Clock()
FPS = 30

frames = ["frame1", "frame2", "frame3", "frame4"]

#print(len(frames))


current_frame = 0

frames_length = len(frames)

then = 0


while True:
    #print("forever.....")
    now = pg.time.get_ticks()
    clock.tick(FPS)
    if now - then > 250:
        print(now)
        then = now
        print(frames[current_frame%frames_length])
        current_frame += 1
