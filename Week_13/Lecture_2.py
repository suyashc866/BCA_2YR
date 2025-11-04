# # ===============================================================

# #       LECTURE : 2 -  Recursion

# # ===============================================================




# Dolls -   https://www.youtube.com/watch?v=HnDij14xXBA



# Observation -  
# 	• Size Keep decreasing 
# 	• Similar dolls
# 	• End doll

#  Recursion -occurring again periodically or repeatedly.
# Solving a problem using smaller instance Of the same problem(Sub problem )




# Definition

#  Function Calling Itself. 
# 	• Recursion is a programming technique where a function calls itself directly or indirectly in order to solve a problem. 
# 	• In a recursive function, the function makes one or more calls to itself as a part of its execution. 
# 	• The process continues until a base case is reached, at which point the function stops calling itself and returns a result.
# Recursion can be visualized as a problem being divided into smaller, similar sub-problems, and the function calling itself to solve these sub-problems.
#  Each recursive call typically works on a smaller input, eventually leading to the base case(s) where the function returns a result without making further recursive calls.

# Why to use Recursion 
# Readability
# Simplifying Complex Problems
# Reduced Code Length
# Divide and Conquer Paradigm
# Handling Tree-like Structures

# Sum of natural number (Regular function)



# STEPS
# Make an assumption - Decide what your function does and trust that it will do it.
# Main logic - Solve the bigger problem using subproblem
# Base Case  - When your recursion Stop.



# Function to find sum of first n natural numbers
def sum_natural(n):
    if n == 0:     # base case
        return 0
    else:
        return n + sum_natural(n - 1)   # recursive case

# main code
n = int(input("Enter a positive integer: "))
print("Sum of first")


# factorial using recursion

# Function to find factorial using recursion
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)   # recursive case

# main code
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))
