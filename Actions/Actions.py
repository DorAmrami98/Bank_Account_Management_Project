from Customers.users import Customer
from Bank_Accounts.Bank_Accounts import Bank_Account
from Actions.Counters import Counter

'''
Class ACTIONS that contains all the bank possible actions 
'''


class Actions:
    def __init__(self):
        self.dict_of_BankAccount = {}
        self.dict = {}
        self.UserName = ""
        self.UserID = 0
        self.savings_account = {}
        self.Counters_Dict = {}
        self.Dict_UsersType = {}
        self.ID = 0

    def Join_Bank(self):
        """
        First function that adds a customer into the bank records with his ID and NAME
        Can't register into the bank with the same ID as someone else
        Calls the customer class from customers
        """
        n = "Y"
        while n != "N":
            try:
                print("-------Bank Joining Form-------")
                User = Customer()
                self.UserName = Customer.Add_User_Name(User)
                self.UserID = Customer.Add_User_ID(User)
                if self.UserID in self.dict.keys():
                    raise ValueError("This ID already exists in our system!\nPlease try again\n ")
                else:
                    self.dict.update({self.UserID: self.UserName})
                    print(f"Hi {self.UserName}!, Welcome To Our Bank!")
                    n = "N"
            except Exception as e:
                n = "Y"
                print(f"{e}")
            print("----------------------------------")
        print(f"\n----------Bank Customers----------\n{self.dict}"
              f"\n----------------------------------")

    def Open_Account(self):
        """
        Function that creates a bank account to a customer with his individual ID
        The function calls 2 methods from Bank_Accounts (Balance,Type) into this function
        Asks how much money the customer wants to deposit and if he is a business owner
        In every account opening, a savings account is being opened as well,containing 0 NIS
        As well as an action counter that resets and ready to count the customer's actions for the bank commissions :(
        """
        Account = Bank_Account()
        typeAcc = Customer()
        counter = Counter()
        Acc_Name = ""
        Exit_Open_Acc = "Y"
        while Exit_Open_Acc != "N":
            try:
                print("\n-------Account Opening Form-------")
                identification = int(input("Please Identify Yourself With Your ID: "))
                if identification in self.dict.keys():
                    self.ID = identification
                    balance = Bank_Account.Balance(Account)
                    self.dict_of_BankAccount[identification] = balance
                    Acc_Name = self.dict[identification]
                    Account_Type, TypeNum = Bank_Account.Type(Account, Acc_Name)
                    self.Dict_UsersType = Customer.Users_type(typeAcc, identification, TypeNum)
                    print(
                        f"    {Acc_Name} You Have A {Account_Type} Account With {self.dict_of_BankAccount[identification]} NIS")
                else:
                    raise ValueError("\nThis ID is not in our system!\nPlease Try Again ")
                self.savings_account[identification] = 0
                '''Activates Reset Counter'''
                self.Counters_Dict[identification] = 0
                print(f"    Initial SAVINGS Account: {self.savings_account[identification]} NIS")
                Exit_Open_Acc = "N"
            except Exception as e:
                Exit_Open_Acc = "Y"
                print(f"{e}")
            print("----------------------------------")

    def Close_Account(self):
        """
        A closing account function that closes the customer's account by switching his status to 'INACTIVE'
        Once the account closes, all of his money in both his balance and his savings transfer into the customers
        'pocket' (AKA User_Money)
        The customer is still being saved in the bank records as a customer
        """
        Exit_ClsAcc = False
        User_Money = 0
        while Exit_ClsAcc != True:
            try:
                print("-------Account Closing Form-------")
                identification = int(input("Please Identify Yourself With Your ID: "))
                if identification in self.dict.keys():
                    User_Money += self.dict_of_BankAccount[identification]
                    User_Money += self.savings_account[identification]
                    self.dict_of_BankAccount[identification] = "INACTIVE"
                    self.savings_account[identification] = "INACTIVE"
                    print(
                        f"-Hey {self.dict[identification]}-,\n    Sorry To See You Go!\n    Here Is Your Money Back: {User_Money} NIS\n")
                    print(f"-Your Account Is: {self.dict_of_BankAccount[identification]}-")
                    for key in self.dict_of_BankAccount:
                        print(
                            f"-ID: {key}-    -Name: {self.dict[key]}-    -Account Status: {self.dict_of_BankAccount[key]}-")
                Exit_ClsAcc = True
            except Exception as e:
                Exit_ClsAcc = False
                print(f"{e}")

    def Savings_Account(self):
        """
        A function that does various actions on customer's savings account
        Deposit And Withdrawal
        The function calls 2 separate methods (savings_deposit,savings_withdraw) in order to lighten up the load from
        this function and do a separation between deposit and withdraw
        In addition, calls the counter
        """
        Exit_Savings = False
        identification = 0
        c = Counter()
        while Exit_Savings != True:
            try:
                print("-------Savings Account-------")
                identification = self.ID
                if identification in self.dict.keys():
                    D_OR_W = input("Do You Want To Make A Deposit Or Withdrawal?: D/W:  ").upper()
                    if D_OR_W == "D":
                        '''DEPOSIT'''
                        Actions.savings_deposit(self, identification)
                        Balance_after_commission, Count = Counter.counter(c,
                                                                          self.dict_of_BankAccount[identification],
                                                                          self.Counters_Dict[identification],
                                                                          self.Dict_UsersType[identification])
                        self.Counters_Dict[identification] = Count
                        self.dict_of_BankAccount[identification] = Balance_after_commission
                        Exit_Savings = True
                    elif D_OR_W == "W":
                        '''WITHDRAW'''
                        Exit_Savings = Actions.savings_withdraw(self, identification)
                        Balance_after_commission, Count = Counter.counter(c,
                                                                          self.dict_of_BankAccount[identification],
                                                                          self.Counters_Dict[identification],
                                                                          self.Dict_UsersType[identification])
                        self.Counters_Dict[identification] = Count
                        self.dict_of_BankAccount[identification] = Balance_after_commission
                    else:
                        raise ValueError("Error!!!!\nTry Again\n")
            except Exception as e:
                Exit_Savings = False
                print(f"{e}")
        print(f"Your SAVINGS Account Contains: {self.savings_account[identification]} NIS")
        print(f"    Your BALANCE Account: {self.dict_of_BankAccount[identification]}")

    def savings_deposit(self, identification):
        reset_function = True
        money_in_Account = self.dict_of_BankAccount[identification]
        money = self.savings_account[identification]
        while reset_function != False:
            amount = int(input('Enter The Amount To Deposit To Your Saving Account: '))
            if amount > money_in_Account:
                print("Insufficient Funds!")
            else:
                self.dict_of_BankAccount[identification] -= amount
                money += amount
                self.savings_account[identification] = money
                reset_function = False

    def savings_withdraw(self, identification):
        reset_function = True
        while reset_function != False:
            amount = int(input('Enter The Amount To Withdraw From Your Saving Account: '))
            money = self.savings_account[identification]
            money -= amount
            self.dict_of_BankAccount[identification] += amount
            self.savings_account[identification] = money
            reset_function = False
            if amount > money:
                print("Insufficient Funds!")
                return False
        return True

    def Show_Balance(self):
        """
        A function that shows the customer entire account details
        Calls a counter
        """
        Exit_Show = False
        c = Counter()
        while Exit_Show != True:
            try:
                print("\n-------Balance Status------")
                identification = self.ID
                if identification in self.dict.keys():
                    info = self.dict_of_BankAccount[identification]
                    print(f"\n== Your Account: {info} ==\n")
                    print(f"== Your SAVINGS Account: {self.savings_account[identification]} ==\n")
                    Balance_after_commission, Count = Counter.counter(c, info, self.Counters_Dict[identification],
                                                                      self.Dict_UsersType[identification])
                    self.Counters_Dict[identification] = Count
                    self.dict_of_BankAccount[identification] = Balance_after_commission
                Exit_Show = True
            except Exception as e:
                Exit_Show = False
                print(f"{e}")

    def Deposit(self):
        """
        A deposit function that lets the customer deposit money into his account
        Calls the counter
        """
        print("\n-------Money Deposit Service------")
        c = Counter()
        try:
            identification = self.ID
            if identification in self.dict.keys():
                amount = float(input('Enter the amount to deposit: '))
                balance = self.dict_of_BankAccount[identification]
                balance += amount
                print(f"\nYour BALANCE After The Deposit: {balance} NIS")
                Balance_after_commission, Count = Counter.counter(c, balance, self.Counters_Dict[identification],
                                                                  self.Dict_UsersType[identification])
                self.Counters_Dict[identification] = Count
                self.dict_of_BankAccount[identification] = Balance_after_commission
        except Exception as e:
            print(f"{e}")
        print("----------------------------------")

    def Withdraw(self):
        """
        A withdrawal function that lets the customer withdraw money from his account
        Can't over draft, prevents debt

        Calls counter
        """
        c = Counter()
        try:
            print("\n------Money Withdrawal Service------")
            identification = self.ID
            info = self.dict_of_BankAccount[identification]
            if identification in self.dict.keys():
                Balance_Now = info
                Prevent_Minus = False
                while Prevent_Minus != True:
                    amount = float(input("Enter The Amount You Want To Withdraw: "))
                    try:
                        if amount > info:
                            Prevent_Minus = False
                            raise ValueError("Insufficient Funds!")
                        else:
                            Balance_Now -= amount
                            info = Balance_Now
                            Prevent_Minus = True
                            print(f"Your Balance After The Withdraw: {Balance_Now}")
                            self.dict_of_BankAccount[identification] = info
                    except Exception as e:
                        print(f"{e}")
                Balance_after_commission, Count = Counter.counter(c, info, self.Counters_Dict[identification],
                                                                  self.Dict_UsersType[identification])
                self.dict_of_BankAccount[identification] = Balance_after_commission
                self.Counters_Dict[identification] = Count
        except Exception as e:
            print(f"{e}")
        print("----------------------------------")


