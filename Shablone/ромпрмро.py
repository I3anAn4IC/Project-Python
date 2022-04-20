class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def print_account(self):
        print(self.login, self.__email)

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        # self.__email = new_email
        j = int(0)
        h = int(0)
        for i in range(len(new_email)):
            if new_email[i] == '@':
                l = int(i)
                for l in range(len(new_email)):
                    if new_email[l] == '.':
                        h += 1
                j += 1
        if (j > 1 or j < 1) or (h < 1 or h > 1):
            print('Error')
        else:
            self.__email = new_email


k = UserMail('I3an', 'I3an@gmail.com')
print(k.get_email())
k.set_email(input())
k.set_email(input())
k.set_email(input())
print(k.get_email())
