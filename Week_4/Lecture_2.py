# Given N print N no. of Stars


# For N = 5
# *  *  *  *  *
N = int(input())
for i in range(0,N):
	print("*", end = " ")


# Grid Pattern
# N = 3 (rows)
# M = 5(column)

N = int(input())
M = int(input())
for i in range(0,N):
	for j in range(0,M):
		print("*", end = " ")
	print()
# * * * * * 
# * * * * * 
# * * * * * 


# Explanation


N = int(input())
M = int(input())
for i in range(0,N):   # outer loop to print across rows
	#print i th row
	#print ‘M’ no of stars => loop => Repetitive process
	for j in range(0,M):   # Inner loop to print across column
		print("*", end = " ")
	# print new line after each row
	print()  #→ end  value by default => “\ n” ( new line character)


# Star Pattern
# * * * * 
# * * * * 
# * * * * 
# * * * * 


# Row no. = 1 2 3 4
# Star    = 4 4 4 4
N=int(input())
for i in range(N):
   for j in range(N):
           print("*",end=" ")
                  
   print()


# Star pattern
# * 
# * * 
# * * * 
# * * * * 


# Row no. = 1 2 3 4
# Star    = 1 2 3 4
N = int(input())
for i in range(1,N+1):  #print n row
   for j in range(i):#print(i)no.of *
       print("*" , end = " ")
   print()


# Reverse star pattern
# * * * * 
# * * * 
# * * 
# * 


# Star = 4 3 2 1
# Row  = 1 2 3 4
N = int(input())
for i in range(1,N+1):
   for j in range(N+1-i): 
       print("*" , end = " ")
   print()


