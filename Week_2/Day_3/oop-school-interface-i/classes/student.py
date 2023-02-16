from person import Person

class Student(Person):
    def __init__(self):
        self.name = Person.name 
        self.age = Person.age         
        self.password = Person.password
        self.role = Person.role
        self.school_id = Person.id