"""
1071. Greatest Common Divisor of Strings
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
Difficulty: Easy

Approach:
- We can use the gcd (greatest common divisor) of the lengths of the two strings to find the longest common divisor string.
- Time Complexity: O(n), where n is the length of the longer string.
- Space Complexity: O(1)
"""

class Solution:
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        max_len = gcd(len(str1), len(str2))
        return str1[:max_len]