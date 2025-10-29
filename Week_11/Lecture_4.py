# # ===============================================================

# #       LECTURE : 4 -  Subarray 

# # ===============================================================



# # Lecture 1(Subarray)


# # Subarray 
# # Continuous part of an array is called a Subarray
# # A single element is a Subarray
# # Entire subarray is called a Subarray.
# # Empty cannot be a Subarray.

# # Count of subarray

# # Arr = [4, 2, 10, 3, 12, -2, 15]


# # Subarray staring from index 0 → 7
# # Subarray staring from index 1 → 6
# # Subarray staring from index 2 → 5 …

# # Given  N array elements , How many subarray can be generated?

# # N*(N+1) /2



# # 1.Print all the values of the subarray



# # Function printSubarray(array, startIndex, endIndex):
# #     For i from startIndex to endIndex:
# #         Print array[i]
# #     EndFor
# # EndFunction
# # =============================
# # def print_subarray(arr, start, end):
# #    for i in range(start, end + 1):
# #        print(arr[i])

# # arr = [1, 2, 3, 4, 5, 6, 7]
# # N = len(arr)
# # print_subarray(arr, 0, N-1)
# # =============================

# # 2.Find the sum of all the elements in a given subarray



# # Function findSubarraySum(array, startIndex, endIndex):
# #     sum = 0  
# #     For i from startIndex to endIndex:
# #         sum = sum + array[i]  
# #     EndFor
# #     Return sum  
# # EndFunction
# # =================================
# # def addSubarray(A, start, end):
# #   s = 0
# #   for i in range(start , end + 1):
# #       s += A[i]
# #   return s
# # arr = [1, 2, 3, 4, 5, 6, 7]
# # N = len(arr)
# # res = addSubarray(arr, 0, N-1 )
# # z
# def printSubarry(A, start, end):
#    for i in range(start, end+ 1):
#        print(A[i], end = " ")
#    print()
# def printAllSubarray(A):
#    N = len(A)
#    for i in range(N):
#        for j in range(i,N):
#            printSubarry(A, i, j)
# A = [1, 2, 3]
# printAllSubarray(A)
# ============================================
# 4.Print Sum of every single subarray

# # 



# ==================================
# def addSubarray(A, start, end):
#    s = 0
#    for i in range(start , end + 1):
#        s += A[i]
#    return s

# def subarraySum(A):
#    N = len(A)
#    for i in range(N):
#        for j in range(i , N):
#            ans = addSubarray(A, i , j)
#            print(ans)
# A = [3 ,-2 , 4]
# subarraySum(A)

# ==================================

