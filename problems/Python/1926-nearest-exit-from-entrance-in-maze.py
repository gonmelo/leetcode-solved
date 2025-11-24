"""
1926. Nearest Exit from Entrance in Maze
Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
Difficulty: Medium

Approach:
- Standard BFS algorithm, the only catch is that the visited is populated on enqueue not dequeue to avoid TLE.
- Time Complexity: O(MN)
- Space Complexity: O(max(M,N)) -> would be O(MN) if we could not mark visited in place
"""
from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        def is_exit(row, col):
            return row == 0 or row == m-1 or col == 0 or col == n-1

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        to_visit = deque()
        maze[entrance[0]][entrance[1]] = "!"
        to_visit.append((tuple(entrance), 1))
        while to_visit:
            pos, steps = to_visit.popleft()
            for direction in directions:
                new_pos = pos[0] + direction[0], pos[1] + direction[1]
                if 0 <= new_pos[0] <= m-1 and 0 <= new_pos[1] <= n-1:
                    if maze[new_pos[0]][new_pos[1]] == ".":
                        if is_exit(new_pos[0], new_pos[1]):
                            return steps
                        to_visit.append((new_pos, steps+1))
                        maze[new_pos[0]][new_pos[1]] = "!"

        return -1
