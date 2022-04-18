class Human:
    name = 'Илюша'

    def __init__(self, name):
        self.name = name
        print('Human')

    def can_breef(self):
        print('дышать')

    def can_talk(self):
        print('говорить')


class Doctor(Human):
    def __init__(self, age, name):
        super().__init__(name)
        self.age = age
        print('doctor')

    def can_cure(self):
        print('хил')

    def can_talk(self):
        print('больной')

    def __del__(self):
        print('----<@')

    def __str__(self):
        return '{}'.format(self.name)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return other + self.age
        if isinstance(other, Doctor):
            return self.age + other.age

    def __radd__(self, other):
        return self + other


d1 = Doctor(23, 'dima')
d2 = Doctor(45, 'Ilysha')
print(5+d1)
print(d1+6)
print(d1.age+d2.age)
print(d1+d2)


