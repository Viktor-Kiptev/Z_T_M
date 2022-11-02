# Question 1

# """
# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#  Hint: Consider use range(#begin, #end) method.
# """
# my_list = []
# for item in range(2000, 3201):
#     if item % 7 == 0 and item % 5 != 0:
#         my_list.append(item)
# print(my_list)
#
# print(list(filter(lambda item: item % 7 == 0 and item % 5 != 0, range(2000, 3201))))
#
# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

# Question 2

# """
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
# """
# import math
#
# n = int(input('Enter num for factorial '))
# n1 = n
#
# print(math.factorial(n))
#
# factorial1 = 1
# for i in range(2, n + 1):
#     factorial1 *= i
# print(factorial1)
# factorial2 = 1
#
# while n > 1:
#     factorial2 *= n
#     n -= 1
# print(factorial2)
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n
#
#
# print(factorial(n1))

# Question 3

# """
# With a given integral number n, write a program to generate a dictionary that contains
# (i, i x i) such that is an integral number between 1 and n (both included). and then
# the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hint: In case of input data being supplied to the question,
# it should be assumed to be a console input.Consider use dict()
# """

# try:
#     your_num = int(input('Enter your number to create new dict '))
# except ValueError as err:
#     print(f'Use number {err}')
#
#
# def create_dict(num):
#     test_dict = {}
#     my_range = range(1, num + 1)
#     for i in my_range:
#         test_dict.update({i: i * i})
#     return test_dict
#
#
# print(create_dict(your_num))
#
#
# def create_dict2(num):
#     test_dict = {}
#     my_range = range(1, num + 1)
#     for i in my_range:
#         test_dict[i] = i * i
#     return test_dict
#
#
# print(create_dict2(your_num))
#
# test_dict2 = {i: i * i for i in range(1, your_num + 1)}
# print(test_dict2)
#
# print(dict(enumerate([i * i for i in range(1, your_num + 1)], 1)))

# Question 4

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
# In case of input data being supplied to the question,
# it should be assumed to be a console input.tuple() method can convert list to tuple


# def return_list_and_tuple(counter):
#     my_list = []
#     while counter != 0:
#         try:
#             my_list.append(int(input(f'Enter your data for list left {counter} \n')))
#             counter -= 1
#         except ValueError as err:
#             print(f'Use number {err}')
#     my_tuple = tuple(my_list)
#     return my_list, my_tuple
#
#
# print(return_list_and_tuple(6))

# my_list2 = list(input('Enter your data ').split(','))
# my_tuple2 = tuple(my_list2)
# print(my_list2, my_tuple2)

# Question 5

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints: Use init method to construct some parameters

# class MyString():
#
#     def __init__(self):
#         self.x = ''
#
#     def get_string(self):
#         self.x = input('Enter your string \n')
#
#     def print_string_uper(self):
#         print(self.x.upper())
#
#
# test_str = MyString()
# test_str.get_string()
# test_str.print_string_uper()
# print(test_str)

# Question 6

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.For example Let us assume the following comma separated input sequence is
# given to the program: 100,150,180
# The output of the program should be: 18,22,24

# Hint: If the output received is in decimal form, it should be rounded off
# to its nearest value (for example, if the output received is 26.0, it should be printed
# as 26).In caseof input data being supplied to the question,
# it should be assumed to be a console input.

# from math import sqrt

# c = 50
# h = 30
# my_list = input('Enter values using coma ').split(',')
# new_list = []
# for d in my_list:
#     new_list.append(str(round(sqrt((2 * c * int(d) / h)))))
# print(','.join(new_list))

# Qestion 7
'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i _ j.*
Note: i=0,1.., X-1; j=0,1,¡Y-1. Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hint: Note: In case of input data being supplied to the question, 
it should be assumed to be a console input in a comma-separated form.
'''

# x,y = map(int,input('enter values').split(','))
# my_list = []
#
# for i in range(x):
#     tmp = []
#     for j in range(y):
#         tmp.append(i*j)
#     my_list.append(tmp)
#
# print(my_list)