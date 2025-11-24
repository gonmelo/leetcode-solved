"""
1. Two sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: TODO

Approach:
- We use a hash map to store the numbers we have seen so far and their indices.
- For each number, we check if it is the complement of a number we have seen before (i.e., target - num).
- If it is, we return the indices of the two numbers.
- If not, we add the number and its index to the hash map.
- Time Complexity: O(n)
- Space Complexity: O(n)
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in mapping:
                return mapping[num], i
            else:
                mapping[target - num] = i
