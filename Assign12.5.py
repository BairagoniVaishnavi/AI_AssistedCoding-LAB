#Task 1 – Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(arr))


#Task 2 – Binary Search
def binary_search(arr, target):
    """
    Performs Binary Search on sorted list.

    Best Case: O(1)
    Average Case: O(log n)
    Worst Case: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))

#Task 3 – Healthcare Appointment Scheduling
appointments = [
    {"id": 101, "patient": "A", "fee": 500},
    {"id": 102, "patient": "B", "fee": 300},
    {"id": 103, "patient": "C", "fee": 700}
]

# Sorting by fee
sorted_appointments = sorted(appointments, key=lambda x: x["fee"])

print("Sorted by Fee:", sorted_appointments)

#Task 4 – Railway Reservation System
tickets = [
    {"ticket_id": 1, "seat": 12},
    {"ticket_id": 2, "seat": 5},
    {"ticket_id": 3, "seat": 20}
]

sorted_tickets = sorted(tickets, key=lambda x: x["seat"])
print(sorted_tickets)

#Task 5 – Hostel Room Allocation
rooms = [
    {"student_id": 101, "room": 12},
    {"student_id": 102, "room": 5},
    {"student_id": 103, "room": 20}
]

sorted_rooms = sorted(rooms, key=lambda x: x["room"])
print(sorted_rooms)

#Task 6 – Online Movie Streaming Platform
movies = [
    {"id": 1, "rating": 8.5},
    {"id": 2, "rating": 9.2},
    {"id": 3, "rating": 7.8}
]

sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
print(sorted_movies)

#Task 7 – Agriculture Crop Monitoring
crops = [
    {"id": 1, "moisture": 30},
    {"id": 2, "moisture": 45},
    {"id": 3, "moisture": 25}
]

sorted_crops = sorted(crops, key=lambda x: x["moisture"])
print(sorted_crops)

#Task 8 – Airport Flight Management
flights = [
    {"id": 1, "departure": "10:30"},
    {"id": 2, "departure": "08:15"},
    {"id": 3, "departure": "12:45"}
]

sorted_flights = sorted(flights, key=lambda x: x["departure"])
print(sorted_flights)