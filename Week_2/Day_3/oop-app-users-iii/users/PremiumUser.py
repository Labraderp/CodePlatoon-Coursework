# Your PremiumUser class goes here
import User


# Default attributes of User parent class:
#
# self.fname = fname
# self.lname = lname
# self.email = f'{fname}.{lname}@labraderp.dog'
# self.DL_num = DL_num
# self.premium = False
# self.post_num = 0


class PremiumUser(User.User):
    def __init__(self, user_profile):
        self.fname = user_profile.fname
        self.lname = user_profile.lname
        self.DL_num = user_profile.DL_num
        self.email = user_profile.email
        self.premium = True