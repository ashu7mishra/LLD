class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def displayInfo(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")

    def getUsername(self):
        # Todo : Implement this method

    def getEmail(self):
        # Todo : Implement this method


class Student(User):
    def __init__(self, username, email, studentId, course):
        super().__init__(username, email)
        self._studentId = studentId
        self._course = course

    def displayInfo(self):
        super().displayInfo()
        print(f"Student ID: {self._studentId}")
        print(f"Course: {self._course}")

    def getStudentId(self):
       # Todo : Implement this method

    def getCourse(self):
        # Todo : Implement this method


class Employee(User):
    def __init__(self, username, email, employeeId, department):
        super().__init__(username, email)
        self._employeeId = employeeId
        self._department = department

    def displayInfo(self):
        #Todo: Implement this method

    def getEmployeeId(self):
        # Todo : Implement this method

    def getDepartment(self):
        # Todo : Implement this method
