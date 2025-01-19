from user import User

class Admin(User):

    def signup(self):
        print("Admin signed up")

    def login(self):
        print("Admin logged in")