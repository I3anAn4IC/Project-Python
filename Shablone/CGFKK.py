class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return '{}'.format("Тип транспорта ",
        self.kind, "марки ",
        self.brand, "может развить скорость",
        self.max_speed, "км/ч.")

    class Car(Transport):
        def __init__(self, brand, max_speed, mileage, gasoline_residue, kind="car"):
            super().__init__(brand, max_speed)
            self.mileage = mileage
            self.__gasoline_residue = gasoline_residue

    class Plane(Transport):
        pass

    class Boat(Transport):
        pass

    a = Transport("df", 34)
    print(a)
