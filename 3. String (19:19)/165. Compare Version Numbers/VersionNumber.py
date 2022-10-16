#!/usr/bin/env python3
from typing import List
import itertools

class Solution:
	def compareVersion(self, version1: str, version2: str) -> int:
		v1 = list(map(int,version1.split('.')))
		v2 = list(map(int,version2.split('.')))
		for _,__ in itertools.zip_longest(v1,v2,fillvalue=0):
			if _ == __:
				continue
			return -1 if _ < __ else 1
		return 0
		

def main():
	version1 = "1.01"
	version2 = "1.001"
	sol = Solution()
	print(sol.compareVersion(version1, version2))
	
if __name__ == "__main__":
	main()