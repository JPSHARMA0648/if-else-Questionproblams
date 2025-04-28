"""Q13 Write a program that simulates a simple ATM. The user should be able to:
Check balance
Deposit money
Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's"""
#ans


class ATM:
    def __init__(self):
        self.balance = 0  # Initial balance is 0

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}.")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}.")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

def atm_simulation():
    atm = ATM()  # Create an ATM object

    