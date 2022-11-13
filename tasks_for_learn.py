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

# Question 8

'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# my_list = sorted(list(input('Enter your words using coma \n').split(',')))
# print(','.join(my_list))
#
# def my_func(e):
#     return e[0]
#
# my_list = input('Enter a comma separated string: ').split(",")
# my_list.sort(key=my_func)
# print(",".join(my_list))

# Question 9
'''
Write a program that accepts sequence of lines as input and 
prints the lines after making all characters in the sentence capitalized.

'''
# text = list(input('to separate line use come ').split(','))
# test_list = []
# for i in text:
#     test_list.append(i.upper())
#
# print('\n'.join(test_list))

# def user_input():
#     while True:
#         x = input()
#         if not x:
#             break
#         yield x
# print(*(line.upper() for line in user_input()), sep='\n')

# Question 10
'''
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
'''
# word1 = set(input().split(' '))
# list(word1).sort()
# print(' '.join(word1))
#
# word2 = sorted(list(set(input().split())))
# print(' '.join(word2))
#
# word3 = input().split()
# for i in word3:
#     if word3.count(i) > 1:
#         word3.remove(i)
#
# word3.sort()
# print(" ".join(word3))

# Question 11

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as 
its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Answer:1010
'''

# my_list = input().split(',')
#
#
# def bin2dec(s):
#     i = 0
#     d = 0
#     while len(s) > 0:
#         d = d + int(s[-1]) * 2 ** i
#         i = i + 1
#         s = s[:-1]
#     return d
#
# print(*(i for i in my_list if bin2dec(i) % 5 == 0), sep=',')
# a = '0100'
# x = int(a,2)
# print(x)

# Question 12

'''
Write a program, which will find all such numbers between 1000 and 3000 (both included)
 such that each digit of the number is an even number.
 The numbers obtained should be printed in a comma-separated sequence on a single line.
 
 Hint: In case of input data being supplied to the question, it should be assumed to be a console input
'''
# selected_value = []
# for i in range(1000, 3001):
#     check = 0
#     for x in str(i):
#         if ord(x) % 2 != 0:
#             check = 1
#     if check == 0:
#         selected_value.append(str(i))
# print(','.join(selected_value))
#
# selected_value1 = [str(i) for i in range(1000, 3001)]
# selected_value1 = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), selected_value1))
# print(",".join(selected_value1))

# Question 13
'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
Answer:
LETTERS 10
DIGITS 3
'''
# our_str = input()
# letters = 0
# digits = 0
# for i in our_str:
#     if i.isdigit():
#         digits +=1
#     elif i.isalpha():
#         letters +=1
# print(f'LETTER {letters} \nDIGIT {digits}')
#
# import re
#
# input_string = input('> ')
# print()
# counter = {"LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS":len(re.findall("[0-9]", input_string))}
#
# print(counter)

# Question 14
'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world!
Answer: 
UPPER CASE 1
LOWER CASE 9
'''
# my_input = input('Enter data:\n')

# def summ_upper_low(some_str):
#     upper_case = 0
#     lower_case = 0
#     for i in some_str:
#         if i.isalpha() and i.islower():
#             lower_case += 1
#         elif i.isalpha() and i.isupper():
#             upper_case += 1
#     print(f'Upper case {upper_case} \nLower case {lower_case}')
#
# summ_upper_low(my_input)

# Question 15
'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9
Then, the output should be: 11106
'''
# from functools import reduce
#
# x = input('please enter a digit:')
# print(reduce(lambda x, y: int(x) + int(y), [x*i for i in range(1,5)]))
#
# sum = 0
# for i in range(1,5):
#     sum = sum + int(x*i)
# print(sum)