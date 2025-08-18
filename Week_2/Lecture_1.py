# ===============================================================

#       LECTURE : 1 - INTRODUCTION OF CONTROL STATEMENT

# ===============================================================

# Python If-Else Statement

a = 10
if a > 0:
	print("positive number")
print("checking numbers")


# Python If-Else Statement

a = 10
if a > 0:
	print("positive number")
else:
	print("negative numbers")
print("checking numbers")


# Python If-Elif-else Statement
a = 10
if a > 0:
    print("positive number")
elif a == 0:
    print("Zero")
else:
    print("Negative number")
print("checking numbers")



# Q1. Eligible to vote exercise questions using if-else statements


age = int(input())

if age >= 18:

    print("You are eligible to vote.")

else:

    print("You are not eligible to vote.")



# Q2. Read a number and check if it is divisible by 7.


N = int(input())

if N%7 == 0:
    print("Yes, N is divisible by 7")
else : 
    print("No, N is not divisible by 7 ")
