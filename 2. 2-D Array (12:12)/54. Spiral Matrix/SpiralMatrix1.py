#!/usr/bin/env python3
from typing import List

class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		L = []
		M = len(matrix)
		if M == 0:
			return
		N = len(matrix[0])
		if M == 1:
			for j in range(N):
				L.append(matrix[0][j])
			return L
		if N == 1:
			for i in range(M):
				L.append(matrix[i][0])
			return L
		for j in range(N-1):
			L.append(matrix[0][j])
		for i in range(M-1):
			L.append(matrix[i][N-1])
		for j in range(N-1, 0, -1):
			L.append(matrix[M-1][j])
		for i in range(M-1, 0, -1):
			L.append(matrix[i][0])
		
		if M == 2 or N == 2:
			return L
		
		submatrix = matrix[1:M-1]
		for i in range(len(submatrix)):
			submatrix[i] = submatrix[i][1:N-1]
		if submatrix == None:
			return
		L.extend(self.spiralOrder(submatrix))
		return L


def main():
	matrix = [[1,2],[3,4]]
	sol = Solution()
	print(sol.spiralOrder(matrix))
	
if __name__ == "__main__":
	main()