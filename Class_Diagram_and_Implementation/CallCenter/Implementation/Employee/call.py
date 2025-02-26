from Class_Diagram_and_Implementation.CallCenter.Implementation.Employee.call_state import CallState


class Call(object):

    def __init__(self, employee_type):
        self._call_state = CallState.READY
        self._employee_type = employee_type
        self._employee = None
