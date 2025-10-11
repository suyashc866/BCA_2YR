# ===============================================================

#       LECTURE : 1 -  Strings

# ===============================================================



# Strings

# A collection of Characters.
S = "Hello"
print(S)          #Single line String
Books = """ abc
		def
		ghi """
print(Books)  #Multi line String

# Indexing and length of String
Name= "Suyash Chaudhary"
print(Name[0])    #”S”
print(Name[3])    #”a”
print(Name[6])    #”_”
print(Name[-1])  # “y”

# Length of string
print(len(Name)) # 16

# String are immutable
S = "Hello"
print(id(S))
#==========
S = "Hello World"
print(id(S)) 
# Both ids are different ,change the binding
# Strings are immutable it does not change the original string




# Basic Operations

# 1.Concatenation
S1 = "abc"
S2 = "def"
S3 = S1 + S2
print(S3)          #”abcdef”
# 2.Repetition
 
# S = “abc”
print(S * 3)            # “abc” 3 times
# 3.In Operation
 
a = "Suyash Chaudhary teach Python."
target = "Python"
if target in a:
	print("Found")
else:
	print("Not Found")
	
# 4.Count()
 
book = "Harry Half"
print(book.count("H"))         #Output = 2
print(book.count("half"))     #Output = 1

# 5.Find()

# Find the index of a given substring 
# Return the first first substring

# 6.Replace()
S = "Python is  amazing"
#To replace “ amazing”  with “ awesome”
t  = S.replace("amazing" , "awesome")
print(t)    # Created a copy of S with replacement#Python is  awesome
print(S)  #Python is  amazing
# =========
S = "Python is  amazing . Programming is also amazing."
t  = S.replace("amazing" , "awesome",2)
print(t)

# 7. Lower(),Upper() and Capitalize()
S = "Suyash"
U = S.upper()
print(U)
L = S.lower()
print(L)
C = S.capitalize()
print(C)

# 8. Looping over string
# For loops → Iterables
Name = "Suyash Chaudhary"
for x in Name:
	print(x,end=" ")

# ASCII Values

# American Standard Code for Information Interchange.
a = 97
b = 98
C = 99
A = 65
B = 66
C = 67

# Ord() and Chr()

# Ord() → To get the ASCII code for any Character.
print(ord('A')) #→ 65
# Chr() → To get the Character for any ASCII code.
print(chr('66')) #→ B


# Example
# A 
# B B 
# C C C 
# D D D D 

C = 65
N = 4
for i in range(N):
	print((chr(C) + " ") * (i + 1))
	C += 1

# Strip function

S = "_____Hello World_____"
print(S.lstrip("_"))
print(S.rstrip("_"))
print(S.strip("_"))
# ========
S = "Hello World"
S = S.replace("Hello", " " )
print(S)               #delete world

# Join function

# In Python, the join() method is used to concatenate elements of an iterable (such as a list) into a single string. 
# separator.join(iterable)

# Reverse the order of words

names = "Suyash Chaudhary"
Output = "Chaudhary Suyash"
words = names.split()        #return the list of string
print(words)                 #['Suyash', 'Chaudhary']
# =======Reverse()
words = words[::-1]       #['Chaudhary', 'Suyash']
# Or
#words = words.reverse()
print(words)
# ========Join()
res = " ".join(words)
print(res)                       #Chaudhary Suyash


# Reverse each word individually  in a string

book = "Harry Potter and Half"
Output = "yrraH rettoP dna flaH"
words = book.split()
print(words)      #['Harry', 'Potter', 'and', 'Half']
# =====
for i in range(len(words)):
	words[i] = words[i][::-1]
res = " ".join(words)
print(res)      #yrraH rettoP dna flaH


# Check if given strings are anagrams or not.
# Anagrams are words that contain the same characters but in a different order.

string1 = "silent"
string2 = "listen"
string1 = string1.lower()
string2 = string2.lower()
# Sort the characters of both strings
sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)
# Check if the sorted strings are equal
if(sorted_string1 == sorted_string2):
   print("yes")
else:
   print("NO")


#  Amazing Subarrays
# You are given a string S, and you have to find all the amazing substrings of S.
# An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
# Input    ABEC
# Output    6
# Explanation
# Amazing substrings of given string are :
#     1. A
#     2. AB
#     3. ABE
#     4. ABEC
#     5. E
#     6. EC


A = input()
A = A.upper()
N = len(A)
count = 0
for i in range(N):
   if (A[i] == "A" or A[i] == "E" or A[i] == "I" or A[i] == "O" or A[i] == "U"):
       count += N -i
print (count)







