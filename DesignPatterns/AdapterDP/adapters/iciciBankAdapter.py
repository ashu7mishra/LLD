from DesignPatterns.AdapterDP.Banks.IciciBank import IciciBank
from DesignPatterns.AdapterDP.adapters.bank_adapter_abc import BankAdapterABC


class IciciBankAdapter(BankAdapterABC):

    def __init__(self):
        self.bank = IciciBank()

    def checkBalance(self):
        return self.bank.bal()