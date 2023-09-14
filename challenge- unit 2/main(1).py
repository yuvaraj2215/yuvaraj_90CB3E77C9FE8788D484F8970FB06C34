class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount:.2f} into {self.__account_holder_name}'s account."
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return f"Withdrew ${amount:.2f} from {self.__account_holder_name}'s account."
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"


# Example usage:
if __name__ == "__main__":
    # Create a BankAccount instance
    my_account = BankAccount("123456789", "John Doe", 1000.0)

    # Deposit money
    print(my_account.deposit(500.0))  # Deposited $500.00 into John Doe's account.

    # Withdraw money
    print(my_account.withdraw(200.0))  # Withdrew $200.00 from John Doe's account.

    # Display account balance
    print(my_account.display_balance())  # Account balance for John Doe: $1300.00
