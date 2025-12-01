# # ===============================================================

# #       LECTURE : 2 -  Sorting

# # ===============================================================



# What is Sorting?

# Sorting means arranging items in ascending or descending order,
# or arranging based on some parameter.

# Example parameters:

# Sort a deck of cards → by Value, Color, Suits

# Examples:

# 3 8 9 14 19 → Ascending by value

# 19 14 9 8 3 → Descending by value

# 1 5 3 9 6 10 12 → Ascending by number of factors

# Factors count: 1 2 2 3 4 4 6

# Inbuilt Sort Methods
# Java
# Arrays.sort(A);

# Python
# A.sort()

# Time Complexity

# To sort an array of N items:

# TC = O(N log N)



# ---------------------------------------------------------------------

# Min Cost to Remove All Elements

# Given N array elements, at every step you must remove one element.

# Cost of removing an element = Sum of all elements currently present in the array

# Goal → Find the minimum total cost to remove all elements.

# Example 1
# Arr = [2, 1, 4]


# Step-by-step removal:

# Remove	Array State	Cost (sum of elements)
# 1	     [2, 1, 4]	2 + 1 + 4 = 7
# 2	     [2, 4]	2 + 4 = 6
# 4	     [4]	4

# Total Cost = 7 + 6 + 4 = 17

# Example 2
# Arr = [4, 6, 1]


# (You can compute using same logic after sorting)

# Example 3
# Arr = [3, 5, 1, -3]

# Observation (Very Important!)

# To get minimum cost,
# we must remove elements in descending order of their values.

# Reason:

# Consider sorted descending:

# [a, b, c, d]   where a ≥ b ≥ c ≥ d


# Cost breakdown:

# Step	Remaining Elements	Cost
# Remove a	a b c d	    a + b + c + d
# Remove b	b c d	    b + c + d
# Remove c	c d	        c + d
# Remove d	d	        d

# Total Cost:
# = a + (b+b) + (c+c+c) + (d+d+d+d)
# = a + 2b + 3c + 4d


# This is minimum because larger values are removed earlier.

# Pseudocode
# Sort the array in descending order   // O(N logN)

# cost = 0

# for i = 0 to N-1:
#     cost = cost + arr[i] * (i + 1)

# return cost

# Time & Space Complexity
# TC = O(N log N)
# SC = O(1)


