
from datetime import datetime

class Car:

    __FMT = '%H:%M:%S'

    def __init__(self):
        self.car_id = 0
        self.time_in = ""
        self.time_out = ""
        self.dict_cars = {}
        self.list_cars = []
    
    def register_car(self, car_id, time_in):
        self.dict_cars = { "id": car_id, "time_in": time_in, "time_out": ""}
        self.list_cars.append(self.dict_cars)
    
    def get_all_cars(self):
        return self.list_cars
    
    def search_car(self, car_id):
        for item in self.list_cars:
            if item.get("id") == car_id:
                return item
    
    def set_time_out(self, car_id, time_out):
        car = self.search_car(car_id)
        car.update({"time_out": time_out})
    
    def print_all_cars(self):
        for obj in self.list_cars:
            print(obj.values())

#car = Car()
#car.register_car(12345, "1:21:10")
#car.register_car(12346, "12:21:10")
#car.register_car(12347, "13:21:10")
#car.set_time_out(12347, "14:15:32")
#car.set_time_out(12345, "2:30:18")
#car.search_car(12347)
#car.print_all_cars()