from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
class Bank:
    def __init__(self, name,id,balance):
        self.name = name
        self.id = id
        self.balance = balance
    def deposit(self,balance):
        self.balance+=balance
        print("{} was deposited at time {} ".format(self.balance,current_time))
        print("Your Current Balance is ",self.balance)
        return balance
    def cashout(self,balance):
        self.balance=balance
        print("Your Current Balance is ",self.balance)
        return balance
    def check_balance(self):
        print("Your Current Balance is ",self.balance)