



# Range() Method


# The range method / function is used to generate a range of integers.
# range(start, end, step)   #end is not include
# Default value start =0 step = 1
# range(6) →[0,1,2,3,4,5]
# range(2,8) →[2,3,4,5,6,7]
# range(-1,10,2) →[-1,1,3,5,7,9]
# range(10,1,-2) → [10,8,6,4,2]

print(range(0,6))    # → range(0,6)
# Using list() to convert range to a list:
print(list(range(0,6))) #→[0,1,2,3,4,5,6]
# 	• start (optional): The starting value of the sequence (default is 0).
# 	• stop: The end value of the sequence. The generated sequence includes all values up to, but not including, this value.
#      step (optional): The step size between values in the sequence (default is 1).


# For Loop


# Loop that is used to iterate/loop over an iterable.
# Iterable is an object which can be looped over or iterated over with the help of a for loop.
#  Objects like range ,lists, tuples, sets, dictionaries, strings, etc. are called iterables. 
# In short and simpler terms, iterable is anything that you can loop over.


# Syntax

for i in range(1,10,2):
	print(i)
for i in range(1,10,2):
	print(i*i , end= " ")

# Print all integers from 1 to N

N = int(input())
for i in range(1, N + 1):
	print(i)


# Print all odd integers from 1 to N


for i in range(1,N+1,2):
	print(i, end=" ")


# Power

# a^b 
# a= 3 , b= 2,  ans →9


a = int(input())
b = int(input())
ans = 1
for i in range(b):
	ans = ans * a
print(ans,end=" ")


# Break Statement 


# Used to break out of the enclosing loop.


for i in range(100):
	print(i,end=" ")
	if (i == 50):
		break
# Output:- 0 to 50


# Continue Statement


# Skip the iteration
# Print 1 to 20 Skip the multiple of 3.
for i in range(1,21):
	if(i % 3 == 0):
		continue
	print(i, end=" ")


# Random Game
# Generate and print random nos from 1 to 10 until you reach 5
import random 
while True:
	X = random.randint(1,10)
	if (X == 5):
		break
	print(X , end = " ")
# infinite loop Possible → while True
#Both (1,10 ) are include.



# Skip the multiple of 4


import random 
while True:
	X = random.randint(1,10)
	if (X % 4 == 0):
		continue
	print(X, end =" ")
	if (X == 5):
		break
	print(X , end = " ")

