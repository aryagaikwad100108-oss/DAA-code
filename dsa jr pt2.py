#practical 4 
#NumPy. 
#Practical 4.1: Create a NumPy Array
#Question:
#Write a Python program to create and display a NumPy array.
#import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print("Array:", numbers)
#4.2 Write a Python program to perform addition, subtraction and multiplication on a NumPy array.
# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print("Original array:", numbers)
# print("Addition:", numbers + 5)
# print("Subtraction:", numbers - 5)
# print("Multiplication:", numbers * 2)

#Write a Python program to find the maximum and minimum value in a NumPy array.
# import numpy as np

# numbers = np.array([25, 10, 45, 30, 15])

# print("Array:", numbers)
# print("Maximum:", np.max(numbers))
# print("Minimum:", np.min(numbers))
#Create a NumPy array containing 10 elements and display elements from the 1st to 5th position.
# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("Original array:", numbers)

# print("First five elements:", numbers[0:5])
#Write a Python program to display values greater than 50 from a NumPy array.
# import numpy as np

# numbers = np.array([20, 45, 60, 75, 30, 90])

# result = numbers[numbers > 50]

# print("Values greater than 50:", result)
# #Create a Pandas DataFrame containing student names and marks.
# import pandas as pd

# data = {
#     "Name": ["Rahul", "Priya", "Amit", "Sneha"],
#     "Marks": [75, 85, 65, 90]
# }

# df = pd.DataFrame(data)

# print(df)
#Create a DataFrame of student marks and display statistical information.
# import pandas as pd

# data = {
#     "Name": ["Rahul", "Priya", "Amit", "Sneha"],
#     "Marks": [75, 85, 65, 90]
# }

# df = pd.DataFrame(data)

# print(df)
# print("\nStatistical Information:")
# print(df["Marks"].describe())
#Create a Pandas Series using a dictionary containing student names and marks.
# import pandas as pd

# marks = {
#     "Rahul": 75,
#     "Priya": 85,
#     "Amit": 65,
#     "Sneha": 90
# }

# series = pd.Series(marks)

# print(series)
#Create a Pandas Series of marks and display only marks greater than 70.
# import pandas as pd

# marks = pd.Series([55, 75, 80, 60, 90])

# result = marks[marks > 70]

# print("Marks greater than 70:")
# print(result)
#Create a DataFrame containing student names, marks and attendance. Display students who have marks greater than 70.
# import pandas as pd

# data = {
#     "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
#     "Marks": [75, 85, 60, 90, 65],
#     "Attendance": [80, 90, 75, 95, 70]
# }

# df = pd.DataFrame(data)

# print("Student Data:")
# print(df)

# print("\nStudents scoring more than 70:")
# print(df[df["Marks"] > 70])

# #Create a 2D NumPy Array
# import numpy as np

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(arr)
# import numpy as np

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print("Shape:", arr.shape)
# Reshape an Array
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# new_arr = arr.reshape(2, 3)

# print(new_arr)
#  Generate Random Numbers
# import numpy as np

# numbers = np.random.randint(1, 100, 10)

# print(numbers)
# #  Calculate Mean, Median and Standard Deviation
# import numpy as np

# marks = np.array([60, 70, 80, 90, 75])

# print("Mean:", np.mean(marks))
# print("Median:", np.median(marks))
# print("Standard Deviation:", np.std(marks))
# I. Simple Data Analysis
#  Group Students According to Course
# import pandas as pd

# data = {
#     "Name": ["Rahul", "Priya", "Amit", "Sneha"],
#     "Course": ["BSc", "BCA", "BSc", "BCA"],
#     "Marks": [80, 90, 70, 85]
# }

# df = pd.DataFrame(data)

# result = df.groupby("Course")["Marks"].mean()

# print(result)
# Count Students in Each Course
# import pandas as pd

# data = {
#     "Name": ["Rahul", "Priya", "Amit", "Sneha"],
#     "Course": ["BSc", "BCA", "BSc", "BCA"]
# }

# df = pd.DataFrame(data)

# print(df["Course"].value_counts())
# # Find Top 3 Students
# import pandas as pd

