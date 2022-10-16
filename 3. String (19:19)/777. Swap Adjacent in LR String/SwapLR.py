#!/usr/bin/env python3
from typing import List
from collections import Counter

class Solution:
	def canTransform(self, start: str, end: str) -> bool:
		if start.replace("X", "") != end.replace("X", ""):
			return False
		l = len(start)
		startL = [i for i in range(l) if start[i] == 'L']
		endL = [i for i in range(l) if end[i] == 'L']
		startR = [i for i in range(l) if start[i] == 'R']
		endR = [i for i in range(l) if end[i] == 'R']
		for i,j in zip(startL, endL):
			if j > i:
				return False
		for i,j in zip(startR, endR):
			if i > j:
				return False
		return True
		

def main():
	start = "RXLXRXRLXXL"
	end =   "LRXXXRLRXLX"
	print(Solution().canTransform(start, end))
	
if __name__ == "__main__":
	main()