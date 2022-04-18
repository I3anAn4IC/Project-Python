class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moving(self):
        self.x = int(input())
        self.y = int(input())

    def return_point(self):
        self.x = 0
        self.y = 0

    def show(self):
        print(self.x, self.y)

    def distance(self, another_point):
        if isinstance(another_point, Point):
            print(((self.x - another_point.x)**2 + (self.y - another_point.y)**2)**0.5)


A = Point(3, 0)
B = Point(0, 4)
A.moving()
B.moving()

A.distance(B)





