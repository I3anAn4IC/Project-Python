import pygame as pg

#создание экрана
pg.init()
FPS = 120
clock = pg.time.Clock()
screen = pg.display.set_mode((800, 600))

# smile = pg.image.load('smile02.png')
# smile_rect = smile.get_rect()
# smile_rect.center = (800/2, 600/2)
# screen.blit(smile, smile_rect)
#
# apple = pg.image.load('apple.png')
# apple_et = pg.image.load('apple.png')
# apple = pg.transform.scale(apple, (50, 50))
# apple_rect = smile.get_rect()
# apple_rect.center = (250, 250)

color = pg.Surface((100, 100))
color_rect = color.get_rect()
color_rect.center = (50, 50)
pg.draw.rect(color, (255, 0, 106), (0, 0, 25, 25))
pg.draw.rect(color, (174, 0, 255), (25, 25, 25, 25))
pg.draw.rect(color, (255, 247, 0), (0, 25, 25, 25))
pg.draw.rect(color, (0, 255, 255), (25, 0, 25, 25))
screen.blit(color, color_rect)
# screen.blit(apple, apple_rect)

#вывод на дисплей
pg.display.flip()

#цикл закрытия, цыкл игры
m_left = False
m_right = False
m_up = False
m_down = False
mousedown = False
angel = 0
pos = (0, 0)
pos_draw = (0, 0)
color_draw = (255, 0, 106)

gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                m_left = True
            if event.key == pg.K_d:
                m_right = True
            if event.key == pg.K_w:
                m_up = True
            if event.key == pg.K_s:
                m_down = True
            if event.key == pg.K_f:
                pg.image.save(screen, 'test-picture.png')

        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                m_right = False
            if event.key == pg.K_a:
                m_left = False
            if event.key == pg.K_w:
                m_up = False
            if event.key == pg.K_s:
                m_down = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pg.MOUSEBUTTONUP:
            mousedown = False
    screen.blit(color, color_rect)
    angel += 2
    # apple = pg.transform.rotate(apple_et, angel)
    # apple_rect.center = (250, 250)
    # screen.fill((0, 0, 0))
    # if m_left:
    #     smile_rect.x -= 2
    # if m_right:
    #     smile_rect.x += 2
    # if m_up:
    #     smile_rect.y -= 2
    # if m_down:
    #     smile_rect.y += 2
    if mousedown:
        pos = pg.mouse.get_pos()
        if 25 > pos[0] > 0 and 25 > pos[1] > 0:
            color_draw = (255, 0, 106)
        if 50 > pos[0] > 25 and 50 > pos[1] > 25:
            color_draw = (174, 0, 255)
        if 50 > pos[0] > 25 and 25 > pos[1] > 0:
            color_draw = (0, 255, 255)
        if 25 > pos[0] > 0 and 50 > pos[1] > 25:
            color_draw = (255, 247, 0)
        # if pos == (0, 0, 25, 25):
        #     color_draw = (255, 247, 0)
        # if pos == (0, 25, 25, 25):
        #     color_draw = (255, 247, 0)
        pg.draw.circle(screen, color_draw, pos, 5)
    # screen.blit(smile, smile_rect)
    # screen.blit(apple, apple_rect)
    clock.tick(FPS)
    pg.display.flip()

if gameover:
    pg.quit()


