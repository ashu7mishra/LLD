from Class_Diagram_and_Implementation.Employee.developer import Developer
from Class_Diagram_and_Implementation.Employee.manager import Manager

if __name__ == "__main__":

    manager = Manager()
    dev = Developer()
    manager.add_employee(dev)
    manager.working()