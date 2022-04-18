import tkinter
import time
import random

class Rain:
    def __init__(self, x1, y1,canvas, speed):
        self.speed = speed
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + 10
        self.y2 = y1 + 10
        self.canvas = canvas
        self.id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill='Blue')
        self.t = 0

    def moving(self):
        # self.x1 = self.x1
        # self.y1 = self.y1
        self.canvas.move(self.id, self.speed)
        if c.coords(self.id)[1]>800:
            c.coords(self.id, self.x1, self.y1, self.x2, self.y2)
            self.y1 = 0
        self.t = self.speed


win = tkinter.Tk()
WIDTH = 800
HEIGHT = 800
win.geometry('{}x{}'.format(WIDTH, HEIGHT))
c = tkinter.Canvas(win, width=WIDTH, height=HEIGHT, bg='black')
c.pack()
A = Rain(random.randint(0, 700), random.randint(0, 700), c, random.randint(0, 25))
B = Rain(random.randint(0, 700), random.randint(0, 700), c, random.randint(0, 25))
C = Rain(random.randint(0, 700), random.randint(0, 700), c, random.randint(0, 25))
D = Rain(random.randint(0, 700), random.randint(0, 700), c, random.randint(0, 25))
# B = Rain(500, 0, c)
# C = Rain(350, 0, c)
# D = Rain(0, 0, c)

gameover = False
while not gameover:
    A.moving()
    B.moving()
    C.moving()
    D.moving()
    win.update()
    time.sleep(0.1)

win.mainloop()


