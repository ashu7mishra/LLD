from enum import Enum


class FloorStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    FULL = 'FULL'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'