"""
88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Medium

Approach:
- We use a two-pointer technique to merge the two arrays in reverse order.
- Time Complexity: O(m + n)
- Space Complexity: O(1)
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1

        p = m + n - 1
        while p >= 0:
            if p2 < 0:
                break

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1

            else:
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1
            
