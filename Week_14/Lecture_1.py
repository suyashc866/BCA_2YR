# # ===============================================================

# #       LECTURE : 1 -  Introduction to Bit manipulation

# # ===============================================================




# Bitwise Operation

# Operators

# Operator	Symbol
# AND	          &
# OR	          |
# XOR	          ^



# Inverse (NOT)	~

# a	b	a & b	a | b	a ^ b	~a	~b
# 0	0	0	       0	0	1	1
# 0	1	0	       1	1	1	0
# 1	0	0	       1	1	0	1
# 1	1	1	       1	0	0	0

# Basic Problems on Bitwise Operators

# Example 1:
# a = 29
# b = 19


# Binary representation:

# a = 1 1 1 0 1
# b = 1 0 0 1 1

# Operation	Result	Binary
# a & b	17	1 0 0 0 1
# a | b	31	1 1 1 1 1
# a ^ b	14	0 1 1 1 0

# Example 2:
# a = 13
# b = 10


# Binary representation:

# a = 1 1 0 1
# b = 1 0 1 0

# Operation	Result	Binary
# a & b	     8	1 0 0 0
# a | b	    15	1 1 1 1
# a ^ b	    7	0 1 1 1


# Properties of Bitwise Operation
# Example 1:
# a = 10 (1 0 1 0)
# 1 = (0 0 0 1)
# a & 1 = 0 0 0 0

# Example 2:
# a = 11 (1 0 1 1)
# 1 = (0 0 0 1)
# a & 1 = 0 0 0 1

# Example 3:
# a = 4  (1 0 0)
# 1 = (0 0 1)
# a & 1 = 0 0 0

# Example 4:
# a = 13 (1 1 0 1)
# 1 = (0 0 0 1)
# a & 1 = 0 0 0 1

# Observations
# a	b	a & b	Remark
# 10	1	   0	Even → 0
# 11	1	   1	Odd → 1
# 18	1	   0	Even
# 19	1	   1	Odd

# If (a & 1 == 0) → a is even
# Else → a is odd

# Few More Properties
# Expression	Result
# a & 0	          0
# a | 0	          a
# a & a	          a
# a | a	          a
# a ^ 0	          a
# a ^ a	          0


# Commutative Property
# a & b = b & a
# a | b = b | a
# a ^ b = b ^ a




# Associative Property
# a & (b & c) = (a & b) & c = b & a & c
# a | (b | c) = (a | b) | c = b | a | c
# a ^ (b ^ c) = (a ^ b) ^ c = b ^ a ^ c




# Questions
# 1. What is the value of:
# a ^ b ^ a  ^ b ^ d
# d


# → a & a = a
# → a & a = 0 (for XOR)
# → So, a & b & a & b = ?

# If using XOR:

# a ^ a = 0
# a ^ 0 = a


# c ^ f ^ a ^ f ^ c ^ g ^ a
# g

