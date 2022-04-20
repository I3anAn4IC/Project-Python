import pygame as pg


class Blocks(object):
    def __init__(self, size_block):
        self.size_block = size_block
        self.size_block_rect = size_block.get_rect()

    def Blockfg(self):
        size_block = self.size_block
        size_block_rect = self.size_block_rect
        size_block_rect.center = (150, 150)
        color = (255, 0, 123)
        pg.draw.rect(size_block, color, (0, 0, 250, 200))
