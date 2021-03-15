
from ticket import Ticket
from timer import Timer

class Payment:
    def __init__(self, basic_fare_a_minute):
        self.__basic_fare = basic_fare_a_minute
        self.__ticket = None
        self.__timer = Timer()
    
    def register_payment(self, ticket, list_tickets):
        self.__ticket = list_tickets
        item = ticket
        delta_time = self.get_delta_time(item)
        total_cost = self.get_total_cost(delta_time)
        self.__ticket.set_cost(item, total_cost)
        self.__ticket.set_status_payment(item, "Paid")

    def get_delta_time(self, item):
        return self.__timer.time_delta(self.__ticket.get_time_in(item), self.__ticket.get_time_exit(item))
    
    def get_total_cost(self, delta_time):
        if (delta_time <= 30):
            total_cost = 30 * self.__basic_fare
        else:
            total_cost = delta_time * self.__basic_fare
        return round(total_cost, 2)