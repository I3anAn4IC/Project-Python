import pygame as pg
import random

screen = pg.display.set_mode((640, 480))
HANG_MAN_PICS = ['smile02.png']


def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def display_board(HANG_MAN_PICS, missed_letters, correct_letters, secret_word, font):
    picture = pg.image.load(HANG_MAN_PICS[len(missed_letters)])
    picture_rect = picture.get_rect()
    screen.blit(picture, (100, 200))


def main():
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    words = 'муравей бабуин барсук медведь бобр верблюд'.split()
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)

    while not done:
        display_board(HANG_MAN_PICS, missed_letters, correct_letters, secret_word, font)

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
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pg.draw.rect(screen, color, input_box, 2)
        display_board(HANG_MAN_PICS, missed_letters, correct_letters, secret_word, font)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
