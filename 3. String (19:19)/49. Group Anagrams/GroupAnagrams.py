#!/usr/bin/env python3
from typing import List

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		if strs == [""]:
			return [[""]]
		myDict = {}
		for i in range(len(strs)):
			s = "".join(sorted(strs[i]))
			if s not in myDict:
				myDict[s] = [strs[i]]
			else:
				myDict[s].append(strs[i])
		L = []
		for item in myDict.values():
			L.append(item)
		
		return L
		
def main():
	strs = ["eat","tea","tan","ate","nat","bat"]
	sol = Solution()
	print(sol.groupAnagrams(strs))
	
	
if __name__ == "__main__":
	main()