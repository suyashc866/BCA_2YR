# ===============================================================

#       LECTURE : 3 - While loop Questions

# ===============================================================


# 3.Read N,Print sum of digits in N.

# N = 528 => sum = 15

N = int(input())

S = 0
while(N>0):

    digit = N%10
    N = N // 10
    S += digit

print(S)


# 4.Read N and a single digit ‘d ‘, add ‘d’ back to N

# N = 52
# d = 6
# Ans →526

# N * 10  →52 * 10 =>520
#         +d →520 + 6 =>526
# Ans = N * 10 + d


# Solution

N = int(input())
d = int(input())
print(N*10 +d)


# 5.Read N, Print reverse of N


# N = 123 → 321
N = int(input())

ans = 0

while (N > 0):   
    digit = N % 10
    N = N //10
    ans = ans * 10 + digit

print(ans)