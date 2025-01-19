from user import User


class Instructor(User):

    def signup(self):
        print("A new Instructor signed up")

    def login(self):
        print("Instructor logged in")