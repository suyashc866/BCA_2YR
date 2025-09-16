# ===============================================================

#       LECTURE : 2 -   Senario Based Question


# ===============================================================




# Scenario-Based Questions

# 1. The Exam Result Analyzer

# In a class of n students, each student’s marks are given in a list. A student passes if their marks are greater than or 
# equal to 35.
#  Write a program to count the number of students who passed and failed.

# Input Format
# 	• First line: integer n (1 ≤ n ≤ 1000).
# 	• Second line: n integers (marks of students).

# Output Format
# Print two integers: count of passed students and count of failed students.

# Sample Input
# 6
#  12 67 45 22 90 33
# Sample Output
# 3 3
# Explanation
# Passed = 67, 45, 90 → 3 students.
#  Failed = 12, 22, 33 → 3 students.



n = int(input())                    
marks = list(map(int, input().split()))

passed = 0
failed = 0

for m in marks:
    if m >= 35:
        passed += 1
    else:
        failed += 1

print(passed, failed)




# 2. The Employee ID Filter
# A company stores n employee IDs in a list. The HR wants to print only those IDs that are even numbers
# (since odd IDs are temporary employees).

# Input Format
# 	• First line: integer n (1 ≤ n ≤ 500).
# 	• Second line: n integers (employee IDs).

# Output Format
# Print all even employee IDs separated by space. If none, print -1.

# Sample Input
# 7
#  101 202 303 404 111 222 333
# Sample Output
# 202 404 222

# Explanation
# Only even IDs are selected.




n = int(input())
ids = list(map(int, input().split()))

even_ids = []
for emp in ids:
    if emp % 2 == 0:
        even_ids.append(emp)

if even_ids:
    print(even_ids)
else:
    print(-1)








# 3. The Product Sales Report
# A store keeps a list of sales of n products. Each product has a sales count. 
# The manager wants to print the highest selling product count and the lowest selling product count.
# Input Format
# 	• First line: integer n (1 ≤ n ≤ 1000).
# 	• Second line: n integers (sales count of each product).

# Output Format
# Print two integers: max sales and min sales.
# Sample Input
# 5
#  12 45 23 89 34
# Sample Output
# 89 12
# Explanation
# Maximum sales = 89, Minimum sales = 12.




n = int(input())
sales = list(map(int, input().split()))

max_sales = sales[0]
min_sales = sales[0]

for s in sales:
    if s > max_sales:
        max_sales = s
    if s < min_sales:
        min_sales = s

print(max_sales, min_sales)
