#Task 1: Mutable Default Argument – Function Bug
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))


#Task 2: Floating-Point Precision Error
def check_sum():
    return abs((0.1 + 0.2) - 0.3) < 1e-9

print(check_sum())

#Task 3: Recursion Error – Missing Base Case
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

#Task 4: Dictionary Key Error
def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c", "Key not found")

print(get_value())

#Task 5: Infinite Loop – Wrong Condition
def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1

loop_example()

#Task 6: Unpacking Error – Wrong Variables
a, b, _ = (1, 2, 3)
print(a, b)

#Task 7: Mixed Indentation – Tabs vs Spaces
def func():
    x = 52005
    y = 10
    return x + y

print(func())

#Task 8: Import Error – Wrong Module Usage
import math
print(math.sqrt(16))
