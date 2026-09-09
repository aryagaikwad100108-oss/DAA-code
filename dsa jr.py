# Practical -1
# 1.Write a Program to Insert an Element in an Array
# Program to insert an element in an array

# arr = []

# n = int(input("Enter number of elements: "))

# for i in range(n):
#     num = int(input("Enter element: "))
#     arr.append(num)

# print("Original Array:", arr)

# position = int(input("Enter position to insert (1 to {}): ".format(n + 1)))
# element = int(input("Enter element to insert: "))

# arr.insert(position - 1, element)

# print("Array after insertion:")
# print(arr)
# 2. Write a Program to Access a Matrix Using Recursive Call
# # Program to display a matrix using recursion

# def display(matrix, rows, cols, i, j):

#     if i == rows:
#         return

#     print(matrix[i][j], end=" ")

#     if j == cols - 1:
#         print()
#         display(matrix, rows, cols, i + 1, 0)
#     else:
#         display(matrix, rows, cols, i, j + 1)


# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# print("Enter matrix elements:")

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(int(input()))
#     matrix.append(row)

# print("\nMatrix:")

# display(matrix, rows, cols, 0, 0)
# 3. Program to Perform Addition and Multiplication of Two 2D Arrays
# # Matrix Addition and Multiplication

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# A = []
# B = []

# print("Enter elements of Matrix A")

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(int(input()))
#     A.append(row)

# print("Enter elements of Matrix B")

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(int(input()))
#     B.append(row)

# print("\nAddition of Matrices")

# for i in range(rows):
#     for j in range(cols):
#         print(A[i][j] + B[i][j], end=" ")
#     print()

# print("\nMultiplication of Matrices")

# result = []

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         total = 0
#         for k in range(cols):
#             total = total + A[i][k] * B[k][j]
#         row.append(total)
#     result.append(row)

# for i in range(rows):
#     for j in range(cols):
#         print(result[i][j], end=" ")
#     print()
# 4. Write a Program to Calculate the Transpose of a 2D Array
# # Program to find transpose of a matrix

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# print("Enter matrix elements")

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(int(input()))
#     matrix.append(row)

# print("\nOriginal Matrix")

# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()

# print("\nTranspose Matrix")

# for j in range(cols):
#     for i in range(rows):
#         print(matrix[i][j], end=" ")
#     print()
# Practical 2
# 1. Insert Element in Array
# arr=list(map(int,input("Enter elements: ").split()))
# pos=int(input("Position: "))
# val=int(input("Value: "))
# arr.insert(pos-1,val)
# print(arr)
# 2. Access Matrix Recursively
# def show(a,i,j):
#     if i==len(a): return
#     print(a[i][j],end=" ")
#     if j==len(a[0])-1:
#          print()
#          show(a,i+1,0)
#     else:
#          show(a,i,j+1)

# r,c=map(int,input().split())
# a=[list(map(int,input().split())) for _ in range(r)]
# show(a,0,0)
# #3. Matrix Addition and Multiplication
# r,c=map(int,input().split())
# A=[list(map(int,input().split())) for _ in range(r)]
# B=[list(map(int,input().split())) for _ in range(r)]
# print("Addition")
# for i in range(r):
#      row=[]
#      for j in range(c):
#          row.append(A[i][j]+B[i][j])
#      print(row)

# print("Multiplication")
# for i in range(r):
#      row=[]
#      for j in range(c):
#          s=0
#          for k in range(c):
#              s+=A[i][k]*B[k][j]
#          row.append(s)
#      print(row)
# # 4. Transpose Matrix
# r,c=map(int,input().split())
# a=[list(map(int,input().split())) for _ in range(r)]
# for j in range(c):
#     for i in range(r):
#         print(a[i][j],end=" ")
#     print()
#5. Stack Using List
# stack=[]
# stack.append(10)
# stack.append(20)
# print(stack)
# print("Pop:",stack.pop())
# print(stack)
#Linked List Insertion
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# temp=head
# while temp:
#     print(temp.data,end=" ")
#     temp=temp.next

# Practical 3
# Linear Search
#a=list(map(int,input().split()))
# key=int(input())
# f=False
# for i in range(len(a)):
#     if a[i]==key:
#         print("Found at",i)
#         f=True
#         break
# if not f:
#     print("Not Found")

# Binary Search
# a=sorted(list(map(int,input().split())))
# key=int(input())
# l=0;r=len(a)-1
# while l<=r:
#     m=(l+r)//2
#     if a[m]==key:
#         print("Found")
#         break
#     elif key<a[m]:
#         r=m-1
#     else:
#         l=m+1
# else:
#     print("Not Found")
# Bubble Sort
# a=list(map(int,input().split()))
# for i in range(len(a)):
#     for j in range(len(a)-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# Selection Sort
#a=list(map(int,input().split()))
# for i in range(len(a)):
#     m=i
#     for j in range(i+1,len(a)):
#         if a[j]<a[m]:
#             m=j
#     a[i],a[m]=a[m],a[i]
# print(a)
# Insertion Sort
#a=list(map(int,input().split()))
# for i in range(1,len(a)):
#     key=a[i]
#     j=i-1
#     while j>=0 and a[j]>key:
#         a[j+1]=a[j]
#         j-=1
#     a[j+1]=key
# print(a)
