# ===============================================================

#       LECTURE : 2 - CONTROL STATEMENT - II

# ===============================================================

# Q1.Check if it’s last digit is 4.


N = int(input())

last_digit = N%10

if last_digit == 4:
    print("Yes")
else:
    print("No")


# Q2 Check if its divisible by 3 and its last digit is 4.

N = int(input())

if (N%3 == 0) and N % 10 ==4:
    print("Yes")
else:
    print("No")

# Q3. Read a number check if it divisible by 3 or its last digit is 4.


N = int(input())

if (N%3 == 0) or N % 10 ==4:
    print("Yes")
else:
    print("No")