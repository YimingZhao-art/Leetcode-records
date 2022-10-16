#!/usr/bin/env python3
from typing import List

class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		myDict = {}
		used = {}
		for i in range(len(s)):
			if t[i] not in myDict and s[i] not in used:
				myDict[t[i]] = s[i]
				used[s[i]] = 1
			else:
				if t[i] not in myDict and s[i] in used:
					return False
				if t[i] in myDict and myDict[t[i]] != s[i]:
					return False
		return True
	
def main():
	s = "paper"
	t = "title"
	
	print(Solution().isIsomorphic(s, t))
	
if __name__ == "__main__":
	main()