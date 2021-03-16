
from ticket import Ticket
from timer import Timer
from payment import Payment

class Machine:
    """This class offers funcionalities to register the entrance, exit and payments when someone wants to park a vehicle.
    """
    
    def __init__(self):
        """Machine constructor
        """
        self.__ticket = Ticket()
        self.__timer = Timer()
        self.__payment = Payment(0.233333333)
        
    def register_entrance (self, car_id, time_in):
        """This function calls the register_ticket function to create a new ticket
    
        Args:
            car_id (int): This is the ID of each vehicle (Placa).
            time_in (string): This is the time when the vehicle enter to the parking.
        """
        self.__ticket.register_ticket(car_id, time_in)
    
    def register_exit (self, ticket, time_exit):
        """This function register the time when a vehicle is leaving the parking
    
        Args:
            ticket (dictionary): This argument contains the info of the vehicle.
            time_exit (string): This argument is the time when the vehicle is leaving.
        """
        self.__ticket.set_time_exit(ticket, time_exit)
    
    def print_list_cars(self):
        """This functions prints all tickets created.
        """
        self.__ticket.print_all_tickets()
    
    def payment(self, car_id, time_exit):
        """This function calls to the register_exit, payment and print_ticket functions
        """
        ticket = self.__ticket.search_ticket(car_id)
        if (ticket == None):
            self.print_ticket(ticket)
        else:
            self.register_exit(ticket, time_exit)
            self.__payment.register_payment(ticket, self.__ticket)
            self.print_ticket(ticket)

    def print_ticket(self, ticket):
        """This function prints two differente tickets
        When not registered it prints: Unregistered Vehicle
        if exists, it prints the ticket in detail.
        """
        if (ticket == None):
            text = """
            ----------------------------
                Unregistered vehicle
            ----------------------------
            """
        else:
            today = self.__timer.get_date_today()
            text = """
            ----------------------------
                    PAID PARKING        
            ----------------------------
            Date: {0}
            From: {1}
            To: {2}
            Paid: Bs. {3}
            ----------------------------
            Thank you and lucky road!
            ----------------------------
            """.format(today, self.__ticket.get_time_in(ticket), self.__ticket.get_time_exit(ticket), self.__ticket.get_cost(ticket))
        print(text)
