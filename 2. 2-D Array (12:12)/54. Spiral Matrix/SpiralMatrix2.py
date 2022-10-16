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
		
		p, q = 0,0
		
		while M-2*p > 1 and N-2*q > 1:
			for j in range(q,N-1-q):
				L.append(matrix[p][j])
			for i in range(p,M-1-p):
				L.append(matrix[i][N-1-q])
			for j in range(N-1-q, q, -1):
				L.append(matrix[M-1-p][j])
			for i in range(M-1-p, p, -1):
				L.append(matrix[i][q])
			
			p += 1
			q += 1
		if M-2*p == 1 and N-2*q > 0:
			for j in range(q, N-q):
				
				L.append(matrix[p][j])
		elif N-2*q == 1 and M-2*p>0:
			for i in range(p,M-p):
				L.append(matrix[i][q])
		
		
		return L

def main():
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	sol = Solution()
	print(sol.spiralOrder(matrix))
	
if __name__ == "__main__":
	main()