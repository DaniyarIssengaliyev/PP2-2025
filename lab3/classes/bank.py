class bankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,money):
        self.balance += money
    def withdrawal(self,money):
        self.balance -= money
        if(self.balance < 0):
            print("You have not enough money")
        else:
            print(self.balance)

wallet = bankAccount("Daniyar", 10000)
wallet.deposit(2000)
wallet.withdrawal(12000)