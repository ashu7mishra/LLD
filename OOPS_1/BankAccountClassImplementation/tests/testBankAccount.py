import unittest

from config.bankAccount import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("1234567890", 1000, 5)  # Sample account

    def test_getSimpleInterest(self):
        # Test for 1 year
        self.assertAlmostEqual(self.account.getSimpleInterest(1), 50.0)
        # Test for 2 years
        self.assertAlmostEqual(self.account.getSimpleInterest(2), 100.0)

    def test_getBalanceWithInterest(self):
        # Test for 1 year
        self.assertAlmostEqual(self.account.getBalanceWithInterest(1), 1050.0)
        # Test for 2 years
        self.assertAlmostEqual(self.account.getBalanceWithInterest(2), 1100.0)


if __name__ == '__main__':
    unittest.main()
