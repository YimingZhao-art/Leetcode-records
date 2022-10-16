#!/usr/bin/env python3
from typing import List

class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		matrix.reverse()
		for i in range(n):
			for j in range(i+1,n):
				matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
	
	def anticlockRoate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		for each in matrix:
			each.reverse()
		for i in range(n):
			for j in range(i+1,n):
				matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
		
def main():
	matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
	sol = Solution()
	sol.rotate(matrix)
	correct = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
	print(matrix)
	print(correct)
if __name__ == "__main__":
	main()