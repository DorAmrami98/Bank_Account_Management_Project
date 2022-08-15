
"""
Customer class which creates the customer and being called to Actions.Join_Bank
"""


class Customer:

    def __init__(self):
        self.Name = ""
        self.ID = 0
        self.Dict_Users_type = {}

    def Add_User_Name(self):
        self.Name = str(input("Enter Your Name: ")).upper()
        if not self.Name:
            raise ValueError("Invalid Input. Your Name Cannot Be Blank! ")
        elif not self.Name.isalpha():
            raise ValueError("Name Should Contain Only Alphabetical Characters!")
        return self.Name

    def Add_User_ID(self):
        self.ID = int(input("Enter Your ID: "))
        return self.ID

    def Users_type(self, identification, TypeNum):
        self.Dict_Users_type[identification] = TypeNum
        return self.Dict_Users_type
