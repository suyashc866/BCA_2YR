# ===============================================================

#       LECTURE : 3 -   Pattern Problems

# ===============================================================

# Pattern
# 1 
# 1 * 
# 1 * 3 
# 1 * 3 * 
# 1 * 3 * 5 

# Column 1 2 3 4 5
# Col = even = star print
# Col = odd = Number print
N = int(input())
for i in range(1,N+1):
   for j in range(1,i+1):
       if(j%2==0):
           print("*",end=" ")
       else:
           print(j,end=" ")
   print()



# Pattern
# *3space*
# *___*
# *___*
# *___*
# *___*



# 1st and last col => star
# For other print space _

N=int(input())
for i in range(1,N+1):
   for j in range(1,N+1):
       if (j==1)or(j==N):
           print("*",end="")
       else:
           print("_",end="")
   print()




# Pattern            space
# *_____*             5
# *____*              4
# *___*               3
# *__*                2
# *_*                 1


# Star fixed 1st and last 
# Space = > N - i +1  
N=int(input())
for i in range(1,N+1):
   print("*",end="")
   for j in range(N+1-i):
       print("_",end="")
   print("*",end="")
   print()



# Inverted star      space
# ____*                4
# ___* *               3
# __* * *              2
# _* * * *             1
# * * * * *            0



# Space = N - i
# Star = row   = i


N=int(input())
for i in range(1,N+1):
   for j in range(N-i):
       print("_",end="")
   for j in range(i):
       print("*",end="")
   print()



# Pattern      space 
# * * * * *      0
# _* * * *       1
# __* * *        2
# ___* *         3
# ____*          4



# Each row 
# Space = i -1     
Star  = N-i+1    
N=int(input())
for i in range(1,N+1):
   for j in range(i-1):
       print("_",end="")
   for j in range(N-i+1):
       print("*",end="")
   print()


