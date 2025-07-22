
class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount) and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -${amount}")
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount")

    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name
        print(f"Bank name changed to {cls.bank_name}")

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

    def show_transactions(self) -> None:
        print(f"Transaction history for {self.account_holder}:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print("-", t)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} added.")

    def __str__(self) -> str:
        return f"Savings Account - Account Holder: {self.account_holder}, Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100:.1f}%"


account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.deposit(200)
account2.withdraw(600)
account2.withdraw(200)

BankAccount.change_bank_name("Future Bank")

print(account1)
print(account2)

print("Is -50 valid?", BankAccount.validate_amount(-50))
print("Is 150 valid?", BankAccount.validate_amount(150))

account1.show_transactions()
account2.show_transactions()

savings = SavingsAccount("Charlie", 1000, 0.05)
savings.deposit(50)
savings.add_interest()
print(savings)
savings.show_transactions()
