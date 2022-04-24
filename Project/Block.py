import pygame as pg


class Blocks(object):
    def __init__(self, size_block, coordinates):
        self.size_block_rect = None
        self.size_block = size_block
        self.coordinates = coordinates

    def AddBlock(self):
        self.size_block = pg.Surface((150, 100))
        self.size_block_rect = self.size_block.get_rect()
        self.size_block_rect.center = self.coordinates
        color = (255, 0, 123)
        pg.draw.rect(self.size_block, color, (0, 0, 400, 200))
