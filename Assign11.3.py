#Task 1 – Smart Contact Manager (Arrays & Linked Lists)
#Array Implementation
class ContactManagerArray:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append((name, phone))
        print("Contact added.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact[0] == name:
                return contact
        return "Contact not found"

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact[0] == name:
                self.contacts.remove(contact)
                return "Contact deleted"
        return "Contact not found"


manager = ContactManagerArray()

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        manager.add_contact(name, phone)

    elif choice == "2":
        name = input("Enter name to search: ")
        print(manager.search_contact(name))

    elif choice == "3":
        name = input("Enter name to delete: ")
        print(manager.delete_contact(name))

    elif choice == "4":
        break

    else:
        print("Invalid choice")


manager = ContactManagerArray()
manager.add_contact("Alice", "9876543210")
manager.add_contact("Bob", "9123456780")

print(manager.search_contact("Alice"))
print(manager.delete_contact("Bob"))

#Linked List Implementation
class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None


class ContactManagerLinkedList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone):
        new_node = Node(name, phone)
        new_node.next = self.head
        self.head = new_node
        print("Contact added.")

    def search_contact(self, name):
        temp = self.head
        while temp:
            if temp.name == name:
                return (temp.name, temp.phone)
            temp = temp.next
        return "Contact not found"

    def delete_contact(self, name):
        temp = self.head
        prev = None
        while temp:
            if temp.name == name:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return "Contact deleted"
            prev = temp
            temp = temp.next
        return "Contact not found"


manager = ContactManagerLinkedList()

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        manager.add_contact(name, phone)

    elif choice == "2":
        name = input("Enter name to search: ")
        print(manager.search_contact(name))

    elif choice == "3":
        name = input("Enter name to delete: ")
        print(manager.delete_contact(name))

    elif choice == "4":
        break

    else:
        print("Invalid choice")


#Task 2 – Library Book Search System (Queue & Priority Queue)
#Code – Queue
from collections import deque

class LibraryQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, name):
        self.queue.append(name)
        print("Request added.")

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return "Queue empty"


library = LibraryQueue()

while True:
    print("\n1. Add Request\n2. Process Request\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter requester name: ")
        library.enqueue(name)

    elif choice == "2":
        print(library.dequeue())

    elif choice == "3":
        break


#Priority Queue
import heapq

class LibraryPriorityQueue:
    def __init__(self):
        self.pq = []

    def enqueue(self, name, role):
        priority = 1 if role.lower() == "faculty" else 2
        heapq.heappush(self.pq, (priority, name))
        print("Request added.")

    def dequeue(self):
        if self.pq:
            return heapq.heappop(self.pq)[1]
        return "No requests"


pq = LibraryPriorityQueue()

while True:
    print("\n1. Add Request\n2. Process Request\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        role = input("Enter role (Faculty/Student): ")
        pq.enqueue(name, role)

    elif choice == "2":
        print("Processing:", pq.dequeue())

    elif choice == "3":
        break


#Task 3 – Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ticket):
        self.stack.append(ticket)
        print("Ticket added.")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "No tickets"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Empty"


stack = Stack()

while True:
    print("\n1. Add Ticket\n2. Resolve Ticket\n3. View Latest\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        ticket = input("Enter ticket name: ")
        stack.push(ticket)

    elif choice == "2":
        print("Resolved:", stack.pop())

    elif choice == "3":
        print("Latest:", stack.peek())

    elif choice == "4":
        break


#Task 4 – Hash Table
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))
        print("Inserted")

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return "Not found"

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return "Deleted"
        return "Not found"


ht = HashTable()

while True:
    print("\n1. Insert\n2. Search\n3. Delete\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        ht.insert(key, value)

    elif choice == "2":
        key = input("Enter key to search: ")
        print(ht.search(key))

    elif choice == "3":
        key = input("Enter key to delete: ")
        print(ht.delete(key))

    elif choice == "4":
        break



    