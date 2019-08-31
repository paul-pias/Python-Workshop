class Bank:
    def __init__(self, name, id, balance): #self = java's this
        self.name = name 
        self.id = id 
        self.balance = balance 

    def check_balance(x):           # _ - protected
        print(x.balance)            # __ - private
        

emran = Bank("Emran", 121, 100)
emran.check_balance()