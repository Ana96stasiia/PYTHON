class Cat:
    def __init__(self, size, color, cat_type): #конструктор
        self.size = size #атрибут класу
        self.color = color #атрибут класу
        self.cat_type = cat_type #атрибут класу

    def set_size(self): #метод
        if self.cat_type == 'indoor': #умова
            self.size='small'

    def set_size(self): #метод
        if self.cat_type == 'indoor': #умова
            self.size='small'

cat_1 = Cat(size='', color='white', cat_type='indoor') #екземпляр класу
cat_1.set_size()
print('size=', cat_1.size, 'color=', cat_1.color, 'cat_type=', cat_1.cat_type)