# data = {
#     "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
#     "Marks": [75, 95, 65, 90, 85]
# }

# df = pd.DataFrame(data)

# result = df.sort_values("Marks", ascending=False)

# print(result.head(3))
# Add a Result Column
# import pandas as pd

# data = {
#     "Name": ["Rahul", "Priya", "Amit", "Sneha"],
#     "Marks": [75, 35, 65, 90]
# }

# df = pd.DataFrame(data)

# df["Result"] = df["Marks"].apply(
#     lambda x: "Pass" if x >= 40 else "Fail"
# )

# print(df)

# Simple Bar Chart
# import matplotlib.pyplot as plt
# names = ["Rahul", "Priya", "Amit", "Sneha"]
# marks = [75, 90, 65, 85]

# plt.bar(names, marks)

# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Student Marks")

# plt.show()

# . Simple Line Graph
# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [100, 150, 130, 180]

# plt.plot(months, sales)

# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.title("Monthly Sales")

# # plt.show()
# # . Simple Histogram
# import matplotlib.pyplot as plt

# marks = [50, 60, 65, 70, 70, 75, 80, 85, 90, 95]

# plt.hist(marks)

# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.title("Distribution of Marks")

# plt.show()
# Question: Write a Python program to create a linked list and display its elements.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create nodes
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# # Connect nodes
# n1.next = n2
# n2.next = n3

# # Display linked list
# current = n1

# while current:
#     print(current.data)
#     current = current.next
# # 2. Insert Node in Linked List
# # Question: Insert a new node at the beginning of a linked list.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# head = Node(20)
# head.next = Node(30)

# # Insert new node
# new_node = Node(10)
# new_node.next = head
# head = new_node

# # Display
# current = head

# # while current:
# #     print(current.data)
# #     current = current.next
# # Insert Node at the End
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# head = Node(10)
# head.next = Node(20)

# new_node = Node(30)

# current = head

# while current.next:
#     current = current.next

# current.next = new_node

# current = head

# while current:
#     print(current.data)
#     current = current.next
# Delete Node from Linked List
# Question: Delete a node containing a given value.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# # Delete 20
# head.next = head.next.next

# current = head

# while current:
#     print(current.data)
#     current = current.next
# # Search an Element in Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# search = int(input("Enter value to search: "))

# current = head
# found = False

# while current:
#     if current.data == search:
#         found = True
#         break
#     current = current.next

# if found:
#     print("Element found")
# else:
#     print("Element not found")
# # . Stack
# # Practical 6: Implement Stack Using List
# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)

# print("Stack:", stack)

# print("Deleted:", stack.pop())

# # print("Stack after deletion:", stack)
# # Stack Using Menu
# stack = []

# while True:
#     print("\n1. Push")
#     print("2. Pop")
#     print("3. Display")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         stack.append(value)

#     elif choice == 2:
#         if len(stack) == 0:
#             print("Stack is empty")
#         else:
#             print("Deleted:", stack.pop())

#     elif choice == 3:
#         print("Stack:", stack)

#     elif choice == 4:
#         break

#     else:
#         print("Invalid choice")
# . Queue
# Practical 8: Implement Queue Using List
# queue = []

# queue.append(10)
# queue.append(20)
# queue.append(30)

# print("Queue:", queue)

# print("Deleted:", queue.pop(0))

# print("Queue after deletion:", queue)
# . Queue Using Menu
# queue = []

# while True:
#     print("\n1. Insert")
#     print("2. Delete")
#     print("3. Display")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         queue.append(value)

#     elif choice == 2:
#         if len(queue) == 0:
#             print("Queue is empty")
#         else:
#             print("Deleted:", queue.pop(0))

#     elif choice == 3:
#         print("Queue:", queue)

#     elif choice == 4:
#         break

#     else:
#         print("Invalid choice")
# Circular Queue
# from collections import deque

# queue = deque(maxlen=3)

# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue)

# queue.append(40)

# print(queue)
# Linear Search
# Question: Search for an element in a list using linear search.
# numbers = [10, 20, 30, 40, 50]

