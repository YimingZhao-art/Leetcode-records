#!/usr/bin/env python3
from typing import List

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		m = len(matrix)
		n = len(matrix[0])
		
		row = 0
		col = n-1
		
		while col >= 0 and row < m:
			if matrix[row][col] == target:
				return True
			elif matrix[row][col] < target:
				row += 1
			else:
				col -= 1
		return False
		
def main():
	sol=Solution()
	print(sol.searchMatrix([[-1,3]], 3))
	
if __name__ == "__main__":
	main()