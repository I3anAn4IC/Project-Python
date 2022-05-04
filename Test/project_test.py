import pygame as pg
import Block
import random
import Button

# иниициализация окна
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.init()
FPS = 120
clock = pg.time.Clock()
# screen.Screen()

# создание блоков
W = pg.display.Info().current_w
H = pg.display.Info().current_h


Block1 = Block.Blocks((10, 10), (random.randint(75, (W//3)-75), random.randint(50, (H//3)-50)))
Block1.AddBlock()
Block2 = Block.Blocks((10, 10), (random.randint(W//3, W-(W//3)-75), random.randint(50, (H//3)-50)))
Block2.AddBlock()
Block3 = Block.Blocks((10, 10), (random.randint(W-(W//3), W-75), random.randint(50, (H//3)-50)))
Block3.AddBlock()

Block4 = Block.Blocks((10, 10), (random.randint(75, (W//3)-75), random.randint((H//3), H-(H//3)-50)))
Block4.AddBlock()
Block5 = Block.Blocks((10, 10), (random.randint(W//3, W-(W//3)-75), random.randint((H//3), H-(H//3)-50)))
Block5.AddBlock()
Block6 = Block.Blocks((10, 10), (random.randint(W-(W//3), W-75), random.randint((H//3), H-(H//3)-50)))
Block6.AddBlock()

Block7 = Block.Blocks((10, 10), (random.randint(75, (W//3)-75), random.randint(H-(H//3), H-50)))
Block7.AddBlock()
Block8 = Block.Blocks((10, 10), (random.randint(W//3, W-(W//3)-75), random.randint(H-(H//3), H-50)))
Block8.AddBlock()
Block9 = Block.Blocks((10, 10), (random.randint(W-(W//3), W-75), random.randint(H-(H//3), H-50)))
Block9.AddBlock()


screen.blit(Block1.size_block, Block1.size_block_rect)
screen.blit(Block2.size_block, Block2.size_block_rect)
screen.blit(Block3.size_block, Block3.size_block_rect)

screen.blit(Block4.size_block, Block4.size_block_rect)
screen.blit(Block5.size_block, Block5.size_block_rect)
screen.blit(Block6.size_block, Block6.size_block_rect)

screen.blit(Block7.size_block, Block7.size_block_rect)
screen.blit(Block8.size_block, Block8.size_block_rect)
screen.blit(Block9.size_block, Block9.size_block_rect)

gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                gameover = True

    clock.tick(FPS)
    pg.display.flip()

if gameover:
    pg.quit()
