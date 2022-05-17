import pygame as pg
import random
import threading

# иниициализация окна

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.init()
FPS = 120
clock = pg.time.Clock()

# создание блоков

W = pg.display.Info().current_w
H = pg.display.Info().current_h


class Button:
    def __init__(self, width, height, screen, inactive_color=(240, 166, 148), active_color=(229, 116, 58)):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    # "рисовка" кнопки на экране

    def draw_button(self, x, y, message=None, font=None, button_num=None, done=None):
        global width_text, height_text, score, f, over, points
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if len(message) >= 1:
            font_button = pg.font.Font(None, self.height)
            text = font_button.render(message, True, self.height)
            width_text = text.get_width()
            height_text = text.get_height()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pg.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            if click[0] == 1:
                if button_num == 3:
                    if t[0] == min(t):
                        t[0] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[0] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 4:
                    if t[1] == min(t):
                        t[1] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[1] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 5:
                    if t[2] == min(t):
                        t[2] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[2] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 6:
                    if t[3] == min(t):
                        t[3] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[3] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 7:
                    if t[4] == min(t):
                        t[4] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[4] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 8:
                    if t[5] == min(t):
                        t[5] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[5] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 9:
                    if t[6] == min(t):
                        t[6] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[6] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 10:
                    if t[7] == min(t):
                        t[7] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[7] == 10:
                        print('Error:1')
                    else:
                        over = True

                if button_num == 11:
                    if t[8] == min(t):
                        t[8] = 10
                        score += random.randint(9, 95)
                        points += 1
                    elif t[8] == 10:
                        print('Error:1')
                    else:
                        over = True

                pg.time.delay(300)
        else:
            pg.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))

        set_text(message, x + (self.width - width_text) // 2, y + (self.height - height_text) // 2, self.screen,
                 font_size=self.height)


def set_text(message, x, y, screen, font_color=(0, 0, 0), font_size=30):
    font_button = pg.font.Font(None, font_size)
    text = font_button.render(message, True, font_color)
    screen.blit(text, (x, y))


# Функция скрытия цифр на кнопках

def draw_block():
    global f
    Block.draw_button(coordinates[0][0], coordinates[0][1], '', None, 3)
    Block.draw_button(coordinates[1][0], coordinates[1][1], '', None, 4)
    Block.draw_button(coordinates[2][0], coordinates[2][1], '', None, 5)

    Block.draw_button(coordinates[3][0], coordinates[3][1], '', None, 6)
    Block.draw_button(coordinates[4][0], coordinates[4][1], '', None, 7)
    Block.draw_button(coordinates[5][0], coordinates[5][1], '', None, 8)

    Block.draw_button(coordinates[6][0], coordinates[6][1], '', None, 9)
    Block.draw_button(coordinates[7][0], coordinates[7][1], '', None, 10)
    Block.draw_button(coordinates[8][0], coordinates[8][1], '', None, 11)
    f = True


# Функция проверки на повторное нажатие на кнопку (не доделана)

def error_1():
    global text

    screen.fill((0, 0, 0))

    Won = 'You Won'
    text = my_font_text.render(Won, True, (255, 255, 255))
    screen.blit(text, text_rect)


# Создание объекта: кнопка

Block = Button(150, 100, screen, (247, 96, 159), (255, 0, 106))

f = False
win = False
over = False

score = 0
points = 0

# настройка текста

my_font_text = pg.font.SysFont(None, 100)
my_font_score = pg.font.SysFont(None, 50)

text = my_font_text.render('Game Over', True, (255, 255, 255))

text_rect = text.get_rect()
text_rect.center = (W // 2, H // 3)

# создание массива с не повторяющимися рандомными цифрами от 1 до 9

s = '123456789'
t = []
while s != '':
    h = random.choice(s)
    p = str(h)
    s = s.replace(p, '')
    t.append(int(h))

# Массив с рандомными координатами кнопок

coordinates = [[random.randint(75, (W // 3) - 150), random.randint(50, (H // 3) - 100)],
               [random.randint(W // 3, W - (W // 3) - 150), random.randint(50, (H // 3) - 100)],
               [random.randint(W - (W // 3), W - 150), random.randint(50, (H // 3) - 100)],
               [random.randint(75, (W // 3) - 150), random.randint((H // 3), H - (H // 3) - 100)],
               [random.randint(W // 3, W - (W // 3) - 150), random.randint((H // 3), H - (H // 3) - 100)],
               [random.randint(W - (W // 3), W - 150), random.randint((H // 3), H - (H // 3) - 100)],
               [random.randint(75, (W // 3) - 150), random.randint(H - (H // 3), H - 100)],
               [random.randint(W // 3, W - (W // 3) - 150), random.randint(H - (H // 3), H - 100)],
               [random.randint(W - (W // 3), W - 150), random.randint(H - (H // 3), H - 100)]]


# Основная функция игры

def funk():
    global win, text, f, win, over, s, t, h, p, score, points

    f = False
    win = False
    sec = False
    over = False
    gameover = False

    score = 0
    points = 0

    # создание массива с не повторяющимися рандомными цифрами от 1 до 9

    s = '123456789'
    t = []
    while s != '':
        h = random.choice(s)
        p = str(h)
        s = s.replace(p, '')
        t.append(int(h))

    screen.fill((0, 0, 0))

    # Отрисовка кнопок

    Block.draw_button(coordinates[0][0], coordinates[0][1], str(t[0]), None, 3)
    Block.draw_button(coordinates[1][0], coordinates[1][1], str(t[1]), None, 4)
    Block.draw_button(coordinates[2][0], coordinates[2][1], str(t[2]), None, 5)

    Block.draw_button(coordinates[3][0], coordinates[3][1], str(t[3]), None, 6)
    Block.draw_button(coordinates[4][0], coordinates[4][1], str(t[4]), None, 7)
    Block.draw_button(coordinates[5][0], coordinates[5][1], str(t[5]), None, 8)

    Block.draw_button(coordinates[6][0], coordinates[6][1], str(t[6]), None, 9)
    Block.draw_button(coordinates[7][0], coordinates[7][1], str(t[7]), None, 10)
    Block.draw_button(coordinates[8][0], coordinates[8][1], str(t[8]), None, 11)

    # Основной цикл игры

    while not gameover:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    screen.fill((0, 0, 0))
                    timer.cancel()
                    return

        # Запуск таймера

        while not sec:
            timer = threading.Timer(10, draw_block)
            timer.start()
            sec = True

        # После завершения таймера отрисовываются кнопки без цифр

        if f and not win:
            draw_block()

        # Проверка ситуации на выигрыш

        if points == 9 and not win:
            screen.fill((0, 0, 0))

            Won = 'You Won'
            text = my_font_text.render(Won, True, (255, 255, 255))
            screen.blit(text, text_rect)

            text2 = my_font_score.render('Score: ' + str(999), True, (255, 255, 255))
            text_rect2 = text2.get_rect()
            text_rect2.center = (W // 2 - 50, H // 3 + 100)
            screen.blit(text2, text_rect2)

            win = True

        # Проверка ситуации на проигрыш

        if over and not win:
            screen.fill((0, 0, 0))

            Won = 'Game Over'
            text = my_font_text.render(Won, True, (255, 255, 255))
            screen.blit(text, text_rect)

            text2 = my_font_score.render('Score: ' + str(score), True, (255, 255, 255))
            text_rect2 = text2.get_rect()
            text_rect2.center = (W // 2, H // 3 + 100)
            screen.blit(text2, text_rect2)

            win = True

        clock.tick(FPS)
        pg.display.flip()

    if gameover:
        pg.quit()
