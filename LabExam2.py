#Task-1:Sorting Employee Salary Records (Dynamic)

import time

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["salary"] > right[j]["salary"]:  # descending
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


#  Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    higher = [x for x in arr[1:] if x["salary"] > pivot["salary"]]
    lower = [x for x in arr[1:] if x["salary"] <= pivot["salary"]]

    return quick_sort(higher) + [pivot] + quick_sort(lower)


#  Dynamic Input
employees = []
n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    name = input("Name: ")
    emp_id = input("ID: ")
    salary = float(input("Salary: "))

    employees.append({
        "name": name,
        "id": emp_id,
        "salary": salary
    })


#  Merge Sort Timing
start = time.time()
merge_sorted = merge_sort(employees)
merge_time = time.time() - start


#  Quick Sort Timing
start = time.time()
quick_sorted = quick_sort(employees)
quick_time = time.time() - start


# Display Top 5
print("\nTop 5 Highest Paid Employees (Merge Sort):")
for emp in merge_sorted[:5]:
    print(emp)


#  Runtime Comparison
print("\nMerge Sort Time:", merge_time)
print("Quick Sort Time:", quick_time)


#Task-2:University Print Queue System
from collections import deque

class PrintQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, job):
        self.queue.append(job)
        print(f"Job '{job}' added.")

    def dequeue(self):
        if self.queue:
            job = self.queue.popleft()
            print(f"Processing job: {job}")
        else:
            print("Queue is empty.")

    def display(self):
        if self.queue:
            print("Current Queue:", list(self.queue))
        else:
            print("Queue is empty.")


#  Main Menu
pq = PrintQueue()

while True:
    print("\n1. Add Print Job")
    print("2. Process Print Job")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        job = input("Enter job name: ")
        pq.enqueue(job)

    elif choice == "2":
        pq.dequeue()

    elif choice == "3":
        pq.display()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")