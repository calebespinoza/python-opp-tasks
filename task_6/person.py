class Person(object):
    def __init__(self, name, lastname, age, gender):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__gender = gender
        self.__is_sick = False
    
    @property
    def name(self):
        return self.__name
    
    @property
    def lastname(self):
        return self.__lastname
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def is_sick(self):
        return self.__is_sick
    
    @is_sick.setter
    def is_sick(self, is_sick):
        self.__is_sick = is_sick