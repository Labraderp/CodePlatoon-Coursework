# your improved User class goes here

class User():
    post_storage = {}
    post_count = 0

    def __init__(self, fname, lname, DL_num):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@labraderp.dog'
        self.DL_num = DL_num
    
    def post(self, post):
        fullname = self.fname + self.lname
        if not fullname in User.post_storage:
            User.post_storage[fullname] = {}
        User.post_storage[fullname][User.post_count] = post
        User.post_count += 1
        print(User.post_storage)
        return f"{fullname}: {post}"
        
    def get_posts(self):
        return User.post_storage[self.fname + self.lname]
    
john = User('John', 'Denver', 902100904)
saul = User('Saul', 'Goodman', 8675309)

print(john.post("Hello, world!"))
print(saul.post("Goodbye, world!"))
print(john.post("Help me, world!"))

print(john.get_posts())