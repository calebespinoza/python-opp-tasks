
class Ticket:

    def __init__(self):
        self.ticket = {}
        self.list_tickets = []
    
    def register_ticket(self, car_id, time_in):
        self.ticket = { "id": car_id, "time_in": time_in, "time_exit": "", "cost": 0, "status_payment": "Unpaid"}
        self.list_tickets.append(self.ticket)
    
    def get_all_tickets(self):
        return self.list_tickets
    
    def search_ticket(self, car_id):
        for item in self.get_all_tickets():
            if item.get("id") == car_id:
                return item
    
    def set_time_exit(self, ticket, time_exit):
        ticket.update({"time_exit": time_exit})
    
    def set_cost(self, ticket, cost):
        ticket.update({"cost": cost})
    
    def set_status_payment(self, ticket, status):
        ticket.update({"status_payment": status})
    
    def get_time_in(self, ticket):
        return ticket["time_in"]
    
    def get_time_exit(self, ticket):
        return ticket["time_exit"]
    
    def get_cost(self, ticket):
        return ticket["cost"]
    
    def print_all_tickets(self):
        for obj in self.get_all_tickets():
            print(obj.values())
    
