import pygame as pg

'''Класс создания и закрывания окна'''


class WindowFullScreen:
    def __init__(self, FPS, clock, screen, gameover, window_info):
        self.FPS = FPS
        self.clock = clock
        self.screen = screen
        self.gameover = gameover
        self.window_info = window_info

    def Screen(self):
        pg.init()
        FPS = self.FPS
        clock = self.clock
        screen = self.screen
        self.window_info = pg.display.Info()
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


# class Blocks():
#     def __init__(self, size_block):
#         self.size_block = size_block
#         self.rect = self.size_block.get_rect(center=(150, 150))
