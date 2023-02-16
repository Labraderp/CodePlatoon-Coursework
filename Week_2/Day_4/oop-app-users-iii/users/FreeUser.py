from user import User

# Default attributes of User parent class:
#
# self.fname = fname
# self.lname = lname
# self.email = f'{fname}.{lname}@labraderp.dog'
# self.DL_num = DL_num
# self.premium = False
# self.post_num = 0

class FreeUser(User):
    def __init__(self, user_profile):
        self.fname = user_profile.fname
        self.lname = user_profile.lname
        self.DL_num = user_profile.DL_num
        self.email = user_profile.email
        self.premium = False
        self.post_num = 1

    def post(self, post):
        fullname = self.fname + self.lname

        if not fullname in super().post_storage:
            super().post_storage[fullname] = {}

        if self.post_num <= 2:
            super().post_storage[fullname][User.post_count] = post
            User.post_count += 1
            self.post_num += 1
            return f"{fullname}: {post}"
        else:
            return f"!!! Max post limit reached, {fullname}! Become a Premium User for more!"
            