# ===============================================================

#       LECTURE : 1 -  List Introduction

# ===============================================================


# Lists

# Lists are used to store multiple items in a single variable 
# • Lists are created using square brackets[ ].
#  • List items are ordered, changeable, and allow duplicate values.
#  • List items are indexed, the first item has index [0], the second item has index [1] etc.
#  •The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. 


# List size
# In Python, lists can grow dynamically, and they can be of virtually any size limited only by the available memory of your system. 
# Python lists are not fixed in size; you can keep adding elements to them as needed. 
# The dynamic resizing of lists is handled internally by the Python interpreter.




# List v/s Array
# A list in Python is an inbuilt collection of items that can contain elements of multiple data types,
# which may be either numeric, character logical values, etc.
# An array  is containing homogeneous elements i.e. if of the same data type.



# Creating a list in Python
# # Creating a Empty List 
List = []
print("Empty List: ")
print(List)


 
# Creating a List of numbers
List = [10, 20, 14]
print("List of numbers: ")
print(List)


# Creating a list with multiple distinct or duplicate elements.
 

# Creating a List with mixed type of values
List = [1, 2, 'Python', 4, 'and', 6,]
print(List)

# Creating a List with duplicates 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print(List)


# Indexing  and Accessing elements in list

list  = [ 2, 4.0, True , [5,10], "Python"]
# Index  [ 0,   1,      2 ,    3,         4]   ÷

print(list)       #→[ 2, 4.0, True , [5,10]]
print(list[1])   #→ 4.0

print(list[3])   #→ [5,10]
print(list[10]) #→Index Error: list index out of range

# Access list inside list

list  = [ 2, 4.0, True , [5,10], "Python"]
# Index  [ 0,   1,      2 ,    3,         4]   
print(list[3][0])     # → 5
print(list[3][1])      # → 10


names  = ["Python" , "Meera", "Aarush"]
print(names[0][0])   #→”P”
print(names[1][2])  # →”e”


# Update value in list

list  = [ 2, 4.0, True , [5,10], "Python"]
# Index  [ 0,   1,      2 ,    3,         4]   
list[2] = 100
print(list[2])


# Negative Index

list  = [ 2, 4.0, True , [5,10], "Python"]
# Index =     [ 0,   1,      2 ,       3,           4]   
# --ve Index = [ -5,   -4,      -3 ,    -2,         -1] 

list[1] == list[-4]     #→ 4.0
list[-1] == list[4]     #→ “Python”
List[-10] #→ Index Error: list index out of range



# Length of list


list  =        [ 2, 4.0, True , [5,10], "Python"]
Index =     [ 0,   1,      2 ,    3,         4]   
print(len(list))   # →5
L = []
print(len(list)) # →0 # empty list








