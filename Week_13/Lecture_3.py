# # ===============================================================

# #       LECTURE : 3 -  Problems on Recursion

# # ===============================================================



# 1. Print numbers from 1 to N

# Print numbers from 1 to N
# Problem:
#  Using recursion, print numbers from 1 to N.
# Input Format:
#  A single integer N.
# Output Format:
#  Print numbers from 1 to N separated by a space.
# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5


def print1toN(n):
    if n == 0:
        return
    print1toN(n - 1)
    print(n, end=" ")
# Input
n = int(input())
print1toN(n)

# 2. Print numbers from N to 1

# Problem:
#  Using recursion, print numbers from N to 1.
# Input Format:
#  A single integer N.
# Output Format:
#  Print numbers from N to 1 separated by a space.
# Sample Input:
# 5
# Sample Output:
# 5 4 3 2 1


def printNto1(n):
    if n == 0:
        return
    print(n, end=" ")
    printNto1(n - 1)
	# Input
n = int(input())
printNto1(n)

#  3. Find Nth Fibonacci number

#  Find Nth Fibonacci number
# Problem:
#  Write a recursive function to find the Nth Fibonacci number.
# Input Format:
#  A single integer N.
# Output Format:
#  Print the Nth Fibonacci number.
# Sample Input:
# 6
# Sample Output:
8


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
# Input
n = int(input())
print(fib(n))



# 4. Sum of digits of a number

# Sum of digits of a number
# Problem:
#  Find the sum of the digits of a given number using recursion.
# Input Format:
#  A single integer N.
# Output Format:
#  Print the sum of its digits.
# Sample Input:
# 1234
# Sample Output:
# 10


def sumOfDigits(n):
    if n == 0:
        return 0
    return (n % 10) + sumOfDigits(n // 10)
# Input
n = int(input())
print(sumOfDigits(n))

#  5.Reverse a string using recursion

#  Reverse a string using recursion
# Problem:
#  Write a recursive function to reverse a string.
# Input Format:
#  A single string S.
# Output Format:
#  Print the reversed string.
# Sample Input:
# hello
# Sample Output:
# olleh


def reverseString(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverseString(s[:-1])
# Input
s = input()
print(reverseString(s))
