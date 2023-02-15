import User, FreeUser, PremiumUser

#Make User Profiles
john = User.User("John", "Smith", 5555555)
saul = User.User("Saul", "Goodman", 8675309)

#Make Free Profile
john = FreeUser.FreeUser(john)

#Make Premium Profile
saul = PremiumUser.PremiumUser(saul)

#Check Premium Values
print(john.premium)     #False
print(saul.premium)     #True

#Test Post inheritance
print(john.post("Here is my first post!"))
print(saul.post("Here is my first post!"))
print(saul.post("Here is my second post!"))
print(john.post("Here is my second post!"))
print(john.post("Here is my third post!"))      #Should print non-Premium statement
print(saul.post("Here is my third post!"))

#Show Post Storage

print(john.get_posts())     #Two posts
print(saul.get_posts())     #Three posts