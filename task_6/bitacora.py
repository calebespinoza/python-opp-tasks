class Bitacora(object):
    def __init__(self):
        self.__people_sick = []
        self.__people_recovered = []
        self.__people_healthy = []
    
    def add_sick_person(self, person):
        self.__people_sick.append(person)

    def add_recovered_person(self, person):
        self.__people_recovered.append(person)

    def add_healthy_person(self, person):
        self.__people_sick.append(person)
    
    #def remove_sick_person(self, person):
    #    self.__people_sick.remove(person)
    
    @property
    def people_sick(self):
        return self.__people_sick
    
    @property
    def people_recovered(self):
        return self.__people_recovered
    
    @property
    def people_healthy(self):
        return self.__people_healthy
