from abc import ABC, abstractmethod
from enum import Enum

class Employee(ABC):

    def __init__(self, employee_id: str, employee_type: Enum, employee_name: str,
                 employee_gender: str, employee_age: int, call_state: Enum):
        self._employee_id = employee_id
        self._employee_type = employee_type
        self._employee_name = employee_name
        self._employee_gender = employee_gender
        self._employee_age = employee_age
        self._call_state = call_state

    @abstractmethod
    def call_handle(self):
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
    def set_employee_age(self, employee_age):
        raise NotImplementedError

    @abstractmethod
    def set_employee_gender(self, employee_gender):
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
