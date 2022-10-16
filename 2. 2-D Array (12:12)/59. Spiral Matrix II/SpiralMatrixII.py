#!/usr/bin/env python3
from typing import List
import numpy as np

class Solution:
	def generateMatrix(self, n: int) -> List[List[int]]:
		matrix = []
		for i in range(n):
			matrix.append([])
			for j in range(n):
				matrix[i].append([])
			
		M = len(matrix)
		if M == 0:
			return
		N = len(matrix[0])
		count = 1
		if M == 1:
			for j in range(N):
				matrix[0][j] = count
				count += 1
			return matrix
		if N == 1:
			for i in range(M):
				matrix[i][0] = count
				count += 1
			return matrix
		
		p, q = 0,0
		
		while M-2*p > 1 and N-2*q > 1:
			for j in range(q,N-1-q):
				matrix[p][j] = count
				count += 1
			for i in range(p,M-1-p):
				matrix[i][N-1-q] = count
				count += 1
			for j in range(N-1-q, q, -1):
				matrix[M-1-p][j] = count
				count += 1
			for i in range(M-1-p, p, -1):
				matrix[i][q] = count
				count += 1
				
			p += 1
			q += 1
		if M-2*p == 1 and N-2*q > 0:
			for j in range(q, N-q):
				
				matrix[p][j] = count
				count += 1
		elif N-2*q == 1 and M-2*p>0:
			for i in range(p,M-p):
				matrix[i][q] = count
				count += 1
				
		
		return matrix

def main():
	sol = Solution()
	print(sol.generateMatrix(3))
	
if __name__ == "__main__":
	main()