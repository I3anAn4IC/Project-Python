import pygame as pg
import random


class Fruit(pg.sprite.Sprite):
    def __init__(self, x, filename, speedy):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename)
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speedy = speedy

    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speedy
        else:
            self.rect.bottom = 0
            self.rect.x = random.randint(50, W-5)


class Cat(pg.sprite.Sprite):
    def __init__(self, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename)
        # self.image = pg.transform.scale(self.image, (W, 50))
        self.rect = self.image.get_rect(center=(W//2, H-50))

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            if self.rect.left >= 0:
                self.rect.x -= 5
        if key[pg.K_d]:
            if self.rect.right <= W:
                self.rect.x += 5

# создание экрана
pg.init()
FPS = 120
clock = pg.time.Clock()
W = 800
H = 600
screen = pg.display.set_mode((W, H))


# apple1 = Fruit(random.randint(50, 750), 'apple.png')
# apple2 = Fruit(random.randint(50, 750), 'apple.png')
# apple3 = Fruit(random.randint(50, 750), 'apple.png')
fruits = pg.sprite.Group(Fruit(random.randint(50, 750), 'apple.png', random.randint(2, 10)),
                         Fruit(random.randint(50, 750), 'apple.png', random.randint(2, 10)))
fruits.add(Fruit(random.randint(50, 750), 'ananas.png', random.randint(2, 10)))
cat = Cat('cat.png')

myfont = pg.font.SysFont(None, 35)
text = myfont.render('Points', True, (242, 10, 79))
# #вывод на дисплей
pg.display.flip()

gameover = False
ananas = False
points = 0
points1 = str(points)
text_points = str('Points: ' + points1)
error = 0

while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True
    # apple1.update()
    # apple2.update()
    # apple3.update()
    # screen.fill((0, 0, 0))
    # screen.blit(apple1.image, apple1.rect)
    # screen.blit(apple2.image, apple2.rect)
    # screen.blit(apple3.image, apple3.rect)
    screen.fill((0, 0, 0))
    fruits.update()
    fruits.draw(screen)
    cat.update()
    screen.blit(cat.image, cat.rect)

    # взаимодействие
    if pg.sprite.spritecollide(cat, fruits, dokill=True):
        points += 1
        points1 = str(points)
        text_points = str('Points: ' + points1)
        print(points)
        if ananas == True:
            fruits.add(Fruit(random.randint(50, 750), 'ananas.png', random.randint(2, 10)))
            ananas = False
        else:
            fruits.add(Fruit(random.randint(50, 750), 'apple.png', random.randint(2, 10)))
            ananas = True
    else:
        error += 1

    if error == 3:
        text1 = myfont.render('Game over', True, (242, 10, 79))
        screen.blit(text1, (W//2, H//2))
    text = myfont.render(text_points, True, (242, 10, 79))
    screen.blit(text, (0, 0))

    clock.tick(FPS)
    pg.display.flip()

if gameover:
    pg.quit()

