import pygame as pg
from pygame import *
'''Класс создания и закрывания окна'''


class WindowFullScreen(sprite.Sprite, Surface):
    def __init__(self, FPS, clock, screen):
        self.FPS = FPS
        self.clock = clock
        self.screen = screen
        self.gameover = False
        self.window_info = pg.display.Info()

    # def Screen(self):
    #     pg.init()
    #     FPS = self.FPS
    #     clock = self.clock
    #     screen = self.screen
    #     # pg.display.flip()

    def ScreenBlit(self, firstname, secondname):
        self.screen.blit(firstname, secondname)

    def ScreenClose(self):
        gameover = self.gameover
        while not gameover:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        gameover = True

            self.clock.tick(self.FPS)
            pg.display.flip()

        if gameover:
            pg.quit()


# class Blocks():
#     def __init__(self, size_block):
#         self.size_block = size_block
#         self.rect = self.size_block.get_rect(center=(150, 150))
