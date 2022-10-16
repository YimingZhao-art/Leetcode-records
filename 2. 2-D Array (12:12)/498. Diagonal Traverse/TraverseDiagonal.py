#!/usr/bin/env python3
from typing import List

class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		m = len(mat)
		n = len(mat[0])
		i,j = 0,0
		direction = 1
		L = []
		while i < m and j < n:
			if direction == 1:
				while i > -1 and j < n:
					L.append(mat[i][j])
					if i == m-1 and j == n-1:
						return L
					i -= 1
					j += 1
				direction *= -1
				
				if j == n:
					i += 2
					j -= 1
				else:
					i = i+1
			else:
				while i < m and j > -1:
					L.append(mat[i][j])
					if i == m-1 and j == n-1:
						return L
					j -= 1
					i += 1
				direction *= -1
				if i == m:
					i -= 1
					j += 2
				else:
					j += 1
		return L
			

def main():
	mat = [[1,2,3],[4,5,6],[7,8,9]]
	sol = Solution()
	print(sol.findDiagonalOrder(mat))
	
if __name__ == "__main__":
	main()