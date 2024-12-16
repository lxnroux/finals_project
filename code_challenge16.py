class BankAccount:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}.")
            self.show_balance()
            self.breakdown_denomination(amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Successfully withdrew {amount}.")
                self.show_balance()
                self.breakdown_denomination(amount)
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

    def breakdown_denomination(self, amount):
        print(f"Breakdown of {amount}:")
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        for denom in denominations:
            count = amount // denom
            if count > 0:
                print(f"{denom} = {count}")
            amount %= denom


def main():
    print("Welcome to the Bank System!")
    accounts = {}

    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            if name in accounts:
                print("Account already exists.")
            else:
                accounts[name] = BankAccount(name, initial_deposit)
                print(f"Account created for {name} with initial deposit of {initial_deposit}.")

        elif choice == "2":
            name = input("Enter account name: ")
            if name in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            name = input("Enter account name: ")
            if name in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            name = input("Enter account name: ")
            if name in accounts:
                accounts[name].show_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            print("Thank you for using the Bank System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
