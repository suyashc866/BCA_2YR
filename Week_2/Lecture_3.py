# ===============================================================

#       LECTURE : 1 - CONTROL STATEMENT - III

# ===============================================================#

# 1. Write a program to input three numbers and print the minimum among them.


# Input three numbers and print the minimum

A = int(input())
B = int(input())
C = int(input())

minimum = A
if B < minimum:
    minimum = B
if C < minimum:
    minimum = C

print("Minimum:", minimum)


# 2. You are given 3 integer angles of a triangle. Tell whether the triangle is valid or not.



# Check if the triangle is valid based on angles

A = int(input())
B = int(input())
C = int(input())

if A + B + C == 180 and A > 0 and B > 0 and C > 0:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# 3. Given 5 numbers A, B, C, D, E as input. Print the average of these 5 numbers.


# Calculate the average of five numbers

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

average = (A + B + C + D + E) / 5
print("Average:", average)


# 4. Accept the percentage from the user and display the grade according to criteria.


# Grade calculator based on percentage

percentage = int(input())

if percentage < 25:
    print("Grade: D")
elif percentage < 45:
    print("Grade: C")
elif percentage < 65:
    print("Grade: B")
elif percentage < 85:
    print("Grade: A")
else:
    print("Grade: A+")
