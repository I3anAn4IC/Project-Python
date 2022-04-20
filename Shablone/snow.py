import pygame as pg

#создание экрана
pg.init()

FPS = 120
clock = pg.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

sun = pg.Surface((100, 100))
canvas = pg.Surface((1600, 600))
cloud = pg.Surface((100, 100))

canvas_rect = canvas.get_rect()
sun_rect = sun.get_rect()
cloud_rect = cloud.get_rect()

canvas_rect.center = (0, 600)
sun_rect.center = (600, 600/2)
cloud_rect.center = (0, 100)

canvas.fill((27, 184, 13))
sun.fill((0, 0, 0))
sun.set_colorkey((0, 0, 0))
cloud.fill((0, 0, 0))
# cloud.set_colorkey((0, 0, 0))

pg.draw.circle(sun, (247, 223, 7), (50, 50), 25)
pg.draw.circle(cloud, (255, 255, 255), (0, 50), 25)
# pg.draw.rect(canvas, )
screen.blit(canvas, canvas_rect)
screen.blit(sun, sun_rect)
screen.blit(cloud, cloud_rect)

# cload = pg.image.load('cload.png')
# cload_rect = cload.get_rect()
# cload_rect.center = (800/2, 600/2)
# screen.blit(cload, cload_rect)

gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True

    if sun_rect.top > 300:
        sun_rect.bottom = 0
    sun_rect.y += 2
    screen.blit(sun, sun_rect)

    clock.tick(FPS)
    pg.display.flip()

if gameover:
    pg.quit()

