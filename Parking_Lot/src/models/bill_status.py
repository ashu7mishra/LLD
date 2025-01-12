from enum import Enum


class BillStatus(Enum):
    PAID = 'PAID'
    PENDING = 'PENDING'
    PARTIALLY_PAID = 'PARTIALLY PAID'