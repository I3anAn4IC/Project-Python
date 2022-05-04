import pygame as pg
import random
import Window

# screen = Window.WindowFullScreen(FPS=120, clock=pg.time.Clock(), screen=pg.display.set_mode((0, 0), pg.FULLSCREEN),
#                                  gameover=False, window_info=None)

# screen.Screen()
HANG_MAN_PICS = ['Sprites/1.jpg', 'Sprites/2.jpg', 'Sprites/3.jpg', 'Sprites/4.jpg', 'Sprites/5.jpg', 'Sprites/6.jpg',
                 'Sprites/7.jpg', 'Sprites/8.jpg', 'Sprites/9.jpg']
missed_letters = ''
correct_letters = ''
text1 = ' '
GAME_IS_ON = True

Screen = Window.WindowFullScreen(120, pg.time.Clock(),
                                 pg.display.set_mode((0, 0), pg.FULLSCREEN))
pg.init()

W = Screen.window_info.current_w
H = Screen.window_info.current_h
# W = 1920
# H = 1080
MIN = min(H, W) - 200
MAX = max(H, W)
# screen = pg.display.set_mode((W, H))
# устанавливаем размер шрифта
FONT_SIZE = MIN // 16
# вводим значения для координат текста с правильностью ввода
coordinates_text_letter = (10, MIN + FONT_SIZE, MIN, FONT_SIZE)
print(W, H)


def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


words = 'муравей бабуин барсук медведь бобр верблюд'.split()
secret_word = get_random_word(words)


def display_board(font):
    # выводим на экран картинку
    global GAME_IS_ON
    blank = '*' * len(secret_word)

    if len(missed_letters) < 16:
        if len(missed_letters) == 0:
            picture = pg.image.load(HANG_MAN_PICS[len(missed_letters)])
        else:
            picture = pg.image.load(HANG_MAN_PICS[len(missed_letters) - len(missed_letters) // 2])
        picture_rect = picture.get_rect()
        picture = pg.transform.scale(picture, (MIN, MIN))
        Screen.ScreenBlit(picture, (0, 0))
    else:
        picture = pg.image.load(HANG_MAN_PICS[len(missed_letters) - len(missed_letters) // 2])
        Screen.ScreenBlit(picture, (0, 0))
        GAME_IS_ON = False
        for i in range(len(secret_word)):
            if secret_word[i] in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
                blank = blank[:i] + secret_word[i] + blank[i + 1:]
        # размещение "звездочек"
        blank_font = font.render(blank, True, (133, 100, 8))
        Screen.ScreenBlit(blank_font, (10, MIN))
    # picture_rect = picture.get_rect()
    # screen.blit(picture, (100, 200))
    # выводим на экран список неправильных букв
    text_missed_letters = font.render('Неправильные буквы:' + missed_letters, True, (133, 100, 8))
    Screen.ScreenBlit(text_missed_letters, (MIN, 10))

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blank = blank[:i] + secret_word[i] + blank[i + 1:]
    blank_font = font.render(blank, True, (133, 100, 8))
    Screen.ScreenBlit(blank_font, (10, MIN))
    if blank.find('*') == -1:
        GAME_IS_ON = False


def check_letters(letter, font):
    global correct_letters, missed_letters, text1
    text_letter = font.render('', True, (133, 100, 8))
    Screen.ScreenBlit(text_letter, coordinates_text_letter)
    if len(letter) > 1:
        text_letter = font.render('Введите одну букву кириллицы', True, (133, 100, 8))
        Screen.ScreenBlit(text_letter, coordinates_text_letter)
    elif (letter in missed_letters or letter in correct_letters) and len(letter) != 0:
        text_letter = font.render('Эту букву вы уже вводили', True, (133, 100, 8))
        Screen.ScreenBlit(text_letter, coordinates_text_letter)
    elif letter not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
        text_letter = font.render('Введите букву кириллицы', True, (133, 100, 8))
        Screen.ScreenBlit(text_letter, coordinates_text_letter)
    else:
        if letter in secret_word:
            correct_letters = correct_letters + letter
            text1 = ''
        else:
            missed_letters = missed_letters + letter + ' '
            text1 = ''
        text_letter = font.render('Введите одну букву кириллицы', True, (133, 100, 8))
        Screen.ScreenBlit(text_letter, coordinates_text_letter)


def main():
    global text1
    font = pg.font.Font(None, FONT_SIZE)
    clock = Screen.clock
    input_box = pg.Rect(10, MIN + 2 * FONT_SIZE, 140, FONT_SIZE)
    color_inactive = pg.Color('lightskyblue2')
    color_active = pg.Color('dodgerblue3')
    color = color_inactive
    active = False
    text = ''
    text1 = text
    done = False

    while not done:
        display_board(font)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    Screen.screen.fill((0, 0, 0))
                    return
                if active and GAME_IS_ON:
                    if event.key == pg.K_RETURN:
                        text1 = text
                        text = ''
                        print(text)
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        Screen.screen.fill((255, 255, 255))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        Screen.ScreenBlit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pg.draw.rect(Screen.screen, color, input_box, 2)
        display_board(font)
        check_letters(text1, font)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
