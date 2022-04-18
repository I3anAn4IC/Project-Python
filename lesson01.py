class Cat:
    def __init__(self, name='Archibald', age=0, breed='pers', color='grey', sex=0):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.sex = sex

    def say(self):
        self.age += 2
        print('Мяу', self.name, self.breed, self.age)

    def meeting(self, another_cat):
        if isinstance(another_cat, Cat):
            if self.sex == another_cat.sex:
                print('Драка')
            else:
                print('Любовь')
        else:
            print('это не котики')


tom = Cat('Tom', 2, 'Sfinx', 'grey', 1)
murka = Cat('Murka', 2, 'Sfinx', 'grey', 0)
matroskin = Cat('Matroskin', 2, 'Sfinx', 'grey', 1)
garfild = Cat()
tom.meeting(murka)
tom.meeting(matroskin)
tom.meeting(45)
