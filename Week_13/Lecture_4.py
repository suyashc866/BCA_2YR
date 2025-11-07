# # ===============================================================

# #       LECTURE : 4 -  Contest and Binary Search

# # ===============================================================


# Contest ID: 8930.  


# GLA_BCA2ndyr_Contest_7



# Take as input N, the size of array. Take N more inputs and store that in an array. Take as input a number M. Write a function which returns the index on which M is found in the array, in case M is not found -1 is returned. Print the value returned.You can assume that the array is sorted, but you’ve to optimize the finding process. For an array of size 1024, you can make 10 comparisons at maximum.
# 1.It reads a number N.
# 2.Take Another N numbers as input in Ascending Order and store them in an Array.
# 3.Take Another number M as input and find that number in Array.
# 4.If the number M is found, index of M is returned else -1 is returned.Print the number returned.
# Input Format
# Constraints
# N cannot be Negative. Range of Numbers N and M can be between -1000000000 to 1000000000



# def binary_search(arr, m):
#     start = 0
#     end = len(arr) - 1
    
#     while start <= end:
#         mid = (start + end) // 2
        
#         if arr[mid] == m:
#             return mid     # Found → return index
#         elif arr[mid] < m:
#             start = mid + 1
#         else:
#             end = mid - 1
    
#     return -1  # Not found

# # Taking input
# n = int(input())  # size of array
# arr = []

# for i in range(n):
#     num = int(input())
#     arr.append(num)

# m = int(input())  # number to search

# # Call function and print result
# print(binary_search(arr, m))

