import report_generator
from person import Person

class PandemicControl(object):
    def __init__(self, city):
        self.__city = city
        self.__people = []
    
    @property
    def city(self):
        return self.__city
    
    def print_report(self):
        print(f"-------------For the city: [{self.__city}]-------------")
        sick_number = report_generator.get_sicks(people)
        recovered = report_generator.get_recovered(people)
        women_sick = report_generator.get_women_sick(people)
        men_sick = report_generator.get_men_sick(people)
        print(f"The number of people sick is [{sick_number}]")
        print(f"The number of people recovered is [{recovered}]")
        print(f"The number of women sick is [{women_sick}]")
        print(f"The number of men sick is [{men_sick}]")
    
    @property
    def people(self):
        return self.__people
    
    @people.setter
    def people(self, people):
        self.__people = people
    
person1 = Person("Juancito", "Pinto", 45, "Male")
person2 = Person("Juancita", "Pinto", 38, "Female")
person3 = Person("Juancho", "Pintazo", 35, "Male")
person3.is_sick = True

# Women that are sick
women1 = Person("Maria", "Del Barrio", 30, "Female")
women2 = Person("Magdalena", "Del Pilar", 43, "Female")
women3 = Person("Teresa", "De Calcuta", 28, "Female")
women4 = Person("Mon", "Laferte", 35, "Female")
women1.is_sick = True
women2.is_sick = True
women3.is_sick = True
women4.is_sick = True

# Men that are sick
man1 = Person("Enrique", "Iglesias", 45, "Male")
man2 = Person("Alejandro", "Fernandez", 39, "Male")
man3 = Person("Raymond", "Ayala", 40, "Male")
man4 = Person("Elvis", "Crespo", 24, "Male")
man1.is_sick = True
man2.is_sick = True
man3.is_sick = True
man4.is_sick = True

people = [person1, person2, person3, women1, women2, women3, women4, man1, man2, man3, man4]

p = PandemicControl("Cochabamba")
p.people = people
p.print_report()