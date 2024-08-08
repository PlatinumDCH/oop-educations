'''синтакисс наследование класов
    class   название_подкласса (имя_суперкласса)
        методы_подкласса'''

class Person:
    def __init__(self,name) -> None:
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    def display_info(self):
        print(f'name: {self.__name}')
class Employer(Person):
    def work(self):
        print(f'{self.name} works')

obj = Employer('Random_name')
print(obj.name)
obj.display_info()
obj.work()       