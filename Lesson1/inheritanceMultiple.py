class Doctor:
    def can_cure(self): #метод класу
        print('Я лікар, я вмію лікувати')

    def can_build(self): #метод класу
        print('Я лікар, я трохи вмію будувати')

class Architect:
    def can_build(self): #метод класу
        print('Я архітектор, я вмію будувати')

class Person(Doctor, Architect): #дочірній клас, який має двох батьків
    pass #заповнювач кода, щоб не було помилки, якщо кода немає
    #def can_build(self): #метод класу
        #print('Я людина, я теж вмію будувати') #метод батьківського класу із змінами

s = Person() #екземпляр класа Person
print(s.can_cure()) #викликання методу батьківського класу Doctor
print(s.can_build()) #викликання методу батьківського класу Architect
print(Person.__mro__) #виведення порядок пошуку методів в класах