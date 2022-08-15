from CLI.Invoker import Invoker
from CLI.CLI import Cli
from Actions.Actions import Actions
from CLI.Calling_Functions import Join_Bank, Open_Account, Savings_Account, Close_Account, Deposit, Withdraw, Show_Balance


def main():
    """
    CLI
    """
    action = Actions()
    join_bank = Join_Bank(action)
    open_account = Open_Account(action)
    saving_account = Savings_Account(action)
    close_account = Close_Account(action)
    deposit = Deposit(action)
    withdraw = Withdraw(action)
    show_balance = Show_Balance(action)

    """
    RUN COMMANDS
    """
    Answer1 = "Y"
    while Answer1 != "N":
        invoker = Invoker()
        X1 = Cli.form1()
        if X1 == 1:
            invoker.process_command(join_bank)
        elif X1 == 2:
            invoker.process_command(open_account)
            Answer2 = "Y"
            while Answer2 != "N":
                X2 = Cli.form2()
                if X2 == 1:
                    invoker.process_command(saving_account)
                elif X2 == 5:
                    invoker.process_command(close_account)
                elif X2 == 2:
                    invoker.process_command(deposit)
                elif X2 == 3:
                    invoker.process_command(withdraw)
                elif X2 == 4:
                    invoker.process_command(show_balance)
                try:
                    Answer2 = input("\nPerform Another Actions On Your Account? Y/N: ").upper()
                    if not Answer2:
                        raise ValueError("Invalid Input. Your Answer Cannot Be Blank! ")
                    elif not Answer2.isalpha():
                        raise ValueError("Answer Should Contain Only Alphabetical Characters!")
                except Exception as e:
                    Answer2 = "Y"
                    print(f"{e}")
        try:
            Answer1 = input("\nPerform Another Actions? Y/N: ").upper()
            if not Answer1:
                raise ValueError("Invalid Input. Your Answer Cannot Be Blank! ")
            elif not Answer1.isalpha():
                raise ValueError("Answer Should Contain Only Alphabetical Characters!")
        except Exception as e:
            Answer1 = "Y"
            print(f"{e}")


if __name__ == '__main__':
    main()


