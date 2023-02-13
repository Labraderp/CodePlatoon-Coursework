# your User class goes here

class User():
    def __init__(self, fname, lname, DL_num):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@labraderp.dog'
        self.DL_num = DL_num

john = User('John', 'Denver', 902100904)
saul = User('Saul', 'Goodman', 8675309)

print(john.fname)
print(saul.DL_num)