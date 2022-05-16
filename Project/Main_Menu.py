import pygame as pg
from Button import Button

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.init()

W = pg.display.Info().current_w
H = pg.display.Info().current_h

MIN = min(H, W) - 200
FONT_SIZE = MIN // 16

font_text = pg.font.Font(None, FONT_SIZE)
text = font_text.render('Во что вы хотите сыграть?', True, (0, 0, 0))
width_text = text.get_width()
height_text = text.get_height()


text1 = font_text.render('Игра Виселица', True, (255, 255, 255))
width_text1 = text1.get_width()
height_text1 = text1.get_height()

text2 = font_text.render('Игра на памят', True, (255, 255, 255))
width_text2 = text2.get_width()
height_text2 = text2.get_height()

print(height_text1, height_text2)
button1 = Button(width_text1, height_text1, screen)
button2 = Button(width_text2, height_text2, screen)
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = True

    screen.fill((90, 246, 200))
    screen.blit(text, ((W - width_text) // 2, (H - height_text)//2))

    button1.draw_button(W // 2 - width_text1, H//2 + height_text//2, 'Виселица', font_text, 1, done)
    button2.draw_button(W // 2, H//2 + height_text//2, 'Игра на память', font_text, 2)

    pg.display.flip()
    pg.display.update()

if done:
    pg.quit()
