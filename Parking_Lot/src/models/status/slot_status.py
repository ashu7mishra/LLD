from enum import Enum


class SlotStatus(Enum):
    FILLED = 'FILLED'
    EMPTY = 'EMPTY'
    RESERVED = 'RESERVED'
    BLOCKED = 'BLOCKED'
