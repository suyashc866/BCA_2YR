# # # ===============================================================

# # #       LECTURE : 2 -  Longest Palindromic Substring (optimized Approach)

# # # ===============================================================





# Optimised Approach
# Example string (concept explanation):
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
# x  y  b  d  y  z  y  d  b  d   y  z  y  d  x
#                 ↑
#                center

# If the center index of the longest palindromic substring is given ⇒ (example shown at index 11)
# For a palindrome:


# Left pointer = P1


# Right pointer = P2


# Both sides excluded


# Palindrome length = P2 – P1 – 1


# Example:
# Index: -1 0 1 2 3 4 5
#         m a d a m

# Center ⇒ 2
# Length:
# P2 – P1 – 1
# = 5 – (-1) – 1
# = 6 – 1
# = 5


# How to choose the center?
# Check every element as a center.
# We consider two cases:


# Odd length → single index as center


# Even length → pair of indices as center



# Function to find the length of the longest palindrome given two pointers
# int palindromeLength(string s, int P1, int P2) {
#     N = s.length
   
#     while (P1 >= 0 and P2 < N and s[P1] == s[P2]) {
#         P1 -= 1
#         P2 += 1
#     }
#     return (P2 - P1 - 1)
# }


# Function to compute longest palindromic substring length
# int lps(string s) {
#     ans = 1
#     for (i = 0; i < N; i++) {
        
#         // s[i] as center (odd length)
#         P1 = i - 1
#         P2 = i + 1
#         ans = max(ans, palindromeLength(s, P1, P2))

#         // s[i] and s[i+1] as center (even length)
#         P1 = i
#         P2 = i + 1
#         ans = max(ans, palindromeLength(s, P1, P2))
#     }
#     return ans
# }


# Time & Space Complexity
# TC = O(N²)
# SC = O(1)

