from datetime import datetime
from car import Car
import time

class Machine:
    __FMT = '%H:%M:%S'

    def __init__(self):
        self.car_id = ""
        self.time_in = ""
        self.time_out = ""
        self.fare = ""
        self.ticket_status = "Unpaid"
        self.__car = Car()
        
    def register_entrance (self, car_id, time_in):
        self.__car.register_car(car_id, time_in)

    def print_list_cars(self):
        self.__car.print_all_cars()

    def register_exit (self, car_id, time_out):
        self.__car.set_time_out(car_id, time_out)

    ## TIMER

    def calculate_time(self):
        #return datetime.strptime(self.time_out, FMT) - datetime.strptime(self.time_in, FMT)
        return self.time_out - self.time_in

    def get_fare (self):
        time_delta = self.calculate_time()
        minutes = time_delta.total_seconds() / 60
        print (time_delta)
        print (minutes)

    ## TIMER
    
    def register_payment(self):
        self.ticket_status = "Paid"

    def print_ticket(self):
        if (self.ticket_status == "Paid"):
            print("Ticket")
        else:
            print("You didn't pay the fare.")
    
    def print_car_id(self):
        #return self.car_id
        print(self.car_id)

    def get_time(self):
        ts = time.time()
        print(ts)
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S') #('%d-%m-%Y %H:%M:%S')
        print(st)

machine = Machine()
machine.register_entrance(12345, "1:39:00")
machine.register_entrance(12346, "14:02:55")
machine.register_entrance(12347, "00:58:37")
machine.register_exit(12346, "15:33:48")
machine.print_list_cars()
#machine.register_exit(12345, "1:53:10")
#machine.get_fare()
#machine.print_car_id()