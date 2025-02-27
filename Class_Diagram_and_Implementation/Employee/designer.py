from Class_Diagram_and_Implementation.Employee.employee import Employee


class Designer(Employee):

    def __init__(self):
        print("designer added")

    def work(self):
        return "designer is working"
