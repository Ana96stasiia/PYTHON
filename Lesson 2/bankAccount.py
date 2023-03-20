class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name #атрибут класу
        self.__balance = balance
        self.__passport = passport

    #def print_data(self): #metod
       # print(self.name, self.balance, self.passport)

    def print_protected_data(self):  # metod
        print(self._name, self._balance, self._passport)

    def print_private_data(self):  # metod
        print(self.__name, self.__balance, self.__passport)

account1=BankAccount('Kolya', 5000, 'cr7567458') #екземпляр класу
# account1.print_private_data() #викликання методу
# print(account1._name)  #звертання до атрибуту класу
# print(account1._balance)
# print(account1._passport)
#print(dir(account1))
print(account1._BankAccount__balance)
