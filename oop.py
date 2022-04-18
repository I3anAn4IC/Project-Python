class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def print_account(self):
        print(self.name, self.__balance)

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_balance(self):
        return self.__balance

    balance = property(fget=get_balance, fset=set_balance)


ac1 = Account('I3an', 123)
ac1.print_account()
ac1.set_balance(int(input()))
print(ac1.name)
ac1.print_account()
# ac1.__balance = 274982
print(ac1.get_balance())
ac1.balance = 8776
print(ac1.balance)


