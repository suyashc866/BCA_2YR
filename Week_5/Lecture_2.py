# ===============================================================

#       LECTURE : 2 -  Star Pattern Sheet


# ===============================================================



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


