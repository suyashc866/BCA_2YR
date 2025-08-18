# ===============================================================

#     LECTURE : 4 - Python Comments and Taking Input from user

# ===============================================================




# Comments 

# Comments in Python are just short descriptions along with the code. It is used to increase the readability of a code.

# They are just meant for the developers to understand a piece of code. Python interpreter completely ignores comments in Python.

# A single-line comment in Python begins with a hash mark ( # ) and whitespace character and continues to the line's end.

# ===============================================================



# What are Comments in Python Used For?

# Learning to write comments in Python is also a valuable skill. There are several reasons why comments in Python are used

# Some of them are-

# 	• Explaining the code.
	
# 	• Making the code more readable.
	
# 	• Preventing execution while testing code.

# 	• Enhance code readability
	
# 	• Explaining code to other
	
# 	• Understanding code if studied after some time
	
# 	• Documenting the steps and needs for a function
	
# 	• Sharing code with fellow developers
	
#       Collaborating with multiple people



# ===============================================================




# Different Types of Comments in Python



# There are three types of comments in Python:

# 	• Single line Comments
	
# 	• Multiline Comments
	
# 	• Docstring Comments


# ===============================================================




# 1. Single-Line Comments in Python



# The single-line comments in Python are denoted by the hash symbol “#” and include no white spaces. As the name suggests, this kind of 

# comment can only be one line long. They come in handy for small explanations and function declaration



# ===============================================================

# 2. Multi-Line Comments in Python



# Python does not have multi-line comments, but there are two ways we can achieve this –

# 	• You can write “#” at the beginning of every line you wish to comment out. This stimulates multi-line comments in Python. 


	
# 	#Multi
	
# 	#line
	
# 	#Comments
	
# 	#In Python
	
	
	
# 	• For including multi-line comments in Python, we make use of the delimiter (""")




#    """

#    If you do not want to type # every time for 

#    every line, you can make use of 

#    delimiters!
#  """



# ===============================================================




# 3. Docstring Comments in Python



# def intro():  

#   """ 

# 	This function prints Welcome to Python
	
#   """  
#  print("Introduction Python")   
           
# print(intro.__doc__)



# ===============================================================



# Right Way to write comments in Python



# 	• Comments should be short and precise.

# 	• Use comments only when necessary, don’t clutter your code with comments.

# 	• Comment should have some meaning.

# 	• Avoid writing generic or basic comments.

#     Write comments that are self explanatory.



# ===============================================================




# Taking Input from User in Python

# The programs were not too interactive as we had hard-coded values of the variables. 

# Sometimes, users or developers want to run the programs with their own data in the variables for their own ease.

# To execute this, we will learn to take input from the users, in which the users themselves will define the values of the variables.


# The syntax for this function is as follows:

# input('prompt ')

# Here, prompt is the string we want to display while taking input from the user. This is optional.

# ===============================================================


name = input("Enter your name")

print(name)

print(type(name))

# ===============================================================

number = int(input("Enter your age"))

print(number)

print(type(number))



