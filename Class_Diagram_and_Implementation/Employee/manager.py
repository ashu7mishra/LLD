class Manager:

    def __init__(self):
        self.employee = []

    def add_employee(self, employee):
        self.employee.append(employee)

    def working(self):
        for employee in self.employee:
            print(employee.work())