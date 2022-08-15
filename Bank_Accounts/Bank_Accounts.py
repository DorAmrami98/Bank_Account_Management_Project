
"""
Contains the parameters to open a bank account and used in ACTIONS Class
"""
class Bank_Account:
    def __init__(self):
        self.balance = 0
        self.account_type = ""

    def Balance(self):
        self.balance = int(input("How Much Money Would You Like To Deposit ? "))
        return self.balance

    def Type(self, Acc_Name):
        business = input("Are You A Business Owner? Y/N: ").upper()
        if business == "N":
            Acc_Type = "STANDARD"
            return Acc_Type, 1
        elif business == "Y":
            income = int(input(f"{Acc_Name} What Is Your Monthly Income?: "))
            if income <= 25000:
                Acc_Type = "STANDARD"
                number = 1
            elif (income > 25000) and (income < 100000):
                Acc_Type = "BUSINESS"
                number = 2
            else:
                Acc_Type = "BUSINESS PREMIUM"
                number = 3
            return Acc_Type, number
        else:
            raise ValueError("Wrong Answer!")


