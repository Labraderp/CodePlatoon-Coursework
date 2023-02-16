from person import Person

class Staff(Person):
    def __init__(self):
        self.name = Person.name 
        self.age = Person.age         
        self.password = Person.password
        self.role = Person.role
        self.employee_id = Person.id