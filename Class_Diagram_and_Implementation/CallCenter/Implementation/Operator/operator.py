from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.employee import Employee
from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.employee_type import EmployeeType
from enum import Enum

class Operator(Employee):

    def __init__(self, employee_id: str, employee_type: Enum, employee_name: str,
                 employee_gender: str, employee_age: int, call_state: Enum):
        super().__init__(self, employee_id, employee_name, employee_gender, employee_age)
        self._employee_type = EmployeeType.Operator
