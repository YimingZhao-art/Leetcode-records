#!/usr/bin/env python3
from typing import List

class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		m = len(mat)
		n = len(mat[0])
		_dict = {}
		L = []
		for i in range(m):
			for j in range(n):
				if i+j not in _dict:
					_dict[i+j] = [mat[i][j]]
				else:
					_dict[i+j].append(mat[i][j])
		print(_dict)
		for key in _dict:
			if key % 2 == 1:
				L.extend(_dict[key])
			else:
				L.extend(reversed(_dict[key]))

		return L
	
def main():
	mat = [[1,2,3],[4,5,6],[7,8,9]]
	sol = Solution()
	print(sol.findDiagonalOrder(mat))
	
	
if __name__ == "__main__":
	main()