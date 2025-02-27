from Class_Diagram_and_Implementation.Employee.employee import Employee


class Developer(Employee):

    def __init__(self):
        print("Developer added")

    def work(self):
        return "developer is working"
