# Customer class with customer details

class Customer:

    def __init__(self, id, name, email, is_active):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active
    
    def show_customer(self):
        print(f"id {self.id}, name {self.name}, email {self.email}, is_active {self.is_active}")
    
