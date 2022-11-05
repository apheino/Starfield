import pygame as pg

import random
import sys
import math

RES = WIDTH, HEIGHT = 1600,900
NUM_STARS = 200
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
MAX_DIST = 1000
SPEED = 0.6
STAR_SIZE = 15

pg.init()

screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
delta_time = 1

stars = [[random.randint(0, RES[0]), random.randint(0, RES[1]), random.randint(0, MAX_DIST),random.randint(5, STAR_SIZE)] for _ in range(NUM_STARS)]

def run():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
               
        delta_time = clock.tick(FPS)
        pg.display.set_caption(f'{clock.get_fps() :.1f}')

        screen.fill('black')
        for i,star in enumerate(stars):
            star[2] -= SPEED*delta_time
            dist_scale = 1-star[2]/MAX_DIST

            pos_vect = (star[0]-HALF_WIDTH, star[1]-HALF_HEIGHT)
            pos_mag = math.sqrt(pos_vect[0]*pos_vect[0] + pos_vect[1]*pos_vect[1])
            pos_unit = (pos_vect[0]/pos_mag, pos_vect[1]/pos_mag)
            star[0] = star[0]+pos_unit[0]*20*dist_scale*dist_scale
            star[1] = star[1]+pos_unit[1]*22*dist_scale*dist_scale

            
            if star[0]<-STAR_SIZE or star[0]>WIDTH+STAR_SIZE or star[1]<-STAR_SIZE or star[1]>HEIGHT+STAR_SIZE or star[2]<=0:
                stars[i] = [random.randint(0, RES[0]), random.randint(0, RES[1]), MAX_DIST, random.randint(5, STAR_SIZE)]

            dist_scale = 1-star[2]/MAX_DIST
            color = min(255*dist_scale, 255)
            pg.draw.circle(screen, (color, color, color), (star[0],star[1]), max(star[3]*dist_scale,1))
        pg.display.flip()
    
if __name__ == '__main__':
    run()

