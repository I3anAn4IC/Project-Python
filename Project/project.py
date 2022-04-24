import pygame as pg
import Window
import Block
import random


# иниициализация окна
screen = Window.WindowFullScreen(120, pg.time.Clock(),
                                pg.display.set_mode((0, 0), pg.FULLSCREEN),
                                False)
screen.Screen()

# создание блоков
W = 405
H = 310

Block1 = Block.Blocks((10, 10), (random.randint(75, 405), random.randint(50, 310)))
Block1.AddBlock()
Block1 = Block.Blocks((10, 10), (random.randint(75, 405), random.randint(50, 310)))
Block1.AddBlock()
Block1 = Block.Blocks((10, 10), (random.randint(75, 405), random.randint(50, 310)))
Block1.AddBlock()
Block1 = Block.Blocks((10, 10), (random.randint(75, 405), random.randint(50, 310)))
Block1.AddBlock()
Block12 = Block.Blocks((100, 100), (random.randint(1430, 1835), random.randint(715, 1025)))
Block12.AddBlock()

screen.ScreenBlit(Block1.size_block, Block1.size_block_rect)
screen.ScreenBlit(Block12.size_block, Block12.size_block_rect)

screen.ScreenClose()
