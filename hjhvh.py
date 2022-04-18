class NewInt(int):
    def __init__(self, number, n=2):
        self.n = n
        self.number = number

    def repeat(self, n=2):
        self.n = n
        h = self.number
        c = len(str(self.number))
        for i in range(1, self.n):
            h = h * (10 ** c) + self.number
        return h

    def to_bin(self):
        s = bin(self.number)
        s = s[2:]
        return s


a = NewInt(15)
print(a.repeat(5))
d = NewInt(a + 5)
print(d.repeat(3))
b = NewInt(NewInt(7)*NewInt(5))
print(b.to_bin())

