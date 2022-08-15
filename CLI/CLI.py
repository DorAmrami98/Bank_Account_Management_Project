
"""
Creates the CLI form
"""

class Cli:
    @staticmethod
    def form1():
        Option_List = [1, 2]
        T_F = False
        while T_F != True:
            try:
                print("\nWelcome To our Bank!\n")
                print("=========== Which Action Would You Like To Do: ===========")
                X = int(input("* Join Our bank ............................. Press -1-\n"
                              "* Open An Account ........................... Press -2-\n\n"
                              "Your Answer: "))
                if X in Option_List:
                    return X
                else:
                    T_F = False
            except Exception as e:
                T_F = False
                print(f"{e}")

    @staticmethod
    def form2():
        Option_List = [1, 2, 3, 4, 5]
        T_F = False
        while T_F != True:
            try:
                print("\nWelcome To our Bank!\n")
                print("=========== Which Action Would You Like To Do: ===========")
                X = int(input("* Perform Actions On Your Savings Account ... Press -1-\n"
                              "* Deposit Money Into Your Balance ........... Press -2-\n"
                              "* Withdraw Money From Your Balance .......... Press -3-\n"
                              "* Show Your Account Details ................. Press -4-\n"
                              "* Close Your Account ........................ Press -5-\n\n"
                              "Your Answer: "))
                if X in Option_List:
                    return X
                else:
                    T_F = False
            except Exception as e:
                T_F = False
                print(f"{e}")
