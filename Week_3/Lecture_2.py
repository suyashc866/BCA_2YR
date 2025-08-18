# ===============================================================

#       LECTURE : 2 -  Introduction to While loop

# ===============================================================





# What is While Loop in Python?

# While loop statement in Python is used to execute statement(s) repeatedly. 

#  It will keep on repeatedly executing as long as a while condition is true, and it
# will stop repeating only if the condition becomes false.


# Syntax of While Loop in Python


# while expression:

#     statement(s)


# Example

count = 0
while (count < 3):
    print("Hello Suyash")
count = count + 1



# 1.Print all factors/divisor of a given  +ve number.



# N = 10     factor = 1,2,5,10

# N =36      factor = 1,2,3,4,6,12,18,36

# range[1,N]

N = int(input())

i = 1
while (i<=N):

    if(N%i ==0):       #”i is factor”

        print(i)

    i += 1
		
		
		
		
		
# 2.Read N,Print No of digits in N.


# N = 100  →3

# N = 5926 →5

# N / 10 =>5926 /10  →4 times divide => 4 digit
# =============


N = int(input())
digit = 0    #→Initialization

while (N>0):    #→condition
    N = N//10   #→ Update (integer division)
    digit = digit + 1   #→ Work (preparing result)

print(digit)

