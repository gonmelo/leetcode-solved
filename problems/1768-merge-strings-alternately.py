"""
1768. Merge Strings Alternately
Link: https://leetcode.com/problems/merge-strings-alternately/
Difficulty: Easy

Approach:
- We will iterate through the characters of both strings simultaneously, appending one character from each string to the result in each iteration.
- Time Complexity: O(n), where n is the length of the longer string.
- Space Complexity: O(n), where n is the length of the longer string.
"""
from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        len_1 = len(word1)
        len_2 = len(word2)
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len_1:
                res += word1[i]
            if i < len_2:
                res += word2[i]

        return res