# search = int(input("Enter number: "))

# found = False

# for i in range(len(numbers)):
#     if numbers[i] == search:
#         print("Element found at position", i)
#         found = True
#         break

# if not found:
#     print("Element not found")
# . Binary Search
# Question: Search for an element using binary search.
# numbers = [10, 20, 30, 40, 50, 60]

# search = int(input("Enter number: "))

# low = 0
# high = len(numbers) - 1

# while low <= high:

#     mid = (low + high) // 2

#     if numbers[mid] == search:
#         print("Element found")
#         break

#     elif search > numbers[mid]:
#         low = mid + 1

#     else:
#         high = mid - 1

# else:
#     print("Element not found")
# . Binary Search
# Question: Search for an element using binary search.
# numbers = [10, 20, 30, 40, 50, 60]

# search = int(input("Enter number: "))

# low = 0
# high = len(numbers) - 1

# while low <= high:

#     mid = (low + high) // 2

#     if numbers[mid] == search:
#         print("Element found")
#         break

#     elif search > numbers[mid]:
#         low = mid + 1

#     else:
#         high = mid - 1

# else:
# #     print("Element not found")
# # Bubble Sort
# numbers = [50, 20, 40, 10, 30]

# for i in range(len(numbers)):

#     for j in range(len(numbers) - i - 1):

#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print("Sorted list:", numbers)
# Selection Sort
# numbers = [50, 20, 40, 10, 30]

# for i in range(len(numbers)):

#     minimum = i

#     for j in range(i + 1, len(numbers)):

#         if numbers[j] < numbers[minimum]:
#             minimum = j

#     numbers[i], numbers[minimum] = \
#         numbers[minimum], numbers[i]

# print(numbers)
# #  Insertion Sort
# numbers = [50, 20, 40, 10, 30]

# for i in range(1, len(numbers)):

#     key = numbers[i]
#     j = i - 1

#     while j >= 0 and numbers[j] > key:
#         numbers[j + 1] = numbers[j]
#         j = j - 1

#     numbers[j + 1] = key

# print("Sorted list:", numbers)
# Recursion – Factorial
# def factorial(n):

#     if n == 0:
#         return 1

#     return n * factorial(n - 1)


# num = int(input("Enter number: "))

# print("Factorial:", factorial(num))
# Recursion – Fibonacci Series
# def fibonacci(n):

#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)


# n = int(input("Enter number of terms: "))

# for i in range(n):
#     print(fibonacci(i), end=" ")
# . Binary Tree
# Create a Simple Binary Tree
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# root = Node(10)

# root.left = Node(20)
# root.right = Node(30)

# print("Root:", root.data)
# print("Left:", root.left.data)
# print("Right:", root.right.data)
# . Tree Traversal – Inorder
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# def inorder(root):

#     if root:

#         inorder(root.left)

#         print(root.data)

#         inorder(root.right)


# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)

# inorder(root)
# Dictionary as Key-Value Data Structure
# student = {
#     "RollNo": 101,
#     "Name": "Rahul",
#     "Marks": 85
# }

# print("Roll No:", student["RollNo"])
# print("Name:", student["Name"])
# print("Marks:", student["Marks"])
# . Count Frequency of Elements
# numbers = [10, 20, 10, 30, 20, 10]

# frequency = {}

# for number in numbers:

#     if number in frequency:
#         frequency[number] += 1
#     else:
#         frequency[number] = 1

# print(frequency)
# . Word Frequency
# text = "python data science python data"
# words = text.split()

# frequency = {}

# for word in words:

#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)
# . Set Operations
# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}

# print("Union:", A | B)
# print("Intersection:", A & B)
# print("Difference:", A - B)
# . Stack Using Linked List
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# stack = None

# # Push 10
# new_node = Node(10)
# new_node.next = stack
# stack = new_node

# # Push 20
# new_node = Node(20)
# new_node.next = stack
# stack = new_node

# # Display
# current = stack

# while current:
#     print(current.data)
#     current = current.next
# Queue Using Linked List
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

queue.popleft()

print("After deletion:", queue)

