"""
1466. Reorder Routes to make all paths lead to city zero
Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-city-zero/
Difficulty: Medium

Approach:
- BFS or DFS to traverse all cities starting from city 0.
- Time Complexity: O(N)
- Space Complexity: O(N)
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        to_visit = deque([0])
        visited = set([0])
        adj = defaultdict(list)
        for road in connections:
            adj[road[0]].append((road[1], 1))
            adj[road[1]].append((road[0], 0))
        
        while to_visit:
            city = to_visit.popleft()
            for neighbor, sign in adj[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    to_visit.append(neighbor)
                    count += sign

        return count
