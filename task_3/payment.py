
from ticket import Ticket
from timer import Timer

class Payment:
    """This class performs the payment operations
    """
    def __init__(self, basic_fare_a_minute):
        """Constructor

        Args:
            basic_fare_a_minute (float): The basic fare a minute that the parking will charge
        """
        self.__basic_fare = basic_fare_a_minute
        self.__ticket = None
        self.__timer = Timer()
    
    def register_payment(self, ticket, list_tickets):
        """This functions registers a payment

        Args:
            ticket (list): The ticket
            list_tickets (object): This is the object that allows to access to the Ticket's functions
        """
        self.__ticket = list_tickets
        item = ticket
        delta_time = self.get_delta_time(item)
        total_cost = self.get_total_cost(delta_time)
        self.__ticket.set_cost(item, total_cost)
        self.__ticket.set_status_payment(item, "Paid")

    def get_delta_time(self, item):
        """This function returns the total minutes since the hour that the vehicle has entered to the parking until it is leaving

        Args:
            item (dictionary): The ticket that contains the entrance time and the exit time.

        Returns:
            date: The difference in minutes
        """
        return self.__timer.time_delta(self.__ticket.get_time_in(item), self.__ticket.get_time_exit(item))
    
    def get_total_cost(self, delta_time):
        """This function defines how much the vehicle's owner has to pay for being parked.

        Args:
            delta_time (date): the time difference in minutes

        Returns:
            float: The cost that has to be paid.
        """
        if (delta_time <= 30):
            total_cost = 30 * self.__basic_fare
        else:
            total_cost = delta_time * self.__basic_fare
        return round(total_cost, 2)