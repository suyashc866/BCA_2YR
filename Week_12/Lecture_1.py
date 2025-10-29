# # ===============================================================

# #       LECTURE : 1 -  Kadane's Algorithm 

# # ===============================================================



# (Kadane's Algorithm )


# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

# Output: 6

# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.


# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.




# Kadane's Algorithm is an efficient method for finding the maximum sum of a contiguous subarray in a 1D array of integers.






# ====================================================================

# function maxSubArray(nums):

#     max_current = nums[0]
   
#     max_global = nums[0]   
     
#     for i from 1 to length(nums) - 1:
        
#         max_current = max(nums[i], max_current + nums[i])
        
#         if max_current > max_global:

#             max_global = max_current

#     return max_global

# ===================================================



# def maxSubArray(nums):
#     max_current = nums[0]
#     max_global = nums[0]
    
#     for i in range(1, len(nums)):
#         max_current = max(nums[i], max_current + nums[i])
#         if max_current > max_global:
#             max_global = max_current

#     return max_global


# Nums = [1,2,3,4,-10]



