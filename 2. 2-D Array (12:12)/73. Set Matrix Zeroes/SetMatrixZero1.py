#!/usr/bin/env python3
from typing import List

class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		m = len(matrix)
		n = len(matrix[0])
		
		col1Zero = False
		
		for i in range(m):
			if matrix[i][0] == 0:
				col1Zero = True
			for j in range(1, n):
				if matrix[i][j] == 0:
					matrix[i][0] = 0
					matrix[0][j] = 0
					
		for i in range(m-1,-1,-1):
			for j in range(n-1,0,-1):
				if matrix[0][j] == 0 or matrix[i][0] == 0:
					matrix[i][j] = 0
			if col1Zero:
				matrix[i][0] = 0
				
def main():
	matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
	sol = Solution()
	sol.setZeroes(matrix)
	print(matrix)
	
if __name__ == "__main__":
	main()