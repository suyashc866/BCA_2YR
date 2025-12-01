# # # # ===============================================================

# # # #       LECTURE : 1 -  (Prefix Sum)

# # # # ===============================================================



# (Prefix Sum)

# Given N array elements & Q queries on the same array.

# For each query calculate the sum of all elements in the given array — [L, R]

# Note: L & R are indices such that L ≤ R.

# arr[10] = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]

# L	R	Sum
# 4	8	9
# 3	7	10
# 1	3	12
# 0	4	14



# solve(int []arr){
#     Q = input()
#     while(Q > 0){
#         L, R = input()
#         # Compute sum from L to R
#         Q--
#     }
# }


# Time Complexity: O(N * Q) (slow for large inputs)





# # ======================================================================

# Q2 – Cricket Score Example (Prefix Sum Concept)

# Given Indian Cricket Team’s score after each over (first 10 overs):

# Over	1	2	3	4	5	6	7	8	9	10
# Score	2	8	14	29	31	49	65	79	88	97
# Examples using prefix sum logic:

# 1. Total runs scored in last over (10th over):
# 97 - 88 = 9

# 2. Total runs in 7th over:
# score[7] - score[6] = 65 - 49 = 16

# 3. Total runs from 6th to 10th overs:
# score[10] - score[5] = 97 - 31 = 66

# 4. Total runs from 3rd to 6th overs:
# score[6] - score[2] = 49 - 8 = 41

# Prefix-Sum Query Formula

# For any inclusive range [I, J]:

# Total = Score[J] - Score[I - 1]


# (Both I and J are included)

