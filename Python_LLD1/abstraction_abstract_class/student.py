from user import User


class Student(User):

    def signup(self):
        print("A new student signed up")

    def login(self):
        print("Student logged in")