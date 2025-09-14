# ===============================================================

#       LECTURE : 2 -  Linear Search

# ===============================================================


# Searching in List

# • In Operator → In build operator
# • Index()
# • Search for a value in an iterable.
# • Check if 10 is present inside the list ‘l’
# list = [10,20,30,40]
target = 10
if target in list:
	print("Yes")
else:
	print("No")


# Given  a list , find the index of a target Number.


list = [10,20,30,40,50]
	#[0 , 1,   2  , 3,   4]
print(l.index(40))     #→ Output = 3
print(l.index(500))   #→ value error(500 is not list)
list = [1,2,3,3,4]
print(list.index(3))     #→Output = 2  → Return 1st value of occurrence

# Linear Search

# Given a list of Integers and a target no, find and print index of the target in the list.
list  = [10,20,30,40]
Target = 30
for  i in range(0,len(list)):
	if (list[i] == target): 
		print(i)
		break


# For duplicate do not use break

list  = [10,20,30,30,40,30]
Target = 30
for  i in range(0,len(list)):
	if (list[i] == target): 
		print(i)

# Concatenates  two list

# The + operator, when used with lists in Python, concatenates the lists rather than adding the elements element-wise. 
# Therefore, if you use l1 + l2, you'll get a new list containing the elements of both l1 and l2. 
l1 = [1, 2, 3]           
l2 = [3, 4, 5]
result = l1 + l2
print(result)
result1 = l1 * 3
print(result1)

# Add two list elements

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result = []
for i in range(len(list1)):
   result.append(list1[i] + list2[i])
print(result)


# Error

list1 = [1, 2, 3, 4,4,5]
list2 = [5, 6, 7, 8]
result = []
for i in range(len(list1)):
  result.append(list1[i] + list2[i])
print(result)

# IndexError: list index out of range

