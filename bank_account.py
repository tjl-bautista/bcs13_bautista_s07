class BankAccount:
    def __init__(self, account_number, balance):
        # single underscore prefix ('_') to indicate that an attribute or method should be treated as 'private' or 'internal' to the class.
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print("Deposit successful. New Balance: ", self._balance)

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Withdrawal successful. New Balance: ", self._balance)
        else:
            print("Insufficient balance. Cannot Withdraw.")

    def get_balance(self):
        return self._balance
        

# create an instance of bank account object
my_account = BankAccount("123456", 2500)
print(my_account._account_number)

# deposit
my_account.deposit(500)

# withdrawal
my_account.withdraw(200)