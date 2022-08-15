
"""
Commission class that calculates the commission amount to take from a customer considering his account type
"""


class Commission:
    @staticmethod
    def Standard_Commission(balance):
        money = (balance * 0.05)
        balance -= money
        return balance

    @staticmethod
    def Business_Commission(balance):
        balance -= (balance * 0.05)
        return balance

    @staticmethod
    def Business_Premium_Commission(balance):
        balance -= (balance * 0.025)
        return balance




