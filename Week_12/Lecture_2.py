# # ===============================================================

# #       LECTURE : 2 -  Contribution Technique

# # ===============================================================




#  (Contribution Technique)

# Given an array , find the sum of all subarray sums.



def totalSubarraySum(A):
    n = len(A)
    total_sum = 0
    
    for i in range(n):
        contribution = A[i] * (i + 1) * (n - i)
        total_sum += contribution

    return total_sum



A = [1, 2, 3]
print(totalSubarraySum(A))  
