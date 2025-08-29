# ===============================================================

#       LECTURE : 4 -   Contest -1  (Discussion)


# ===============================================================





# Question :1   Count Digits

# Problem Preview
# Take the following as input.
# A number
# A digit
# Write a function that returns the number of times digit is found in the number. Print the value returned.
# Input Format
# Integer (A number) Integer (A digit)
# Constraints
# 0 <= N <= 1000000000 0 <= Digit <= 9
# Output Format
# Integer (count of times digit occurs in the number)
# Sample Input
# 5433231 
# 3
# Sample Output
# 3
# Explanation
# The digit can be from 0 to 9. Assume decimal numbers.In the given case digit 3 is occurring 3 times in the given number.



number = int(input()) 
digit = int(input())   

count = 0

while number > 0:
    last_digit = number % 10
    if last_digit == digit:
        count += 1
    number //= 10


print(count)




# Test Case 
# Input :- 1
# 1000000000 
# 0 
# Output :- 9

# Input :- 2
# 0
# 1
# Output :-  0

# Input :- 3
# 99999223
# 1
# Output :-  0


# Input :- 4
# 929121319
# 1
# Output :-3
















# Question :2   Star Pattern


# Problem Preview
# Write a program to print given pattern by taking input N.
# Input Format
# The first line contains an integer N.
# Constraints
# Output Format
# Display the pattern as result.
# Sample Input
# 5
# Sample Output
#           * 
#         * * 
#       * * * 
#     * * * * 
#   * * * * * 


s=int(input())
for i in range(1,s+1):
	for j in range(s-i):
		print(" ",end=" ")
	for j in range(i):
		print("*",end=" ")
	print()
	
	
	
	# Test Case 
	# 5
	# 10
	# 19
