class Employer:

    def __init__(self,name) -> None:
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    def work(self):
        print(f'{self.name} works')
    
class Student:

    def __init__(self,name) -> None:
        self.__name= name
    
    @property
    def name(self):
        return self.__name
    
    def study(self):
        print(f'{self.name} studies')
class WorkingStudent(Employer,Student):
    pass

obj = WorkingStudent('RandomName')
obj.work()
obj.study()