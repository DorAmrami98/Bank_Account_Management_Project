from CLI.Command_Interface import Run

''' Concrete Command classes'''

class Join_Bank(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Join_Bank()


class Open_Account(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Open_Account()


class Savings_Account(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Savings_Account()


class Close_Account(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Close_Account()


class Deposit(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Deposit()


class Withdraw(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Withdraw()


class Show_Balance(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Show_Balance()


class Get_ID(Run):
    def __init__(self, call):
        self.call = call

    def process(self):
        self.call.Get_ID()