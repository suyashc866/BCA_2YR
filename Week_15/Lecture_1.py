# # ===============================================================

# #       LECTURE : 1 -  Longest Palindromic Substring

# # ===============================================================


# Longest Palindromic Substring

# Given a string, calculate the length of the longest palindromic substring.

# Ex:1
# Index: 0 1 2 3 4 5
#        a b c a b c


# aba → length = 3
# aca → length = 3
# bcacb → length = 5

# Ans → 5


# Ex:2
# Index: 0 1 2 3 4
#        a b c d e
# a → 1

# b → 1



# Ans → 1

# Ex:3
# Index: 0 1 2 3 4
#        m a d a m


# Ans → 5

# Brute Force Idea

# For every substring,
# check if it is a palindrome or not → get max length palindrome.



def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def lps(s):
    n = len(s)
    ans = 1  # at least every single character is a palindrome
    
    for l in range(n):
        for r in range(l, n):
            if is_palindrome(s, l, r):
                length = r - l + 1
                ans = max(ans, length)
    
    return ans


# Example
s = "abac"
print(lps(s))   # Output: 3


# Time Complexity: O(N³)

# N² substrings

# N time to check palindrome

# Space Complexity: O(1)