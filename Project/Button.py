import pygame as pg
from pygame_project import main
from project import funk

"""import nemesis.py;"""


class Button:
    def __init__(self, width, height, screen, inactive_color=(240, 166, 148), active_color=(229, 116, 58)):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    # "рисовка" кнопки на экране

    def draw_button(self, x, y, message=None, font=None, button_num=None, done=None):
        global width_text, height_text
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if len(message) >= 1:
            font_button = pg.font.Font(None, self.height)
            text = font_button.render(message, True, self.height)
            width_text = text.get_width()
            height_text = text.get_height()

        click_button(self.height, self.width, self.inactive_color, self.active_color, self.screen, x, y, button_num)
        set_text(message, x + (self.width - width_text) // 2, y + (self.height - height_text) // 2, self.screen,
                 font_size=self.height)


def click_button(height, width, inactive_color, active_color, screen, x, y, button_num):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pg.draw.rect(screen, inactive_color, (x, y, width, height))

        # что делать после нажатия:

        if click[0] == 1:
            if button_num == 1:
                main()
            if button_num == 2:
                funk()
            pg.time.delay(300)
    else:
        pg.draw.rect(screen, active_color, (x, y, width, height))


# Задать текст который будет на кнопке

def set_text(message, x, y, screen, font_color=(0, 0, 0), font_size=30):
    font_button = pg.font.Font(None, font_size)
    text = font_button.render(message, True, font_color)
    screen.blit(text, (x, y))
