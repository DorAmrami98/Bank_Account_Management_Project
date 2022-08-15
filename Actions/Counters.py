from Customers.users import Customer
from Commissions.Commissions import Commission


class Counter:

    def __init__(self):
        C = Customer()

    def counter(self, balance, User_counter, UserType):
        Balance = 0
        """
        :param User_counter: In each action, a counter counts the customer's actions
        :param UserType: [Standard, Business, Premium Business]
        The function calls the commission methods and in each account type with its own conditions
        It takes a commission after every actions the customer does
        """
        '''
        STANDARD ACCOUNT
        '''
        if UserType == 1:
            if User_counter < 5:
                User_counter += 1
                Balance = balance
                print(f"==ACTION COUNTER: {User_counter}==")
            else:
                User_counter = 0
                Balance = Commission.Business_Premium_Commission(balance)
                print(f"\nA commission was taken from your account...\n\nNow you have: {Balance} NIS\n")
            '''BUSINESS ACCOUNT'''
        elif UserType == 2:
            if User_counter < 10:
                User_counter += 1
                Balance = balance
                print(f"==ACTION COUNTER: {User_counter}==")
            else:
                User_counter = 0
                Balance = Commission.Business_Premium_Commission(balance)
                print(f"A commission was taken from your account...\n\nNow you have: {Balance} NIS\n")
            '''BUSINESS PREMIUM ACCOUNT'''
        elif UserType == 3:
            if User_counter < 10:
                User_counter += 1
                Balance = balance
                print(f"==ACTION COUNTER: {User_counter}==")
            else:
                User_counter = 0
                Balance = Commission.Business_Premium_Commission(balance)
                print(f"A commission was taken from your account...\n\nNow you have: {Balance} NIS\n")
        return Balance, User_counter
