#!/usr/bin/env python3
from typing import List

class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		for k in range(int(n/2)):
			for j in range(n-1-k):
				if k+j ==n-1-k:
					break
				#print("k is",k,'j is',j,'temp is',matrix[k][k+j])
				temp = matrix[k][k+j]
				matrix[k][k+j] = matrix[n-k-1-j][k]
				matrix[n-k-1-j][k] = matrix[n-1-k][n-1-k-j]
				matrix[n-1-k][n-1-k-j] = matrix[k+j][n-1-k]
				matrix[k+j][n-1-k] = temp
		
		
def main():
	matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
	sol = Solution()
	sol.rotate(matrix)
	correct = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
	print(matrix)
	print(correct)
if __name__ == "__main__":
	main()