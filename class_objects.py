"""class name_class
        atribut_class
        method_class"""


class Person:
    # конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('create new class object')

obj_1 = Person("dima", 22)  # создагин обекта 1
obj_2 = Person("vika", 19)  # создагин обекта 2
obj_1.surname = 'cheban' #динамическре создание атрибута


class Person_2:
    def __init__(self,name) -> None:
        self.name = name
    def __del__(self):
        print('delete ',self.name)
def create_person():
    tom = Person_2('Tom')
create_person()
print('end program')