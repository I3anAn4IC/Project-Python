import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 600))
gameover = False
pt = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
timer = pg.time.Clock()
# платформа
paddlew = 200
paddleh= 25
paddlex =300
paddley = 550
live = 5

# смайлик
pic = pg.image.load('smile02.png')
picx=0
picy=0
picw=100
pich=100
speedx = 5
speedy = 5
screen.blit(pic, (picx, picy))
pg.display.flip()

while not gameover:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            gameover=True
        if event.type == pg.MOUSEBUTTONDOWN

    screen.fill(BLACK)
    # отрисовка платформы
    paddlex = pg.mouse.get_pos()[0]
    paddlex -= paddlew/2
    pg.draw.rect(screen,WHITE,(paddlex,paddley,paddlew, paddleh))
    # механика движения смайлика
    if picx >=800-100 :
        speedx = -1*speedx
    if picy >=600-100 :
        speedy = -1*speedy
        live = live - 1
        print(live)
    if picy < 0:
        speedy = -1 * speedy
    picx = picx + speedx
    picy = picy+speedy

    # отрисовка смайлика
    screen.blit(pic, (picx, picy))
    # проверка взаимодействий
    if picy + pich >=  paddley:
        if picx+ picw//2>=paddlew and picx + picw//2<=paddlex + paddlew:
            speedy = -speedy
            pt = pt+1
    if pt ==5:
        speedy = 20
        speedx = 20
    if live == 0:
        gameover = True

    pg.display.flip()
    timer.tick(30)

if gameover:
    pg.quit()
