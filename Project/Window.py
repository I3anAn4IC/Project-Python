import pygame as pg

'''Класс создания и закрывания окна'''


class WindowFullScreen:
    def __init__(self, FPS, clock, screen, gameover):
        self.FPS = FPS
        self.clock = clock
        self.screen = screen
        self.gameover = gameover

    def Screen(self):
        pg.init()
        FPS = self.FPS
        clock = self.clock
        screen = self.screen
        pg.display.flip()

    def ScreenBlit(self, firstname, secondname):
        self.screen.blit(firstname, secondname)
        pg.display.flip()

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
