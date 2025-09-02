# ===============================================================

#       LECTURE : 2 -  List manipulation

# ===============================================================

# Adding elements
# 	Append()
	
	
# 	#Append()function  → add elements at the end of the list.
list = [5,2,9]
list.append(100)
print(list)
	
	
	
list.append(101,102)
	
	
	
print(list) #→ TypeError: list.append() takes exactly one argument (2 given)
	
	
# Multiple values added using append()

# For the addition of multiple elements with the append() method, loops are used.
List = []
print(List)
 
# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(4)
print(List)     #[1, 2, 4]
 
# Adding elements to the List using Iterator
for i in range(1, 4):
    List.append(i)
print(List)     #[1, 2, 4, 1, 2, 3]
 
# Adding Tuples to the List
List.append((5, 6))
print(List)     #[1, 2, 4, 1, 2, 3, (5, 6)]
 
# Addition of List to a List
List2 = ['Suyash', 'Chaudhary']
List.append(List2)
print(List)    
#[1, 2, 4, 1, 2, 3, (5, 6), ['Suyash', 'Chaudhary']]



# 2.Insert()


#  Insert() method requires two arguments(position, value). 
# Insert (index,value) → Insert value
list = [10,20,30,40]
#Insert value 15 at index 1
list.insert(1,15)
#Output
[10,15,20,30,40]


# insert(100,1990)



# The insert method in Python is used to insert an element at a specific index in a list. 
# If the specified index is beyond the current length of the list, the element will be inserted at the end of the list. In your example, the index 100 is beyond the length of the list l, so the element 1990 will be inserted at the end of the list.
# Here's what the code does:
l = [1, 10, 13]
l.insert(100, 1990)
print(l)


# 3.Exends

# This method is used to add multiple elements at the same time at the end of the list.
# Creating a List
List = [1, 2, 3, 4]
print(List)
 
# Addition of multiple elements to the List at the end
# (using Extend Method)
List.extend([8, 'Suyash', True])
print(List)
# Output:
[1, 2, 3, 4, 8, 'Suyash', True]


# 4.Remove()


list = [10,20,10]
list.remove(10)    #→ Value as argument
list[20,10]  #→ Remove first value.
# Note: Remove method in List will only remove the first occurrence of the searched element.


# 5.Pop()


# It can also be used to remove and return an element from the list, but by default it removes only the last element of the list.
# Pop() → To eliminate a value at a index.
l = [10,20,30,40]
l.pop()   #→ Remove the last value.
print(l)   #→[10,20,30]
# ==================
# To remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.
#Remove the value at index 2
l = [11,12,13,14,15]
l.pop(2)   #→ #Index as argument
#Output
[11,12,14,15]  


# Reverse()

# Method 1:  A list can be reversed by using the
# Reverse() Method
mylist = [1.4, 2, 3, 4, 5, 'Python']
mylist.reverse()
print(mylist)



# Reversed()


# The reversed() function returns a reverse iterator, which can be converted to a list using the list() function.

my_list = [1, 2, 3, 4, 5]
reversed_list = reversed(my_list)
#<list_reverseiterator object at 0x101ee4eb0>
print(reversed_list)

reversed_list = list(reversed(my_list))
print(reversed_list)



# Difference 

# Reverse is a method that operates in-place on a list, modifying the original list, 
# While Reversed is a built-in function that returns a reversed iterator without modifying the original iterable.
# 	• Time Complexity: O(n) - linear
# 	• Space Complexity: O(1) - constant
# When using a[::-1] in Python to reverse a list a, it creates a reversed copy of the list without modifying the original list.
# 	• Time Complexity: O(n)
# 	• Space Complexity: O(n)



# Reverse a list by swapping


list1 = [1, 2, 3, 4, 5, 6]
N = len(list1)
for i in range(0, N // 2):
   list1[i], list1[N - 1 - i] = list1[N - 1 - i], list1[i]
print(list1)






	
