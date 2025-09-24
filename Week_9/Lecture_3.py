
# ===============================================================

#       LECTURE : 3 -   Functions


# ===============================================================



# Examples

# Let me give you 2 Books
# Book 1 => 300 pages , No indexing / Chapters/no Heading/No modules
# Book 2 => 500 pages, (divided by chapter and modules and proper index)
# Book has same content 
# Which book will you refer ?
# 2 book because this book is more understandable and readable.
# If you want to read few topics 
#  Book 2 → go to index or chapter


# CODE??

# Code in one stretch or divided
# Which is very bad→code is confusing
# 				→ take more time 
# 				→ not easy to maintain and understand.

# Drawback
# • Repeating code
# • Redundant code /unnecessary,
# • Hard to maintain and update(ginger)
# • Increase the file size.(Space)
# • Lot of  manual work.
# • Code is not readable and understandable.


# SOLUTION — Functions
# A function in Python is a block of reusable code/ statements  that return a specific task.
# It executes the code whenever it is called.
# tea()
# coffee()
# tea()
# tea()
# coffee()
# Benefits:-
# 	• Increase Code Readability 
# 	• Increase Code Reusability
# 	• Easy to update


# Creating and Calling a function
#Creation  Python Function
def hello():
 print("This is a function")
# Calling a  Python Function
hello()


# TEA and Coffee code
def makeTea():
   print("Boil some water")
   print("add tea leaves , milk and sugar")
   print("let it boil for a few minutes")
def makeCoffee():
   print("Boil some water")
   print("add coffee powder, milk and sugar")
   print("let it boil for a few minutes")
# Will this code give any output??? – NO
# Reason – Function code will executes when you call it.
makeTea()
makeCoffee()
makeTea()
makeCoffee()



# Function without arguments
def hello():
   print("Hello Suyash")
hello()    #Hello Suyash
hello()    #Hello Suyash


# Function with arguments
def hello(name):
   print("Hello " ,name)
hello("Suyash")   #Hello Suyash
hello("ABC")      #Hello ABC
hello("DEF")      #Hello DEF


#  Parameters
# Parameters: Parameters are the variables listed inside the parentheses in the function definition. 
# They are placeholders for the values that will be provided when the function is called. 
# Parameters define what kind of arguments a function can accept.

def intro(name):
 print("Hello, " + name)
# In this function, name is a parameter.


# Arguments
# Arguments: Arguments are the actual values or variables that are passed to the function when it is called. 
# They correspond to the parameters defined in the function's definition.


intro("Suyash")

# In this function call, "Suyash" is an argument passed to the intro function.
# In summary, parameters are variables in a function definition, while arguments are the actual values or variables passed to the function when it is called.


# Error

def hello(name):
   print("Hello " ,name)
hello()
# TypeError: hello() missing 1 required positional argument: 'name'


# Find output of this code??

def hello(name):
   print("Hello " ,name)
hello(1)
#hello 1


# Write a function to print square of a number

def add(x, y):
   print(x + y)
add(4,5)

