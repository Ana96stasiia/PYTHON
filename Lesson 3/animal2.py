class Animal2:
    def __init__(self, name):
        self._name = name

    def voice(self):
        if self._name == 'cat':
            print('Meow')
        elif self._name == "dog":
            print('Bark')
        else:
            print("...")

a1 = Animal2('cat')
a2 = Animal2('dog')
a3 = Animal2('dinosaur')
a1.voice()
a2.voice()
a3.voice()



