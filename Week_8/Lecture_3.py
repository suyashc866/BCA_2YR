# ===============================================================

#       LECTURE : 3 -   Senario Based Question


# ===============================================================



# 4. The Scholarship Eligibility
# In a university, n students applied for scholarships. The eligibility criteria are:
# 	• The student’s marks must be greater than or equal to 75.
# 	• The student’s attendance percentage must be greater than or equal to 80.

# Write a program to count how many students are eligible for scholarships.

# Input Format
# 	• First line: integer n (1 ≤ n ≤ 500).
# 	• Next n lines: each contains two integers → marks and attendance percentage.

# Output Format
# Print the number of eligible students.

# Sample Input
# 4
# 85 90
# 70 85
# 75 80
# 90 70
# Sample Output
# 2
# Explanation
# (85,90) eligible
# (70,85) (marks < 75)
# (75,80)  eligible
# (90,70) (attendance < 80)






n = int(input())

eligible = 0  

for i in range(n):
    data = input().split()     
    marks = int(data[0])        
    attendance = int(data[1])
    
    if marks >= 75 and attendance >= 80:   
        eligible += 1

print(eligible)



# 5.The Perfect Pair Finder
# A company maintains a list of project deadlines (in days). Two projects are called a perfect pair if the sum of their deadlines is exactly equal to a given target k.
#  Find how many such pairs exist in the list.

# Input Format
# 	• First line: integer n (1 ≤ n ≤ 1000).
# 	• Second line: n integers (project deadlines).
# 	• Third line: integer k.

# Output Format
# Print the number of perfect pairs.

# Sample Input
# 6
# 1 5 7 -1 5 3
# 6
# Sample Output
# 3
# Explanation
# Pairs are: (1,5), (7,-1), (1,5). → Total 3 pairs.





n = int(input())
data = input().split()
deadlines = []
for i in range(n):
    deadlines.append(int(data[i]))

k = int(input())

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if deadlines[i] + deadlines[j] == k:
            count += 1


print(count)


# 7. The Stock Price Fluctuation
# A company records daily stock prices of n days. The manager wants to know how many days the stock price was strictly higher than the previous day.
# Input Format
# 	• First line: integer n (1 ≤ n ≤ 1000).
# 	• Second line: n integers (stock prices).

# Output Format
#  Print the number of days where price increased compared to the previous day.
# Sample Input
# 7  
# 100 102 101 105 107 106 110
# Sample Output
# 4


n = int(input())
prices = list(map(int, input().split()))

count = 0
for i in range(1, n):
    if prices[i] > prices[i-1]:
        count += 1

print(count)