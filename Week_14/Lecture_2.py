# # ===============================================================

# #       LECTURE : 2 -   Bit manipulation

# # ===============================================================

# Single Number

# Problem Statement:
# Given N array elements, every element repeats twice except 1.
# Find the unique element.

# Examples:

# [5] = 6 9 6 10 9   → 10  
# [7] = 12 9 12 8 7 9 8  → 7  
# [5] = 2 9 7 2 7   → 9



# Brute Force Idea

# For every element, iterate over the array and get its frequency.

# If frequency == 1 → ans = a[i]

# Time Complexity: O(N²)
# Space Complexity: O(1)




# Optimized Idea

# Concept: Take XOR of all elements.

# Steps:

# Take ans = 0

# Iterate and do ans = ans ^ a[i]




# Why XOR works:

# a ^ a = 0

# a ^ 0 = a

# Example:

# [5] = 2 9 7 2 7

# ans = 0
# ans ^ 2 = 2
# ans ^ 9 = 11
# ans ^ 7 = 12
# ans ^ 2 = 14
# ans ^ 7 = 9   → unique element = 9

# Code Implementation


# def singleNumber(arr):
#     ans = 0
#     n = len(arr)

#     for i in range(n):
#         ans = ans ^ arr[i]

#     return ans
# arr = [2, 9, 7, 2, 7]
# print(singleNumber(arr))


# Time Complexity: O(N)
# Space Complexity: O(1)
