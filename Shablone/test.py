import tkinter as tk
import time
import math


class Planet:
    def __init__(self, canvas, priod, radius_orbit, size, color):
        self.canvas = canvas
        self.period = priod
        self.color = color
        self.radius_orbit = radius_orbit
        self.size = size
        self.x1 = self.radius_orbit
        self.y1 = 0
        self.x2 = self.radius_orbit + 2 * self.size
        self.y2 = 0 + 2 * self.size
        self.id = self.canvas.create_oval(self.x1 + sdvig - self.size,
                                          self.y1 + sdvig - self.size,
                                          self.x2 + sdvig - self.size,
                                          self.y2 + sdvig - self.size,
                                          fill=self.color)
        self.t = 0

    def move_planet(self):
        self.x2 = self.radius_orbit * math.cos(math.radians(self.t))
        self.y2 = self.radius_orbit * math.sin(math.radians(self.t))
        self.canvas.move(self.id, self.x2 - self.x1, self.y2 - self.y1)
        self.x1 = self.x2
        self.y1 = self.y2
        self.t = self.period


def circle(r):
    sdvig = 400
    x1 = r
    y1 = 0
    for t in range(361):
        x2 = r * math.cos(math.radians(t))
        y2 = r * math.sin(math.radians(t))
        c.create_line(x1 + sdvig, y1 + sdvig, x2 + sdvig, y2 + sdvig)
        x1 = x2
        y1 = y2


win = tk.Tk()
WIDTH = 800
HEIGHT = 800
win.geometry('{}x{}'.format(WIDTH, HEIGHT))
win.title('солнечная система')
c = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg='#5080ff')
c.pack()
sdvig = WIDTH // 2
sun = c.create_oval(sdvig - 25, sdvig - 25, sdvig + 25, sdvig + 25, fill='yellow', outline='yellow')
circle(100)
circle(200)
# ------первая планета
t1 = 0
r_orbit_p1 = 200
size_p1 = 10
x1_p1 = r_orbit_p1
y1_p1 = 0
x2_p1 = r_orbit_p1 + 2 * size_p1
y2_p1 = 0 + 2 * size_p1
p1 = c.create_oval(x1_p1 + sdvig - size_p1, y1_p1 + sdvig - size_p1, x2_p1 + sdvig - size_p1, y2_p1 + sdvig - size_p1,
                   fill='red', outline='red')
# --------------------
# ------вторая планета
t2 = 0
r_orbit_p2 = 100
size_p2 = 7
x1_p2 = r_orbit_p2
y1_p2 = 0
x2_p2 = r_orbit_p2 + 2 * size_p2
y2_p2 = 0 + 2 * size_p2
p2 = c.create_oval(x1_p2 + sdvig - size_p2, y1_p2 + sdvig - size_p2, x2_p2 + sdvig - size_p2, y2_p2 + sdvig - size_p2,
                   fill='blue', outline='blue')
# --------------------
earth = Planet(c, 1, 150, 12, 'blue')
jupiter = Planet(c, 1, 250, 17, 'brown')
gameover = False
while not gameover:
    # --------первая планета. движение
    x2_p1 = r_orbit_p1 * math.cos(math.radians(t1))
    y2_p1 = r_orbit_p1 * math.sin(math.radians(t1))
    c.move(p1, x2_p1 - x1_p1, y2_p1 - y1_p1)
    x1_p1 = x2_p1
    y1_p1 = y2_p1
    t1 += 1
    t1 %= 360
    # --------------------------------
    # --------вторая планета. движение
    x2_p2 = r_orbit_p2 * math.cos(math.radians(t2))
    y2_p2 = r_orbit_p2 * math.sin(math.radians(t2))
    c.move(p2, x2_p2 - x1_p2, y2_p2 - y1_p2)
    x1_p2 = x2_p2
    y1_p2 = y2_p2
    t2 += 1.3
    t2 %= 360
    # --------------------------------
    earth.move_planet()
    win.update()
    time.sleep(0.01)

win.mainloop()
