import Test_pygame_project
import Window
import pygame as pg
from Test_Button import Button
from Test_pygame_project import main

Screen = Window.WindowFullScreen(120, pg.time.Clock(),
                                 pg.display.set_mode((0, 0), pg.FULLSCREEN))
pg.init()

W = Screen.window_info.current_w
H = Screen.window_info.current_h

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
button1 = Button(width_text1, height_text1, Screen.screen)
button2 = Button(width_text2, height_text2, Screen.screen)
# button1.Button(width_text1, height_text1, screen)
# button1.Button.draw_button(self=button1, x=100, y=100, message='Игра на память', font=font_text)
# button2 =Button()
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = True
    Screen.screen.fill((90, 246, 200))
    Screen.ScreenBlit(text, ((W - width_text) // 2, (H - height_text) // 2))
    button1.draw_button(W // 2 - width_text1, H//2 + height_text//2, 'Виселица', font_text, 1, done)
    button2.draw_button(W // 2, H//2 + height_text//2, 'Игра на память', font_text, 2)
    pg.display.flip()
    pg.display.update()

if done:
    pg.quit()
