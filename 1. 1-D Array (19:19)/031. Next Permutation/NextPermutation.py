#!/usr/bin/env python3
from typing import List

class Solution:
	def nextPermutation(self, num: List[int]) -> None:
		_num = num[:]
		drop_point = -1
		for i in range(len(_num)-1, 0, -1):
			if _num[i] > _num[i-1]:
				drop_point = i-1
				break
			
		movable = _num[drop_point+1:]
		movable.reverse()
		_num = _num[:drop_point+1] + movable
		tag = 0
		for i in range(len(movable)):
			if movable[i] > _num[drop_point]:
				tag = movable[i]
				break
			#print(wordsList[dropPoint], tag)
		for i in range(drop_point+1, len(_num)):
			if _num[i] == tag:
				_num[i], _num[drop_point] = _num[drop_point], _num[i]
				break
		for i in range(len(_num)):
			num[i] = _num[i]
		

def main():
	sol = Solution()
	num = [2,1,3]
	sol.nextPermutation(num)
	print(num)
	
if __name__ == "__main__":
	main()