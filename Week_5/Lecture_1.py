# ===============================================================

#       LECTURE : 1 -  Pattern Problems

# ===============================================================





# Hollow Pyramid Pattern
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# Each row = N
# Star = N -i +1
# Space = 2i - 2
# Star = N - i +1
N=int(input())
for i in range(1,N+1):
   for j in range(N-i+1):
       print("*",end="")
   for j in range(2*i-2):
       print(" ",end="")
   for j in range(N-i+1):
       print("*",end="")
   print()



# Pattern        Star     Space
# *        *     1           8
# **      **     2           6
# ***    ***     3           4
# ****  ****     4           2
# **********     5           0



# Each row 
# Star = i
# Space = 2N-2i
# Star = i
N=int(input())
for i in range(1,N+1):
   for j in range(i):
       print("*",end="")
   for j in range(2*N-2*i):
       print(" ",end="")
   for j in range(i):
       print("*",end="")
   print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4


N=int(input())
for i in range(1,N+1):
   for j in range(1,i+1):
       print(j,end="")
       
      
   print()


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


N=int(input())
for i in range(0,N+1):
   for j in range(1,N-i+1):
           print(j,end="")
                 
   print()


# Pattern            value
# 1                    1
# 2 3                  2
# 4 5 6                3
# 7 8 9 10             4


N=int(input())
k=1
for i in range(1,N+1):
   for j in range(i):
       print(k,end=" ")
       k=k+1
   print()


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


N=int(input())
for i in range(1,N+1):
   for j in range(i):
       print("*",end="")
   print()
for i in range(1,N+1):
   for j in range(N-i,0,-1):
       print("*",end="")
   print()


