from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.employee import Employee
from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.employee_type import EmployeeType
from enum import Enum
from abc import ABC, abstractmethod


class Operator(Employee):

    def __init__(self, employee_id: str, employee_type: Enum, employee_name: str,
                 employee_gender: str, employee_age: int, call_state: Enum):
        super().__init__(self, employee_id, employee_name, employee_gender, employee_age)
        self._employee_type = EmployeeType.Operator

    @abstractmethod
    def call_handle(self):
        raise NotImplementedError

    @abstractmethod
    def escalate_call(self):
        raise NotImplementedError

    @abstractmethod
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    @abstractmethod
    def set_employee_name(self, employee_name):
        self._employee_name = employee_name

    @abstractmethod
    def set_employee_age(self, employee_age):
        self._employee_age = employee_age

    @abstractmethod
    def set_employee_gender(self, employee_gender):
        self._employee_gender = employee_gender

    @abstractmethod
    def set_employee_type(self, employee_type):
        self._employee_type = employee_type

    @abstractmethod
    def set_call_state(self, call_state):
        self._call_state = call_state

    @abstractmethod
    def get_employee_id(self):
        return self._employee_id

    @abstractmethod
    def get_employee_name(self):
        return self._employee_name

    @abstractmethod
    def get_employee_age(self):
        return self._employee_age

    @abstractmethod
    def get_employee_gender(self):
        return self._employee_gender

    @abstractmethod
    def get_employee_type(self):
        return self._employee_type

    @abstractmethod
    def get_call_state(self):
        return self._call_state
