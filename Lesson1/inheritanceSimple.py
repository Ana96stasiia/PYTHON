class Human:
    def __init__(self, age): #конструктор класу
        self.age = age #атрибут класу

    def say_hello(self): #метод класу
        print('Hello, I am {}'.format(self.age))

class HumanExtended(Human): #дочірній клас Human
    def __init__(self, age, name):
        super().__init__(age) #викликання конструктору батьківського класу super
        self.name = name

    def say_hello(self): #метод класу
        print('Hello, I am {} and I am {}'.format(self.name, self.age)) #метод батьківського класу з доповненням

human = Human(age=50) #екземпляр класу
human.say_hello() #викликання методу
human2 = HumanExtended(age=30, name='Erica') #екземпляр дочірнього класу
human2.say_hello() #викликання методу