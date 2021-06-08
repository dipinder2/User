class User:
    def __init__(self,name):
        self.name=name
        self.balance = 0
    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
    def make_deposit(self, amount):
        self.balance+=amount
        return self
    def display_user_balance(self):
        print(f'{self.name} has {self.balance}')
        return self
    def  transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.balance+=amount
        return self
jacob = User("jacob")
ross = User("Ross")
bryan = User("bryan")
jacob.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).transfer_money(ross,100).display_user_balance()
ross.make_deposit(200).make_deposit(200).make_withdrawal(100).make_withdrawal(100).display_user_balance()
bryan.make_deposit(300).make_withdrawal(10).make_withdrawal(100).make_withdrawal(20).display_user_balance()
