from user import User


class TAs(User):

    def signup(self):
        print("TA sign up")

    def login(self):
        print("TA logged in")



ta = TAs()
ta.signup()
ta.login()