#!/usr/bin/env python3
from typing import List

class Solution:
	def updateRow(self, matrix, i, n, finalChange=False):
		if finalChange:
			for j in range(n):
				matrix[i][j] = 0
			return
		for j in range(n):
			if matrix[i][j] != 0:
				matrix[i][j] = 2**31
	
	def updateCol(self, matrix, m, j, finalChange=False):
		if finalChange:
			for i in range(m):
				matrix[i][j] = 0
			return
		for i in range(m):
			if matrix[i][j] != 0:
				matrix[i][j] = 2**31

	
	def setZeroes(self, matrix: List[List[int]]) -> None:
		#Use O(1)
		m = len(matrix)
		n = len(matrix[0])
		
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					self.updateRow(matrix, i, n)
					self.updateCol(matrix, m, j)
		
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 2**31:
					matrix[i][j] = 0
		
		

def main():
	matrix = [[1,1,1],[1,0,1],[1,1,1]]
	sol = Solution()
	sol.setZeroes(matrix)
	print(matrix)
	
if __name__ == "__main__":
	main()