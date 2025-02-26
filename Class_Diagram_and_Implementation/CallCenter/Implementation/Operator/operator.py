from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.call_state import CallState
from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.employee import Employee
from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.employee_type import EmployeeType
from enum import Enum
from abc import ABC, abstractmethod


class Operator(Employee):

    def __init__(self, employee_id: str, employee_name: str):
        super().__init__(self, employee_id, employee_name)
        self._employee_type = EmployeeType.Operator

    def take_call(self, call):
        """Assume the employee will always successfully take the call"""
        self._call = call
        self._call_state = CallState.INPROGRESS
        self._employee_type = self
        self._employee = None

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
