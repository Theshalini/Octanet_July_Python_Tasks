class ATM:
    def __init__(self, initial_balance=0):
        """
        Initialize the ATM with a given initial balance.
        Default PIN is set to '1234'.
        Transaction history is initialized as an empty list.
        """
        self.balance = initial_balance
        self.pin = "1234"  # Default PIN
        self.transaction_history = []
    
    def check_pin(self, input_pin):
        """
        Checks if the entered PIN matches the stored PIN.
        Returns True if they match, else False.
        """
        if self.pin == input_pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def balance_inquiry(self):
        """
        Displays the current balance and log the transaction.
        """
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Balance Inquiry")

    def deposit(self, amount):
        """
        Deposits a specified amount to the account if the amount is positive.
        Log the transaction.
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
            self.transaction_history.append(f"Deposited Rs. {amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if there are sufficient funds and the amount is positive.
        Log the transaction.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
                self.transaction_history.append(f"Withdrew Rs. {amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def change_pin(self, old_pin, new_pin):
        """
        Changes the PIN if the old PIN is verified correctly.
        Log the transaction.
        """
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("PIN Changed")

    def show_transaction_history(self):
        """
        Displays the transaction history.
        """
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    # Initialize the ATM with a default balance of $500
    atm = ATM(initial_balance=500)  
    authenticated = False
    
    # Main loop for the ATM menu
    while True:
        print("\n=== ATM Menu ===")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        # Exit the loop if the user chooses to exit
        if choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        
        # Authenticate the user before proceeding with other options
        if not authenticated:
            input_pin = input("Enter your PIN: ")
            authenticated = atm.check_pin(input_pin)
            if not authenticated:
                continue

        # Perform the selected operation
        if choice == "1":
            atm.balance_inquiry()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "4":
            old_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == "5":
            atm.show_transaction_history()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Entry point of the program
    main()
