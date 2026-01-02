# Writing two programs to understand basic of encapsulation working

# 1. Program (Result checking)

class StudentMarks:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks! Marks must be between 0 and 100")


# creating an instance to access above class

s1 = StudentMarks(90)
print(f"You got -> {s1.get_marks()} marks")

s1.set_marks(0)
s1.set_marks(99)

print(f"You got -> {s1.get_marks()} marks")





# 2. Program (Basic ATM Logic)

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def __validate_pin(self, entered_pin):
        return self.__pin == entered_pin

    def deposit(self, entered_pin, amount):
        if not self.__validate_pin(entered_pin):
            print("❌ Invalid PIN")
            return

        if amount <= 0:
            print("❌ Enter a valid amount")
            return

        self.__balance += amount
        print(f"✅ Deposited {amount} successfully")

    def withdraw(self, entered_pin, amount):
        if not self.__validate_pin(entered_pin):
            print("❌ Invalid PIN")
            return

        if amount > self.__balance:
            print("❌ Insufficient balance")
            return

        self.__balance -= amount
        print(f"✅ Withdrawn {amount} successfully")

    def check_balance(self, entered_pin):
        if not self.__validate_pin(entered_pin):
            print("❌ Invalid PIN")
            return

        print(f"💰 Current balance: {self.__balance}")


atm = ATM("pin@123", 5000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        pin = input("Enter PIN: ")
        amount = int(input("Enter amount: "))
        atm.deposit(pin, amount)

    elif choice == "2":
        pin = input("Enter PIN: ")
        amount = int(input("Enter amount: "))
        atm.withdraw(pin, amount)

    elif choice == "3":
        pin = input("Enter PIN: ")
        atm.check_balance(pin)

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
