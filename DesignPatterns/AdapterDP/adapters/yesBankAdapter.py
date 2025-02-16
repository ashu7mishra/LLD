from DesignPatterns.AdapterDP.Banks.YesBank import YesBank
from DesignPatterns.AdapterDP.adapters.bank_adapter_abc import BankAdapterABC


class YesBankAdapter(BankAdapterABC):

    def __init__(self):
        self.bank = YesBank()

    def checkBalance(self):
        return self.bank.balance()