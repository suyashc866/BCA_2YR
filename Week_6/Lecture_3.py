# ===============================================================

#       LECTURE : 2 -  List Split and Map Fucnction

# ===============================================================

# Split function

# Python String split() method splits a string into a list of strings after breaking the given 
# string by the specified separator.
# Split function alway create a new list.
# Return a list


# Example

s = "Hello everyone how are you"
print(s.split())
#['Hello', 'everyone', 'how', 'are', 'you']
s = "Hello-everyone-how are you"
print(s.split("-"))
#['Hello', 'everyone', 'how are you']
word = 'Suyash:Chaudhary:Noida' 
# Splitting at ':'
print(word.split(':'))   #[“Suyash” , “Chaudhary”, “Noida”]
 
 


t = "5321"
print(t.split())     
Output = [5321]

t = "5 3 2 1"
print(t.split()) 
Output = ['5', '3', '2', '1']


# Map function()


# The map function applies a  given function to each item of an iterable (list,tuples etc)
# and return an iterator.
# map(func,iter)
# iter → iterable → (list,tuple,sets,dict)


# Explanation

# • input(): This function takes user input as a string.
# • split(): This method is used to split the input string into a list of substrings based on whitespace by default.
# • map(int, ... ): The map() function is used to apply the int function to each element of the resulting list from the split() method. This is done to convert the substrings (which are initially strings) into integers.
# list(...): Finally, the list() function is used to convert the resulting map object into a list.


# Reading List input

A=list(map(int,input().split()))
print(A)
m = map(int,input().split())
print(m)    #<map object at 0x105e0af40>

A=list(map(int,input().split()))
for i in range(0,len(A)):
   print(A[i])


# Dry run 

i = input()
print(i)       #1 2 3 4 5
# —--------
s = i.split()
print(s)     #['1', '2', '3', '4', '5']
# —--------
m = map(int,s)
print(m)      #<map object at 0x105d30670>
# —----------
A=list(m)
print(A)           #[1 , 2, 3, 4, 5]
# —---------------
for i in range(0,len(A)):
  print(A[i],end=" ")  #1 2 3 4 5


# Challenge:-1
# Given an array compute the sum of all elements


arr = [1, 2, 3, 4, 5]            # sum = 15
ans  = 0
for  i in arr:
	ans = ans + i
print(ans)


# Challenge:-2
# Given an array, find the maximum value in it.

arr = [5, 10, 1, 3]
ans = -float("inf")
for i in arr:
	if (ans < i):           # or ans = max((ans,x))  
		ans = i  
print(ans)





