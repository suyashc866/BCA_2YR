# # ===============================================================

# #       LECTURE : 4 -  Noble integer

# # ===============================================================



# Noble Integer

# Given N array elements of unique numbers, Calculate number of Noble integers present in it.
# A[i]  is said to be Noble if 

# 	(No of elements < A[i])  = A[i]
	
	
	
	
# Example :

# Arr [ ]                        =         1     -5    3    5     -10    4

# Count of elements  < Arr[i]   =           2     1    3     5     0      4

# Ans = 3
	
	
	

# Example :

# Arr []                           = -3  0   2  5

# Count of elements  < Arr[i]     =   0  1   2  3

# Ans = 1


		
# Example :

# Arr []                        = -10  -5  1  3  4  5  10

# Count of elements  < Arr[i]   =  0    1    2  3  4  5   6

# Index                         =  0   1    2  3  4  5   6

# Ans = 3

	
	
	
	
	
# Brute Force Idea
# For every element , Check if its noble


# ans  = 0

# for (i = 0 ; i < N ; i++){
#     C = 0 
#     for (j = 0 ; j < N ; j ++){
#         If (arr[j] < arr[i]){
#             C += 1
#         }
#     }
#     If (arr[i] == C){
#         ans  = ans + 1
#     }
# }


# TC  = O(N^2)
# SC =  O(1)

	
	
# Optimisation
# Sort the array 

# Ans = 0

# N = A.length

# A.sort()

# for (i = 0 ; i < N ; i++){
    
#     If (A[i] == i){
    
#         Ans = ans + 1
        
#     }
# }
# return ans
    

# TC  = O(Nlogn)
# SC =  O(1)
	
