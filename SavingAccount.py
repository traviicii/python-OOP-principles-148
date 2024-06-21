from BankAccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.set_balance(self.get_balance() + interest)
        print(f"${interest} was added to your account!")
        print(f"Your new balance is: ${self.get_balance()}")


# Create an instance (object) and test
james = SavingsAccount("James", 234000, .05)
print(james.get_balance())
print(james.add_interest())
print(james.add_interest())
print(james.add_interest())
print(james.add_interest())
print(james.add_interest())
print(james.add_interest())
print(james.add_interest())
print(james.add_interest())
print(james.add_interest())

