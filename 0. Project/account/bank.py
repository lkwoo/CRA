class Account:
    def __init__(self, balance):
        self.balance = balance

    def transfer_to(self, target, amount):
        if self.balance < amount:
            raise ValueError("예금 부족")
        self.balance -= amount
        target.balance += amount