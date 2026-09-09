# Job class responsible for jobs objects

class Job:
    def __init__(self, id, customer):
        self.id = id
        self.customer = customer
        self.status = "pending"
        self.attempts = 0
        self.result = None

    def show_job(self):
        print(f"id {self.id} status {self.status} attempts {self.attempts} result {self.result}")
        print(f"customer data {self.customer.name} {self.customer.is_active}")

    def start(self):
        if self.status == 'pending':
            self.status = 'running'
            self.attempts += 1
        else:
            print(f"Job status is not pending, hence not starting it {self.status}")
            return False
        
        return True