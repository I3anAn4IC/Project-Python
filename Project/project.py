import pygame as pg
import Window
import Block


# иниициализация окна
screen = Window.WindowFullScreen(120, pg.time.Clock(),
                                pg.display.set_mode((0, 0), pg.FULLSCREEN),
                                False)
screen.Screen()

# создание блоков
Block1 = Block.Blocks((100, 100))
# size_block = pg.Surface((100, 100))
# size_block_rect = size_block.get_rect()
# size_block_rect.center = (150, 150)
# color = (255, 0, 123)
# pg.draw.rect(size_block, color, (0, 0, 250, 200))

screen.ScreenBlit(size_block, size_block_rect)

screen.ScreenClose()
