class Human: #клас
    def __init__(self, age, name, gender): #конструктор класу
        self.age = age #атрибут класу
        self.name = name #атрибут класу
        self.gender = gender #атрибут класу

    def get_name(self): #метод
      return self.name

    def get_name_and_age(self):  # метод
        return self.name, self.age

human_1 = Human(age=25, name='Ana', gender='female') #екземпляри класу
print('Age=',human_1.age, 'name=',human_1.name, 'gender=',human_1.gender) #звертання до атрибуту класа
print(human_1.get_name()) #викликання методу
print(human_1.get_name_and_age()) #викликання методу