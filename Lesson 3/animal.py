class Animal:
    def __init__(self, name):
        self.name = name

    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        print("Meow")

class Dog(Animal):
    def voice(self):
        print("Bark")

animal = Animal('?')
animal.voice()

cat = Cat('Sarah')
cat.voice()
dog = Dog('Rex')
dog.voice()