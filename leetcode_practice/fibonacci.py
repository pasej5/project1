#!/usr/bin/env python3

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])