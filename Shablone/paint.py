import pygame as pg

#создание экрана
pg.init()
FPS = 120
clock = pg.time.Clock()
screen = pg.display.set_mode((800, 600))

pg.display.flip()