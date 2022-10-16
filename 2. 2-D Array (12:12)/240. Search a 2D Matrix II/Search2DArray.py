#!/usr/bin/env python3
from typing import List

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		m = len(matrix)
		n = len(matrix[0])
		
		i,j = 0,0
		
		for col in range(n):
			if matrix[0][col] == target:
				return True
			if matrix[0][col] > target:
				if j == 0:
					return False
			else:
				j += 1
				
		for row in range(m):
			if matrix[row][0] == target:
				return True
			if matrix[row][0] > target:
				if i == 0:
					return False
			else:
				i += 1
				
				
		for row in range(i):
			for col in range(j):
				if matrix[row][col] == target:
					return True
				
		return False

def main():
	sol=Solution()
	print(sol.searchMatrix([[1,4],[2,5]],5))
	
if __name__ == "__main__":
	main()