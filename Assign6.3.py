#Task-1:Develop a Student class using AI assistance with attributes and a display method
class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)


if __name__ == "__main__":
    s1 = Student("Alice", 101, "CSE")
    s1.display_details()

#Task-2:Generate code to print the first 10 multiples of a given number using different loop constructs.
#Code (Using for loop)
def print_multiples(num):
    for i in range(1, 11):
        print("using for loop:", num * i)


if __name__ == "__main__":
    print_multiples(5)

#Code (Using while loop)
def print_multiples_while(num):
    i = 1
    while i <= 10:
        print("using while loop:", num * i)
        i += 1


if __name__ == "__main__":
    print_multiples_while(5)


#Task=-3:Classify a person’s age into categories using conditional statements.
#Code (if-elif-else)
def classify_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"


if __name__ == "__main__":
    print(classify_age(25))

#Code (Simplified logic using dictionary)
def classify_age_simple(age):
    if age < 13:
        return "Child"
    if age < 20:
        return "Teenager"
    if age < 60:
        return "Adult"
    return "Senior"

#Task-4:Calculate the sum of the first n natural numbers using different approaches
#Code (for loop)
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == "__main__":
    print(sum_to_n(10))


#Code (while loop)
def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

#Task-5:Create a Bank Account class with deposit, withdraw, and balance checking functionality.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


if __name__ == "__main__":
    acc = BankAccount(5000)
    acc.deposit(1000)
    acc.withdraw(2000)
    acc.check_balance()

