from datetime import datetime
import time

class Machine:
    def __init__(self):
        self.car_id = ""
        self.time_in = ""
        self.time_out = ""
        self.fare = ""
        self.ticket_status = "Unpaid"
    
    def register_entrance (self, car_id, time_in):
        self.car_id = car_id
        self.time_in = time_in

    def register_exit (self, car_id, time_out):
        self.time_out = time_out

    def calculate_time(self):
        FMT = '%H:%M:%S'
        return datetime.strptime(self.time_out, FMT) - datetime.strptime(self.time_in, FMT)

    def get_fare (self):
        print (self.calculate_time())
    
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
machine.register_entrance(12345, "01:21:10")
machine.register_exit(12345, "01:53:02")
machine.get_fare()
#machine.print_car_id()