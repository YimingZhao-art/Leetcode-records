#!/usr/bin/env python3
from typing import List

class Solution:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		m = len(grid)
		n = len(grid[0])

		perimeter = 0
		
		for i in range(m):
			for j in range(n):
				if grid[i][j] != 1:
					continue
				xList = [i-1, i, i, i+1]
				yList = [j, j-1, j+1, j]
				_un = 0
				
				for _ in range(4):
					if xList[_] > -1 and xList[_] < m and yList[_] > -1 and yList[_] < n:
						if grid[xList[_]][yList[_]] == 1:
							_un += 1
				perimeter += (4-_un)
					
						
		
		return perimeter

def main():
	
	
if __name__ == "__main__":
	main()