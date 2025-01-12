from enum import Enum


class GateStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'