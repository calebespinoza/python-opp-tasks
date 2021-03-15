
from ticket import Ticket
from timer import Timer
from payment import Payment

class Machine:

    def __init__(self):
        self.__ticket = Ticket()
        self.__timer = Timer()
        self.__payment = Payment(0.233333333)
        
    def register_entrance (self, car_id, time_in):
        self.__ticket.register_ticket(car_id, time_in)

    def register_exit (self, ticket, time_exit):
        self.__ticket.set_time_exit(ticket, time_exit)
    
    def print_list_cars(self):
        self.__ticket.print_all_tickets()
    
    def payment(self, car_id, time_exit):
        ticket = self.__ticket.search_ticket(car_id)
        if (ticket == None):
            return "Unregistered vehicle"
        else:
            self.register_exit(ticket, time_exit)
            self.__payment.register_payment(ticket, self.__ticket)
            return True

    def print_ticket(self):
        pass
    

machine = Machine()
machine.register_entrance(12345, "1:39:00")
machine.register_entrance(12346, "14:02:55")
machine.register_entrance(12347, "00:58:37")
#machine.register_exit(12346, "15:33:48")
#machine.register_exit(12346, "14:31:48")
#machine.print_list_cars()
print(machine.payment(12346, "15:33:48"))
machine.print_list_cars()