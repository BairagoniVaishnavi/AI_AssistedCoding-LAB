#Task 1 – Refactoring Global Variables
def calculate_interest(amount, rate):
    return amount * rate


rate = 0.1
amount = 1000

interest = calculate_interest(amount, rate)
print("Interest:", interest)

#Task 2 – Refactoring Deeply Nested Conditionals
score = 78

if score >= 90:
    result = "Excellent"
elif score >= 75:
    result = "Very Good"
elif score >= 60:
    result = "Good"
else:
    result = "Needs Improvement"

print(result)

#Task 3 – Refactoring Repeated File Handling Code
def read_file(filename):
    with open(filename, "r") as file:
        print(file.read())


read_file("data1.txt")
read_file("data2.txt")

#Task 4 – Optimizing Search Logic
users = {"admin", "guest", "editor", "viewer"}

name = input("Enter username: ")

if name in users:
    print("Access Granted")
else:
    print("Access Denied")


#Task 5 – Refactoring Procedural Code into OOP

class EmployeeSalaryCalculator:

    def __init__(self, salary, tax_rate):
        self.salary = salary
        self.tax_rate = tax_rate

    def calculate_net_salary(self):
        tax = self.salary * self.tax_rate
        net_salary = self.salary - tax
        return net_salary


employee = EmployeeSalaryCalculator(50000, 0.2)

print("Net Salary:", employee.calculate_net_salary())


#Task 6 – Performance Optimization

n = 1000000

even_numbers = n // 2
total = even_numbers * (even_numbers + 1)

print("Sum of even numbers:", total)

#Task 7 – Removing Hidden Side Effects
def add_item(data, value):
    new_data = data.copy()
    new_data.append(value)
    return new_data


data = []

data = add_item(data, 10)
data = add_item(data, 20)

print(data)

#Task 8 – Refactoring Complex Input Validation
def is_length_valid(password):
    return len(password) >= 8


def has_digit(password):
    return any(c.isdigit() for c in password)


def has_uppercase(password):
    return any(c.isupper() for c in password)


password = input("Enter password: ")

if not is_length_valid(password):
    print("Password too short")
elif not has_digit(password):
    print("Must contain digit")
elif not has_uppercase(password):
    print("Must contain uppercase")
else:
    print("Valid Password")