class BankAccount:
    def __init__(self, name, balance): #конструктор класу
        self.name = name #атрибут класу
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('only number!!!')
        self.__balance = value

    def del_balance(self):
        print('delete balance')
        del self.balance

    balance = property(fget=get_balance, fset=set_balance)

a = BankAccount('John', 10000) #екземпляр класу
print(a.balance)
#b = BankAccount('Ana', 500)
# print(a.name) #виведення значення атрибуту класу
# a.balance = 'Your balance is empty' #зміна значення балансу
# print(a.balance) #виведення балансу
# print(a.get_balance())
# a.set_balance(200)
# print(a.get_balance())





