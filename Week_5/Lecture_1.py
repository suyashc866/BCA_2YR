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


