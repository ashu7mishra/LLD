from abc import ABC, abstractmethod
from enum import Enum

class Employee(ABC):

    def __init__(self, employee_id: str, employee_type: Enum, employee_name: str, call_state: Enum):
        self._employee_id = employee_id
        self._employee_type = employee_type
        self._employee_name = employee_name
        self._call_state = call_state
        self._call = None

    @abstractmethod
    def take_call(self, call):
        """Assume the employee will always successfully take the call"""
        raise NotImplementedError

    @abstractmethod
    def escalate_call(self):
        raise NotImplementedError

    @abstractmethod
    def set_employee_id(self, employee_id):
        raise NotImplementedError

    @abstractmethod
    def set_employee_name(self, employee_name):
        raise NotImplementedError


    @abstractmethod
    def set_employee_type(self, employee_type):
        raise NotImplementedError

    @abstractmethod
    def set_call_state(self, call_state):
        raise NotImplementedError

    @abstractmethod
    def get_employee_id(self):
        raise NotImplementedError

    @abstractmethod
    def get_employee_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_employee_age(self):
        raise NotImplementedError

    @abstractmethod
    def get_employee_gender(self):
        raise NotImplementedError

    @abstractmethod
    def get_employee_type(self):
        raise NotImplementedError

    @abstractmethod
    def get_call_state(self):
        raise NotImplementedError
