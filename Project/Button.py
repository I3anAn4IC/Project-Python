import pygame as pg
from pygame_project import main
from project import funk

"""import nemesis.py;"""


# screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)


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
        # width_text, height_text = font.size(message)
        if len(message) >= 1:
            font_button = pg.font.Font(None, self.height)
            text = font_button.render(message, True, self.height)
            width_text = text.get_width()
            height_text = text.get_height()
        # screen.blit(text, (x + width_text, y+ height_text))
        # set_text(message, x + 10, y, self.screen,
        #          font_size=self.height)
        # print(width_text, height_text)
        # if message:
        #     font_button = pg.font.Font(None, self.height)
        #     text = font_button.render(message, True, self.height)
        #     width_text = text.get_width()
        #     print(width_text)
        #     screen.blit(text, (x, y))

        click_button(self.height, self.width, self.inactive_color, self.active_color, self.screen, x, y, button_num)
        # if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
        #     pg.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
        #     # что делать после нажатия:
        #     if click[0] == 1:
        #         if button_num == 1:
        #             main()
        #         pg.time.delay(300)
        # else:
        #     pg.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))
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
    # def click(self, x, y, win_open):
    #     mouse = pg.mouse.get_pos()
    #     click = pg.mouse.get_pressed()
    #     if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
    #         pg.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
    #         # что делать после нажатия:
    #         if click[0] == 1:
    #             win_open
    #             pg.time.delay(300)
    #     else:
    #         pg.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))
    # Задать текст который будет на кнопке


def set_text(message, x, y, screen, font_color=(0, 0, 0), font_size=30):
    font_button = pg.font.Font(None, font_size)
    text = font_button.render(message, True, font_color)
    # print(width_text)
    screen.blit(text, (x, y))

# def main():
#     font = pg.font.Font(None, 32)
#     clock = pg.time.Clock()
#     input_box = pg.Rect(100, 100, 140, 32)
#     color_inactive = pg.Color('lightskyblue3')
#     color_active = pg.Color('dodgerblue2')
#     color = color_inactive
#     active = False
#     text = ''
#     done = False
#     button = Button(700, 100, screen)
#
#     while not done:
#
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 if input_box.collidepoint(event.pos):
#                     active = not active
#                 else:
#                     active = False
#                 color = color_active if active else color_inactive
#             if event.type == pg.KEYDOWN:
#                 if active:
#                     if event.key == pg.K_RETURN:
#                         print(text)
#                         text = ''
#                     elif event.key == pg.K_BACKSPACE:
#                         text = text[:-1]
#                     else:
#                         text += event.unicode
#
#         screen.fill((30, 30, 30))
#         txt_surface = font.render(text, True, color)
#         width = max(200, txt_surface.get_width() + 10)
#         input_box.w = width
#         button.draw_button(30, 60, 'WOW', font)
#         # width1, height = font.size(text)
#         # print(text)
#         # print(width1, height)
#         screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
#         pg.draw.rect(screen, color, input_box, 2)
#
#         pg.display.flip()
#         clock.tick(30)
#
#
# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()
