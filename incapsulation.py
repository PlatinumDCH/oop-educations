class Person:
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age

    @property
    def age(self):
        """геттер для получения возраста"""
        return self.__age
    
    @age.setter
    def age(self,age):
        if 0<age<110:
            self.__age = age
        else:
            print('uncorect input')
 
    @property
    def get_name(self):
        '''геттер для получения имени'''
        return self.__name
    
    def print_person(self):
        print('name =',self.__name,', age =',self.__age)

dima = Person('dima',10)
