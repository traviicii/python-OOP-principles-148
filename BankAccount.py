class BankAccount():

    def __init__(self, account_holder, balance= 0):
        self.__balance = balance # Private attribute
        self.account_holder = account_holder

    # Getter
    def get_balance(self):
        return self.__balance
    
    # Setter
    def set_balance(self, new_balance):
        self.__balance = new_balance

    # Getter
    def get_holder(self):
        return self.account_holder
    
    # Setter
    def set_holder(self, new_holder):
        self.account_holder = new_holder

    # Deposit method
    def deposit(self, money):
        if money > 0:
            self.set_balance(self.get_balance() + money)

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount and amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        elif amount > self.get_balance():
            print("You don't have that amount of money in da bank.")
        else:
            print("Invalid entry. Enter a number greater than zero and less than your total balance")

if __name__ == "__main__":

    travis = BankAccount("Travis Peck", 12)
    # Test out getters
    print(travis.get_balance())
    print(travis.get_holder())

    # Deposit some coinssssss
    travis.deposit(1000000)
    print(travis.get_balance())

    # Withdraw some cheddar
    travis.withdraw(100)
    print(travis.get_balance())