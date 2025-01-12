from enum import Enum


class PaymentMode(Enum):
    CASH = 'CASH'
    ONLINE = 'ONLINE'
    CARD = 'CARD'
    UPI = 'UPI'