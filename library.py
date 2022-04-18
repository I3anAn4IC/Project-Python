def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


class Cat:
    def __init__(self, name='Myrka', age=0):
        self.name = name
        self.age = age
