from abc import ABC, abstractmethod
from enum import Enum

class Employee(ABC):

    def __init__(self, employee_id: str, employee_type: Enum, employee_name: str,
                 employee_gender: str, employee_age: int, call_state: Enum):
        self.employee_id = employee_id
        self.employee_type = employee_type
        self.employee_name = employee_name
        self.employee_gender = employee_gender
        self.employee_age = employee_age
        self.call_state = call_state

    @abstractmethod
    def call_handle(self):
        raise NotImplementedError

    @abstractmethod
    def escalate_call(self):
        raise NotImplementedError