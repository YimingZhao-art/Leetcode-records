#!/usr/bin/env python3
from typing import List

class Solution:
	def findBall(self, grid: List[List[int]]) -> List[int]:
		depth = len(grid)
		width = len(grid[0])
		L = [-1 for i in range(width)]
		
		for ball in range(width):
			i = 0
			j = ball
			while i < depth:
				if j < 0 or j > width-1:
					L[ball] = -1
					print(111)
					break
				
				if  j < width-1 and grid[i][j] == 1 and grid[i][j+1] == -1:
					L[ball] = -1
					break
				elif j > 0 and grid[i][j] == -1 and grid[i][j-1] == 1:
					L[ball] = -1
					break
				
				j += grid[i][j]
				i += 1
				
				
			if i == depth and j < width:
				L[ball] = j
			
		return L
	
def main():
	sol = Solution()
	grid = [[1]]
	print(sol.findBall(grid))
	
if __name__ == "__main__":
	main()