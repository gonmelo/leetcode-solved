"""
994. Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/
Difficulty: Medium

Approach:
- TODO: describe the algorithm
- Time Complexity: O(NM)
- Space Complexity: O(NM)
"""
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        fresh_oranges = 0
        m, n = len(grid), len(grid[0])

        # Initial scan to queue the rotten oranges and count fresh ones
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        # Mark the time       
        queue.append((-1, -1))

        # Simulate the rotting process via BFS
        time_elapsed = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                time_elapsed += 1
                if queue:   # avoids infinite loop 
                    queue.append((-1, -1))
            else:
                for direction in directions:
                    neighbour_pos = row + direction[0], col + direction[1]
                    if 0 <= neighbour_pos[0] < m and 0 <= neighbour_pos[1] < n and grid[neighbour_pos[0]][neighbour_pos[1]] == 1:
                        grid[neighbour_pos[0]][neighbour_pos[1]] = 2
                        fresh_oranges -= 1
                        queue.append(neighbour_pos)
        
        return time_elapsed if not fresh_oranges else -1



                        
            
