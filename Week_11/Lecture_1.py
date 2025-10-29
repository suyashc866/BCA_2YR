# # ===============================================================

# #       LECTURE : 1 -   Scope 

# # ===============================================================






# Sheet - 9 Functions - 2
# By:- Suyash Chaudhary
# 1.Keyword argument
# Define a function in Python Introduce , providing their name, age, and profession as arguments.

# 2.Default argument
# WAP to define and utilize a Python function named introduce to print out information about
# individuals, including their name, age, and profession, with an optional default value for the
# profession parameter.

# 3. What is Error in this code and how can we correct this code?
# def pythagoras(a,b):
# return square(a) + square(b)
# c2 = pythagoras(3,4)
# def square(x):
# return x * x
# print("c2 = "
# , c2)


# 4.What is the output of this code and tell a variable “lang “ is in local or global
# scope?
# def local():
# lang = "Python"
# print(lang)
# local()


# 5.What is the output of this code and tell a variable “lang “ and “name” is in local
# or global scope?
# name = "Suyash"
# def test():
# print(name)
# lang = "Python"
# print(lang)
# test()
# print(name)


# 6.What is Error in this code and how can we correct this code?
# def test():
# lang = "Python"
# print(lang)
# test()
# print(lang)


# 7.What is Error in this code and how can we correct this code?
# name = "Suyash"
# print(name)
# def fun():
# print(name)
# name = "Chaudhary"
# lang = "Python"
# print(lang)
# fun()
# print(name)



# 8.What is the output of this code?
# name = "Suyash"
# print(name)
# def test():
# global name
# print(name)
# name = "Chaudhary"
# print(name)
# test()
# print(name)


# 9.What is the output of this code?
# name = "abc"
# print(name)
# def fun1():
# name = "def"
# print(name)
# print(name)
# fun1()
# def fun2():
# global name
# name = "ghi"
# print(name)
# print(name)
# fun2()
# print(name)



# 10.What is the output of this code?
# def fun1():
# name = "Suyash"
# def fun2():
# name = "Chaudhary"
# fun2()
# print(name)
# fun1()


# 11.What is the output of this code?
# def fun1():
# name = "Suyash"
# def fun2():
# nonlocal name
# name = "Chaudhary"
# fun2()
# print(name)
# fun1()


# 12.Square of that integer using a lambda function
# You want to create a Python program that takes an integer input, calculates the square of that
# integer using a lambda function, and then prints the result.
# Input :
# a= 4
# Output:
# 16




# 13.Odd and Even No
# Write a Python program that performs the following tasks:
# Accepts an integer input from the user and stores it in a variable num.
# Defines a lambda function even_odd_No that takes one parameter num and returns "even"
# if num is even, otherwise it returns "odd".
# Calls the lambda function even_odd_No with the input num and prints the result.
# Provide the Python code to implement the above requirements.



# 14.Max of two No.
# Write a Python program that defines a lambda function called Max that takes two parameters a
# and b, and returns the maximum of the two values. Then, call the lambda function Max with the
# values 1 and 2, and print the result obtained from the call in a single line of code.



# 15.Max of three No.
# Create a Python program that accomplishes the following tasks:
# Define a lambda function max_of_three that takes three parameters a, b, and c, and
# returns the maximum of the three values.
# Call the lambda function max_of_three with three integer values.
# Print the result obtained from calling the lambda function.
# NOTE:- Try to Solve this question with if-else.



# 16.Filter Even No
# Write a Python program that defines a function fun(a) which takes an integer a as input and returns
# True if a is even, otherwise it returns False. Then, create a list called sequence containing integers
# and floating-point numbers. Use the filter() function along with the fun function to filter out the
# even numbers from the sequence list, and store the filtered values in a new list called filtered.
# Finally, print the filtered list.



# 17.Filter Even No with lambda fucntion
# Create a Python program that accomplishes the following tasks:
# Define a list arr containing integer values.
# Use the filter() function with a lambda function to filter out the even numbers from the list
# arr.
# Store the filtered values in a variable ans.
# Print the ans list.



# 18.Filter Numbers Greater Than 60
# Write a single line of Python code that accepts a list of integer values from the user, filters out
# the numbers greater than 60 using the filter() function with a lambda function, and stores the
# filtered values in a variable ans. Print the ans list.



# 18.Add 10 to Each Element of a List Using Map and Lambda Function
# Create a Python program that accomplishes the following tasks:
# Define a list arr containing integer values.
# Use the map() function with a lambda function to add 10 to each element of the list arr.
# Store the modified values in a variable ans.
# Print the ans list.



# 19.Convert Names to Lowercase Using Map and Lambda Function
# Create a Python program that accomplishes the following tasks:
# Define a list names containing string values.
# Use the map() function with a lambda function to convert each name in the list names to
# lowercase.
# Store the modified names in a variable result.
# Print the result list.



# 20.Python Program Using map, filter, and lambda Functions
# Write a Python program that utilizes the map, filter, and lambda functions to achieve the following
# objectives:
# Use map to convert a list of integers to their corresponding squares.
# Use filter to keep only the squared numbers that are multiples of a specific number.