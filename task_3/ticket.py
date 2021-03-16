
class Ticket:
    """This class performs the operations to interact with tickets
    """

    def __init__(self):
        """Ticket constructor
        """
        self.ticket = {}
        self.list_tickets = []
    
    def register_ticket(self, car_id, time_in):
        """This function creates a ticket as a dictionary, then each of then are stored in a list of tickets.

        Args:
            car_id (int): The ID of each vehicle
            time_in (string): The time when the vehice is entering to the parking.
        """
        self.ticket = { "id": car_id, "time_in": time_in, "time_exit": "", "cost": 0, "status_payment": "Unpaid"}
        self.list_tickets.append(self.ticket)
    
    def get_all_tickets(self):
        """This function returns the ticket list simply.

        Returns:
            [list]: The list of all tickets registered.
        """
        return self.list_tickets
    
    def search_ticket(self, car_id):
        """This function search a ticket by the car_id argument and then return it if it exists.

        Args:
            car_id (int): The ID of each vehicle

        Returns:
            dictionary: A ticket.
        """
        for item in self.get_all_tickets():
            if item.get("id") == car_id:
                return item
    
    def set_time_exit(self, ticket, time_exit):
        """This function updates the ticket key 'time_exit' with the hour when the vehicle is leaving the parking.

        Args:
            ticket (dictionary): The ticket that needs to be updated
            time_exit (string): The time when the vehicle is leaving the parking
        """
        ticket.update({"time_exit": time_exit})
    
    def set_cost(self, ticket, cost):
        """This function updates the ticket key 'cost'

        Args:
            ticket (dictionary): The ticket that needs to be updated
            cost (int): it represents the total cost that the vehicle's owner has to pay.
        """
        ticket.update({"cost": cost})
    
    def set_status_payment(self, ticket, status):
        """This function updates the ticket key 'status'

        Args:
            ticket (dictionary): The ticket that needs to be updated
            status (string): Set as 'Unpaid' by default, when the paid is done, it changes to 'Paid'
        """
        ticket.update({"status_payment": status})
    
    def get_time_in(self, ticket):
        """This function gets the hour when the vehicle enterd to the parking.

        Args:
            ticket (list): The ticket

        Returns:
            string: the hour when the vehicle enterd to the parking.
        """
        return ticket["time_in"]
    
    def get_time_exit(self, ticket):
        """This function gets the time of leaving.

        Args:
            ticket (list): The ticket

        Returns:
            string: the hour when the vehicle left
        """
        return ticket["time_exit"]
    
    def get_cost(self, ticket):
        """This function gets the total amount paid for being parked.

        Args:
            ticket (list): The ticket

        Returns:
            int: the total amount paid for being parked.
        """
        return ticket["cost"]
    
    def print_all_tickets(self):
        """This function print all the tickets registered
        """
        for obj in self.get_all_tickets():
            print(obj.values())
    
