class BankAccount:
    # TODO: Initialize the constructor
    def __init__(self, accountNumber, balance, roi):
        self.accountNumber = accountNumber
        self.balance = balance
        self.roi = roi

    # TODO: Implement this method to calculate the simple interest
    def getSimpleInterest(self, time):
        return (self.balance*self.roi*time)/100

    #TODO: Implement this method to return the total amount after adding the interest
    def getBalanceWithInterest(self, time):
        return self.balance + self.getSimpleInterest(time)
