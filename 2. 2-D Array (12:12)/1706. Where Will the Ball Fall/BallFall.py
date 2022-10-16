#!/usr/bin/env python3
from typing import List

class Solution:
	def findBall(self, grid: List[List[int]]) -> List[int]:
		depth = len(grid)
		width = len(grid[0])
		L = [0 for i in range(width)]
		
		for ball in range(width):
			i = 0
			j = ball
			while i < depth:
				if j == 0 and grid[i][j] == -1:
					L[ball] = -1
					break
				elif j == width-1 and grid[i][j] == 1:
					L[ball] = -1
					break
				elif grid[i][j] == 1 and grid[i][j+1] == -1:
					L[ball] = -1
					break
				elif grid[i][j] == -1 and grid[i][j-1] == 1:
					L[ball] = -1
					break
				if grid[i][j] == 1:
					i += 1
					j += 1
				else:
					i += 1
					j -= 1
			if i == depth:
				L[ball] = j
		return L
	
def main():
	sol = Solution()
	print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
	
if __name__ == "__main__":
	main()